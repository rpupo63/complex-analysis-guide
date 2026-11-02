import re, html, json
G = open('guide.html').read()
FIG = json.load(open('figs3.json'))

def rep(old, new, s=None):
    global G
    assert G.count(old) == 1, (G.count(old), old[:80])
    G = G.replace(old, new)

OV = {
 12: ("Transport harmonic functions between regions by holomorphic bijections; build the local theory of holomorphic maps (local behaviour, open mapping, inverse theorem); classify the automorphisms of the disk with the Schwarz lemma.",
      "Lemma 12.2.1 (harmonic conjugates) · Theorem 12.3.1 (harmonic under holomorphic maps) · Prop. 12.4.1 (Cayley map) · Theorem 12.6.1 (local behaviour) · Theorem 12.7.1 (open mapping) · Theorem 12.9.1 (inverse) · Theorem 12.14.1 (Schwarz lemma) · Theorem 12.15.1 (automorphisms of the disk) · Theorem 12.16.1 (Liouville)",
      "Rouché's theorem (Theorem 11.10.1); the identity theorem (Theorem 10.1.1); removable singularities and maximum modulus (Lemma 9.1.1, Lemma 9.6.1); Cauchy's estimate (Cor. 6.5.2).",
      "Lecture 13 · Problem 4 of the practice midterms (conformal maps, the Schwarz lemma)."),
 13: ("Prove the Riemann mapping theorem for regions made of grid squares, by building the conformal map out of the solution of a Dirichlet problem.",
      "Prop. 13.1.2 (what a Riemann map must look like; uniqueness) · Theorem 13.2.1 (Riemann mapping theorem) · Prop. 13.5.1 (counting) · Lemma 13.7.2 (star-shaped sets)",
      "Theorem 5.1.1, the main result of Part I; Lecture 12; the argument principle (Theorem 7.3.1).",
      "The course ends here: Part I's Dirichlet problem and Parts II–IV's complex analysis meet in one theorem."),
}
def ov_html(L):
    g, m, u, l = OV[L]
    rows = [('Goal', g), ('Main results', m), ('Uses', u), ('Used later', l)]
    return '<div class="ov">' + ''.join('<div class="ov-row"><span class="ov-k">%s</span><div>%s</div></div>' % r for r in rows) + '</div>'

UNIT = '''<div class="unit" id="P5">
  <span class="eyebrow">Part V</span>
  <h2>Conformal maps</h2>
  <p>A holomorphic bijection between two regions carries harmonic functions on one to harmonic functions on the other, so a Dirichlet problem on a complicated region can be moved to the disk. Lecture 12 develops the tools: harmonic conjugates, the open mapping and inverse theorems, angle preservation, examples, the automorphisms of the disk and the Schwarz lemma. Lecture 13 runs the logic the other way: it builds the conformal map onto the disk out of the solution of a Dirichlet problem, so Part I's existence theorem becomes the Riemann mapping theorem for regions made of squares.</p>
</div>

'''

new = ''
for L in (12, 13):
    t = open('l%d.html' % L).read().replace('<!--OV:L%d-->' % L, ov_html(L))
    for k, v in FIG.items(): t = t.replace('<!--FIG:%s-->' % k, v)
    assert '<!--FIG' not in t
    new += ('\n\n' + UNIT if L == 12 else '\n\n') + t

# ---- 1. ids on items ----
ABBR = {'Definition':'Def.','Proposition':'Prop.','Theorem':'Thm.','Corollary':'Cor.','Remark':'Rem.','Lemma':'Lemma',
        'Hypothesis':'Hyp.','Setting':'Setting','Fact':'Fact','Example':'Ex.','Convention':'Conv.','Exercise':'Exercise'}
item_ids = set(re.findall(r'id="(it-[\d-]+)"', G))
def add_id(m):
    word, num = m.group(3), m.group(4)
    iid = 'it-' + num.replace('.', '-')
    assert iid not in item_ids, iid
    item_ids.add(iid)
    return f'{m.group(1)} id="{iid}" data-label="{ABBR.get(word, word)} {num}"{m.group(2)}'
new = re.sub(r'(<div class="env [a-z]+")(>\s*(?:<span class="tag [a-z]">[^<]*</span>)?<span class="hd">([A-Z][a-z]+(?: [a-z]+)?) (\d+\.\d+(?:\.\d+)?))', add_id, new)

