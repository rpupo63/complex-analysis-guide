import sys, os
from playwright.sync_api import sync_playwright
f=sys.argv[1]
s=open(f).read()
open('w.html','w').write('<!doctype html><html><head><meta charset=utf-8></head><body>'+s+'</body></html>')
base=os.path.abspath('node_modules/mathjax/es5')
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page()
    pg.on('console', lambda m: print('console', m.type, m.text[:150]) if m.type=='error' else None)
    def h(r):
        u=r.request.url
        if 'mathjax/3.2.2/es5/' in u: r.fulfill(path=base+'/'+u.split('/es5/')[1].split('?')[0], content_type='application/javascript')
        elif 'fonts.' in u: r.fulfill(body='', content_type='text/css')
        else: r.continue_()
    pg.route('**/*', h)
    pg.goto('file://'+os.path.abspath('w.html'), wait_until='domcontentloaded', timeout=120000)
    prev=-1
    for i in range(60):
        pg.wait_for_timeout(2000)
        st=pg.evaluate('()=>[typeof MathJax.version, document.querySelectorAll("mjx-container").length]')
        if st[0]=="string" and i>2 and st[1]==prev: break
        prev=st[1]
    pg.evaluate('()=>MathJax.startup.promise.then(()=>1)'); pg.wait_for_timeout(2000)
    print(pg.evaluate('()=>[MathJax.startup.document.math.length, document.body.innerText.includes("Missing argument")]'))
    errs=pg.eval_on_selector_all('[data-mml-node="merror"]', 'e=>e.map(x=>(x.getAttribute("data-mjx-error")||x.textContent)+" | "+(x.closest("section,div.apx,div.lecture")||{id:""}).id)')
    print(st, len(errs)); print('\n'.join(errs[:40]))
    pg.set_viewport_size({'width':400,'height':800}); pg.wait_for_timeout(1500)
    print('sw', pg.evaluate('document.documentElement.scrollWidth'))
    print(pg.evaluate('''()=>{const o=[];document.querySelectorAll('.wrap mjx-container:not([display]), .wrap figure svg').forEach(e=>{const r=e.getBoundingClientRect(); if(r.right>401) o.push(Math.round(r.right)+' '+(e.closest('section')||{id:''}).id+' | '+e.textContent.slice(0,80))}); return o.join('\\n')}'''))
    for sid in ['n1','n5','n10','n12','o5']:
        pg.evaluate(f"document.getElementById('{sid}').scrollIntoView()"); pg.wait_for_timeout(300); pg.screenshot(path=f'shot_{sid}.png')
    b.close()
