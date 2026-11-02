#!/usr/bin/env python3
"""Check build/guide.html. Exit status 1 on any failure.

    python check.py              # structural + render checks
    python check.py --no-render  # structural checks only (no browser)

Render checks (from legacy/chk4.py) need Playwright and a local MathJax:
    .venv/bin/pip install playwright pyyaml && npm install
They use the system Chromium (CHROMIUM env var, default /usr/bin/chromium) and
serve MathJax from node_modules/, so they work without network access.
"""
import os
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGE = Path(next((a for a in sys.argv[1:] if not a.startswith('--')), ROOT / 'build/guide.html'))
fails = []


def check(name, ok, detail=''):
    print('%-4s %s%s' % ('ok' if ok else 'FAIL', name, ('  ' + detail) if detail and not ok else ''))
    if not ok:
        fails.append(name)


def structural(g):
    html_part = re.sub(r'<script>.*?</script>', '', g, flags=re.S)
    ids = re.findall(r'\bid="([^"]+)"', html_part)
    dup = sorted({i for i in ids if ids.count(i) > 1}) if len(ids) != len(set(ids)) else []
    check('no duplicate ids', not dup, str(dup[:10]))
    dangling = sorted(set(re.findall(r'href="#([^"]+)"', html_part)) - set(ids))
    check('no dangling href="#..."', not dangling, str(dangling[:10]))
    items = re.findall(r'<div class="env (\w+)" id="it-[\d-]+" data-label="[^"]*">(<span class="tag (\w)">)?', g)
    untagged = [c for c, _, t in items if not t and c not in ('rem', 'ex')]
    check('every numbered theorem/definition/assumption has a status tag', not untagged, str(len(untagged)))
    check('no unresolved source syntax', not re.search(r'\]\((?:@|=|apx:)|^::: |\{\{fig:', html_part, re.M),
          str(re.findall(r'.{30}(?:\]\((?:@|=|apx:)|\{\{fig:).{30}', html_part)[:3]))
    bad_class = re.findall(r'\\(?:frac|sqrt)\s*\\class', g)
    check('no \\frac\\class / \\sqrt\\class (needs braces)', not bad_class, str(bad_class[:3]))
    keys = set(re.findall(r'"([\w-]+)": \{"h"', g))
    used = set(re.findall(r'\\class\{ntn-([\w-]+)\}', g))
    check('every \\class{ntn-KEY} has a NOTE entry', used <= keys, str(sorted(used - keys)[:10]))
    check('no $$ display math (not enabled)', '$$' not in html_part)


def render(g):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        check('render check (playwright installed)', False, 'run: .venv/bin/pip install playwright, or use --no-render')
        return
    mj = ROOT / 'node_modules/mathjax/es5'
    if not (mj / 'tex-svg.js').exists():
        check('render check (local MathJax)', False, 'run: npm install')
        return
    with tempfile.TemporaryDirectory() as tmp:
        page_file = Path(tmp) / 'w.html'
        page_file.write_text('<!doctype html><html><head><meta charset=utf-8>'
                             '<meta name="viewport" content="width=device-width, initial-scale=1"></head><body>'
                             + g + '</body></html>')
        with sync_playwright() as p:
            b = p.chromium.launch(executable_path=os.environ.get('CHROMIUM', '/usr/bin/chromium'))
            pg = b.new_page()
            console = []
            pg.on('console', lambda m: console.append(m.text[:200]) if m.type == 'error' else None)

            def route(r):
                u = r.request.url
                if 'mathjax/3.2.2/es5/' in u:
                    r.fulfill(path=str(mj / u.split('/es5/')[1].split('?')[0]), content_type='application/javascript')
                elif u.startswith('file://'):
                    r.continue_()
                else:
                    r.fulfill(body='', content_type='text/css')
            pg.route('**/*', route)
            pg.goto(page_file.as_uri(), wait_until='domcontentloaded', timeout=120000)
            pg.wait_for_function('() => window.MathJax && MathJax.startup && MathJax.startup.promise', timeout=120000)
            pg.evaluate('() => MathJax.startup.promise')
            n = pg.evaluate('() => document.querySelectorAll("mjx-container").length')
            check('MathJax typeset the page (%d formulas)' % n, n > 1000)
            errs = pg.eval_on_selector_all(
                '[data-mml-node="merror"]',
                'e => e.map(x => (x.getAttribute("data-mjx-error") || x.textContent) + " | " + '
                '(x.closest("section,div.apx,div.lecture") || {id: ""}).id)')
            check('0 MathJax errors', not errs, '; '.join(errs[:10]))
            check('no console errors', not console, '; '.join(console[:5]))
            pg.set_viewport_size({'width': 400, 'height': 800})
            pg.wait_for_timeout(1500)
            sw = pg.evaluate('document.documentElement.scrollWidth')
            wide = []
            if sw != 400:
                wide = pg.evaluate('''() => { const o = []; document.querySelectorAll('.wrap *').forEach(e => {
                    const r = e.getBoundingClientRect(); if (r.right > 401 && !e.closest('mjx-container[display], .tbl'))
                    o.push(Math.round(r.right) + ' ' + (e.closest('section') || {id: ''}).id + ' ' + e.tagName); });
                    return o.slice(0, 8); }''')
            check('scrollWidth is 400 at a 400 px viewport (got %d)' % sw, sw == 400, '; '.join(wide))
            b.close()


def main():
    if not PAGE.exists():
        sys.exit('build/guide.html is missing; run python build.py first')
    g = PAGE.read_text()
    structural(g)
    if '--no-render' not in sys.argv:
        render(g)
    print('\ncheck: %s' % ('PASS' if not fails else 'FAIL (%d)' % len(fails)))
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