# ---- 2. reference linking in text nodes ----
KW = r'(?:Exercises?|Conventions?|Conv\.|Examples?|Facts?|Props?\.|Propositions?|Lemmas?|Theorems?|Thms?\.|Cor\.|Corollar(?:y|ies)|Defs?\.|Definitions?|Hyps?\.|Hypothes[ie]s|Remarks?|Rem\.|assumptions?|Setting)'
NUM = r'\d+\.\d+(?:\.\d+)?(?:\([a-z]\))?'
REF = re.compile(r'(' + KW + r')(\s+)(' + NUM + r'(?:(?:,\s*|\s+and\s+|\s+or\s+)' + NUM + r')*)')
missing = []
def link_num(numtxt, label):
    base = re.match(r'\d+\.\d+(?:\.\d+)?', numtxt).group(0)
    iid = 'it-' + base.replace('.', '-')
    if iid not in item_ids:
        missing.append(numtxt); return label
    return f'<a class="ir" href="#{iid}">{label}</a>'
SEC3 = {1:'s2',2:'s3',3:'s4',4:'s5',5:'s6',6:'s7',7:'s8',8:'s9',9:'s10',10:'s11',11:'s12',12:'s13',13:'s14',14:'s15',15:'s16',16:'s17',17:'s18',18:'s20',19:'s21'}
APX = set(re.findall(r'<div class="apx" id="([A-E]\d+)"', G))
def link_refs(text):
    def f(m):
        kw, sp, nums = m.groups()
        out, first = [], True
        for p in re.split(r'(' + NUM + r')', nums):
            if re.fullmatch(NUM, p):
                out.append(link_num(p, (kw + sp + p) if first else p)); first = False
            else: out.append(p)
        return ''.join(out)
    text = REF.sub(f, text)
    def sec(m):
        L, k = int(m.group(1)), m.group(2)
        if k is None: return m.group(0)
        k = int(k)
        sid = {1:'x%d'%k, 2:'w%d'%k, 3:SEC3.get(k), 4:'t%d'%(k+1), 5:'v%d'%(k+1), 6:'f%d'%k, 7:'g%d'%k, 8:'h%d'%k,
               9:'j%d'%k, 10:'k%d'%k, 11:'m%d'%k, 12:'n%d'%k, 13:'o%d'%k}.get(L)
        return f'<a class="ir" href="#{sid}">§{L}.{k}</a>' if sid else m.group(0)
    text = re.sub(r'§(\d+)(?:\.(\d+))?', sec, text)
    text = re.sub(r'(?<![\w.#>])([A-E])\.(\d{1,2})(?![\d])', lambda m: f'<a class="x" href="#{m.group(1)}{m.group(2)}">{m.group(0)}</a>' if (m.group(1)+m.group(2)) in APX else m.group(0), text)
    return text

parts = re.split(r'(<[^>]+>)', new)
out = []; after_hd = False; in_a = 0; in_math_tag = 0
for p in parts:
    if p.startswith('<'):
        after_hd = p == '<span class="hd">'
        if p.startswith('<a '): in_a += 1
        elif p == '</a>': in_a -= 1
        out.append(p); continue
    if not p: continue
    segs = re.split(r'(\$[^$]*\$|\\\[.*?\\\])', p, flags=re.S)
    res = []
    for i, seg in enumerate(segs):
        if i % 2 or after_hd or in_a: res.append(seg)
        else: res.append(link_refs(seg))
    out.append(''.join(res)); after_hd = False
new = ''.join(out)

# ---- 3. appendix links: ids, data-from, chips, cited-in ----
counts = {}
for m in re.finditer(r'id="r-([A-E]\d+)-(\d+)"', G):
    counts[m.group(1)] = max(counts.get(m.group(1), 0), int(m.group(2)))
def lab(t): return t[0] + '.' + t[1:]
state = {'slide': '', 'item': ''}
cites = {}
pat = re.compile(r'<span class="eyebrow">(.*?)</span>|<span class="hd">([A-Z][a-z]+(?: [a-z]+)?) (\d+\.\d+(?:\.\d+)?)|<a class="x" href="#(\w+)">(.*?)</a>', re.S)
def sub(m):
    if m.group(1) is not None:
        if re.match(r'L\d+ ·', m.group(1)): state['slide'] = m.group(1); state['item'] = ''
        return m.group(0)
    if m.group(2):
        state['item'] = ABBR.get(m.group(2), m.group(2)) + ' ' + m.group(3); return m.group(0)
    tid, text = m.group(4), m.group(5)
    counts[tid] = counts.get(tid, 0) + 1
    rid = f'r-{tid}-{counts[tid]}'
    where = state['slide'] + (' · ' + state['item'] if state['item'] else '')
    cites.setdefault(tid, []).append((rid, where))
    chip = '' if re.sub('<.*?>', '', text).strip() == lab(tid) else f'<span class="xl">{lab(tid)}</span>'
    return f'<a class="x" id="{rid}" href="#{tid}" data-from="{html.escape(where)}">{text}{chip}</a>'
new = pat.sub(sub, new)
for tid, lst in cites.items():
    seen = set(); links = ''
    for rid, where in lst:
        if where in seen: continue
        seen.add(where)
        links += f'<a class="bk" href="#{rid}" data-from="Appendix {lab(tid)}">{html.escape(where)}</a>'
    i = G.index(f'<div class="apx" id="{tid}">')
    j = G.index('</div>', G.index('<div class="apx-hd">', i)) + len('</div>')
    k = G.find('<p class="usedin">', i)
    nxt = G.find('<div class="apx"', i + 10)
    if k != -1 and (nxt == -1 or k < nxt):
        e = G.index('</p>', k)
        G = G[:e] + links + G[e:]
    else:
        G = G[:j] + '\n<p class="usedin"><span>Cited in</span>' + links + '</p>' + G[j:]

# ---- 4. insert lectures ----
rep('\n\n<!-- ============ INDEX ============ -->', new + '\n\n<!-- ============ INDEX ============ -->')

# ---- 5. TOC ----
def toc_for(L, src, title):
    items = re.findall(r'<section id="(\w+)">\s*<header><span class="eyebrow">L%d · (Slides? [^<]*)</span><h2>\d+\.\d+ (.*?)</h2>' % L, src)
    o = '<p class="toc-part"><a href="#L%d">Lecture %d · %s</a></p>\n<ol class="toc">\n' % (L, L, title)
    for sid, sl, t in items: o += '  <li><span class="n">%s</span><a href="#%s">%s</a></li>\n' % (sl, sid, t)
    return o + '</ol>\n'
toc = '<p class="toc-unit"><a href="#P5">Part V · Conformal maps</a></p>\n' + toc_for(12, new, 'Conformal maps') + toc_for(13, new, 'The Riemann mapping theorem')
rep('<p class="toc-unit">Reference</p>', toc + '<p class="toc-unit">Reference</p>')

# ---- 6. index rows ----
IDX = '''<tr><td colspan="3" class="idx-part">Lecture 12</td></tr>
<tr><td><span class="tag d">Defined</span></td><td>The plate problem; conformal map; automorphism, $\\varphi_a$; simply connected</td><td>12.1.1, 12.9.2, 12.13.1, 12.17.1</td></tr>
<tr><td><span class="tag c">Cited</span></td><td>Riemann mapping theorem (general form)</td><td>12.17.2</td></tr>
<tr><td><span class="tag r">Derived</span></td><td>$\\frac1\\pi\\arg z$ on $\\mathbb H$; harmonic conjugates on a disk; harmonic under holomorphic maps; transport; the Laplacian under $f$</td><td>12.1.2, 12.2.1, 12.3.1, 12.3.2, 12.3.3</td></tr>
<tr><td><span class="tag r">Derived</span></td><td>Cayley map; the plate solved</td><td>12.4.1, 12.5.1</td></tr>
<tr><td><span class="tag r">Derived</span></td><td>Local behaviour; open mapping; local injectivity; inverse theorem</td><td>12.6.1, 12.7.1, 12.8.1, 12.9.1</td></tr>
<tr><td><span class="tag r">Derived</span></td><td>Angles; the strip; Joukowski map</td><td>12.10.1, 12.11.1, 12.12.1</td></tr>
<tr><td><span class="tag r">Derived</span></td><td>$\\varphi_a$ is an automorphism; Schwarz lemma; all automorphisms of the disk</td><td>12.13.2, 12.14.1, 12.15.1</td></tr>
<tr><td><span class="tag r">Derived</span></td><td>Liouville; fundamental theorem of algebra; no conformal map $\\mathbb C\\to D(0,1)$; uniqueness of Riemann maps</td><td>12.16.1, 12.16.2, 12.16.3, 12.17.3</td></tr>
<tr><td colspan="3" class="idx-part">Lecture 13</td></tr>
<tr><td><span class="tag a">Assumed</span></td><td>A conformal map onto the disk is given</td><td>13.1.1</td></tr>
<tr><td><span class="tag r">Derived</span></td><td>What a Riemann map must look like; Riemann mapping theorem under (D), (C); the disk</td><td>13.1.2, 13.2.1, 13.3.1</td></tr>
<tr><td><span class="tag r">Derived</span></td><td>Counting proposition; Blaschke products; existence of a zero</td><td>13.5.1, 13.6.2, 13.6.3</td></tr>
<tr><td><span class="tag r">Derived</span></td><td>(C) is necessary; star-shaped sets satisfy (C)</td><td>13.7.1, 13.7.2</td></tr>
'''
def idxlink(m):
    return re.sub(r'\d+\.\d+\.\d+', lambda n: link_num(n.group(0), n.group(0)), m.group(0))
IDX = re.sub(r'<td>[\d., ]+</td></tr>', idxlink, IDX)
rep('''<tr><td><span class="tag r">Derived</span></td><td>Rouché's theorem</td><td><a class="ir" href="#it-11-10-1">11.10.1</a></td></tr>
''', '''<tr><td><span class="tag r">Derived</span></td><td>Rouché's theorem</td><td><a class="ir" href="#it-11-10-1">11.10.1</a></td></tr>
''' + IDX)

# ---- 7. front matter ----
rep('<div class="eyebrow">A textbook companion · Lectures 1–11</div>', '<div class="eyebrow">A textbook companion · Lectures 1–13</div>')
i = G.index('<p class="lede">'); j = G.index('</p>', i) + 4
G = G[:i] + '<p class="lede">A textbook built from the slides of a thirteen-lecture course in complex analysis. Part I asks whether a harmonic function is determined by, and can be found from, its boundary values, and answers with finite elements. Part II develops Cauchy\'s integral theory. Part III uses it to compute integrals and Fourier transforms and to prove the sampling theorem. Part IV studies entire functions through their zeros, ending with the Gamma function. Part V studies conformal maps and closes the circle: the solution of Part I\'s Dirichlet problem produces the Riemann map.</p>' + G[j:]
rep('<p>The course was taught as a sequence of self-contained lectures. Read as a book, it falls into four parts.</p>',
    '<p>The course was taught as a sequence of self-contained lectures. Read as a book, it falls into five parts.</p>')
m = re.search(r'(<tr><td><a href="#P4">IV</a> · Lectures 9–11</td>.*?</tr>)', G, re.S)
G = G.replace(m.group(1), m.group(1) + '\n<tr><td><a href="#P5">V</a> · Lectures 12–13</td><td>Which regions can be mapped onto the disk by a holomorphic bijection, and what is such a map good for?</td><td>It transports harmonic functions, so Dirichlet problems move to the disk. The disk\'s self-maps are known exactly (<a class="ir" href="#it-12-15-1">Theorem 12.15.1</a>), and regions made of squares have a Riemann map, built from Part I\'s solution of the Dirichlet problem (<a class="ir" href="#it-13-2-1">Theorem 13.2.1</a>).</td></tr>', 1)
rep('<li><em>Counting zeros.</em>', '<li><em>The circle closes.</em> Part I solved the Dirichlet problem on unions of squares (<a class="ir" href="#it-5-1-1">Theorem 5.1.1</a>). Part V uses that solution, with boundary values $\\log|z-z_0|$, to build the conformal map onto the disk (<a class="ir" href="#it-13-2-1">Theorem 13.2.1</a>); conversely, a conformal map moves Dirichlet problems to the disk (<a class="ir" href="#it-12-3-2">Cor. 12.3.2</a>). The harmonic conjugate of <a class="ir" href="#it-12-2-1">Lemma 12.2.1</a> is Lecture 1\'s stream function.</li>\n<li><em>Counting zeros.</em>')

open('guide.html', 'w').write(G)
print('missing refs:', missing)
ids = set(re.findall(r'id="([\w-]+)"', G)); hrefs = set(re.findall(r'href="#([\w-]+)"', G))
print('dangling:', sorted(hrefs - ids))
print('cites:', {k: len(v) for k, v in cites.items()})
