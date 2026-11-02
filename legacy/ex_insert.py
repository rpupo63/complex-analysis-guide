import re, html
from exercises import EX
G = open('guide.html').read()

item_ids = set(re.findall(r'id="(it-[\d-]+)"', G))
APX = set(re.findall(r'<div class="apx" id="([A-E]\d+)"', G))
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
def link_refs(text):
    def f(m):
        kw, sp, nums = m.groups(); out, first = [], True
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
def link_chunk(chunk):
    parts = re.split(r'(<[^>]+>)', chunk); out = []; after_hd = False; in_a = 0; in_pre = 0
    for p in parts:
        if p.startswith('<'):
            after_hd = p == '<span class="hd">'
            if p.startswith('<a '): in_a += 1
            elif p == '</a>': in_a -= 1
            elif p.startswith('<pre'): in_pre += 1
            elif p == '</pre>': in_pre -= 1
            elif p.startswith('<code'): in_pre += 1
            elif p == '</code>': in_pre -= 1
            out.append(p); continue
        if not p: continue
        segs = re.split(r'(\$[^$]*\$|\\\[.*?\\\])', p, flags=re.S)
        res = []
        for i, seg in enumerate(segs):
            res.append(seg if (i % 2 or after_hd or in_a or in_pre) else link_refs(seg))
        out.append(''.join(res)); after_hd = False
    return ''.join(out)

counts = {}
for m in re.finditer(r'id="r-([A-E]\d+)-(\d+)"', G):
    counts[m.group(1)] = max(counts.get(m.group(1), 0), int(m.group(2)))
def lab(t): return t[0] + '.' + t[1:]
cites = {}
def appendix_links(chunk, where):
    def sub(m):
        tid, text = m.group(1), m.group(2)
        counts[tid] = counts.get(tid, 0) + 1
        rid = f'r-{tid}-{counts[tid]}'
        cites.setdefault(tid, []).append((rid, where))
        chip = '' if re.sub('<.*?>', '', text).strip() == lab(tid) else f'<span class="xl">{lab(tid)}</span>'
        return f'<a class="x" id="{rid}" href="#{tid}" data-from="{html.escape(where)}">{text}{chip}</a>'
    return re.sub(r'<a class="x" href="#(\w+)">(.*?)</a>', sub, chunk, flags=re.S)

by_sec = {}
for e in EX: by_sec.setdefault(e['sec'], []).append(e)
index_rows = []
# pre-pass: reserve all new exercise ids so exercises can cite each other
for sid, lst in by_sec.items():
    i = G.index(f'<section id="{sid}">'); j = G.index('</section>', i); b = G[i:j]
    L, s = map(int, re.search(r'<h2>(\d+)\.(\d+) ', b).groups())
    k0 = max([int(k) for k in re.findall(r'id="it-%d-%d-(\d+)"' % (L, s), b)], default=0)
    for t in range(len(lst)): item_ids.add(f'it-{L}-{s}-{k0+t+1}')
for sid, lst in by_sec.items():
    i = G.index(f'<section id="{sid}">')
    j = G.index('</section>', i)
    secblock = G[i:j]
    eyebrow = re.search(r'<span class="eyebrow">(.*?)</span>', secblock).group(1)
    L, s = map(int, re.search(r'<h2>(\d+)\.(\d+) ', secblock).groups())
    nums = [int(k) for k in re.findall(r'id="it-%d-%d-(\d+)"' % (L, s), secblock)]
    k = max(nums, default=0)
    has_ex = 'class="env ex"' in secblock
    chunk = '' if has_ex else '\n<h3>Exercises</h3>\n<p class="ext">From the homework and the practice midterms. Each has a hint and a full solution; open them only after trying.</p>\n'
    for e in lst:
        k += 1
        num = f'{L}.{s}.{k}'
        iid = 'it-' + num.replace('.', '-')
        label = f'Exercise {num}'
        body = (f'<div class="env ex" id="{iid}" data-label="{label}"><span class="hd">{label} <span class="nm">({e["title"]}; {e["src"]})</span>.</span> '
                f'{e["statement"]}\n<details class="sol"><summary>Hint</summary>\n{e["hint"]}\n</details>\n'
                f'<details class="sol"><summary>Solution</summary>\n{e["solution"]}\n</details></div>\n')
        body = link_chunk(body)
        body = appendix_links(body, f'{eyebrow} · {label}')
        chunk += body
        index_rows.append((e['src'], iid, label, L, s, e['title']))
    G = G[:j] + chunk + G[j:]

# cited-in rows
for tid, lst in cites.items():
    seen = set(); links = ''
    for rid, where in lst:
        if where in seen: continue
        seen.add(where); links += f'<a class="bk" href="#{rid}" data-from="Appendix {lab(tid)}">{html.escape(where)}</a>'
    i = G.index(f'<div class="apx" id="{tid}">')
    k = G.find('<p class="usedin">', i); nxt = G.find('<div class="apx"', i + 10)
    if k != -1 and (nxt == -1 or k < nxt):
        e = G.index('</p>', k); G = G[:e] + links + G[e:]
    else:
        j = G.index('</div>', G.index('<div class="apx-hd">', i)) + len('</div>')
        G = G[:j] + '\n<p class="usedin"><span>Cited in</span>' + links + '</p>' + G[j:]

# problem-set index in the front matter
def key(src):
    order = ['Homework 1', 'Homework 2', 'Practice midterm 1', 'Practice midterm 2', 'Practice midterm 3']
    for i, o in enumerate(order):
        if src.startswith(o): return i
    return 9
rows = []
for src, iid, label, L, s, title in index_rows:
    for part in src.split('; '):
        rows.append((key(part), part, iid, label, L, title))
def pnum(p):
    m = re.search(r'Problem (\d+)(?:\(([a-z])\))?', p)
    return (int(m.group(1)), m.group(2) or '') if m else (99, '')
rows.sort(key=lambda r: (r[0], pnum(r[1])))
tbl = '<div class="tbl"><table>\n<thead><tr><th>Problem</th><th>Topic</th><th>Exercise</th><th>Lecture</th></tr></thead><tbody>\n'
last = None
for kk, part, iid, label, L, title in rows:
    grp = ['Homework 1', 'Homework 2', 'Practice midterm 1', 'Practice midterm 2', 'Practice midterm 3'][kk]
    if grp != last:
        tbl += f'<tr><td colspan="4" class="idx-part">{grp}</td></tr>\n'; last = grp
    short = part[len(grp):].lstrip(', ') or part
    tbl += f'<tr><td>{short}</td><td>{title}</td><td><a class="ir" href="#{iid}">{label}</a></td><td>{L}</td></tr>\n'
tbl += '</tbody></table></div>\n'
block = ('\n<h3 id="problems">Homework and practice midterms</h3>\n'
         '<p>Every problem from the two homework sets and the three practice midterms appears as an exercise, placed in the section that supplies the last tool it needs. Each has a hidden hint (the official hint where the sheet gives one) and a full solution. The practice midterms share a pattern: Problem 1 is a trigonometric integral by residues (Lecture 8), Problem 2 is growth bounds and the identity theorem (Lectures 6 and 10), Problem 3 is Rouché (Lecture 11), and Problem 4 is conformal maps and the Schwarz lemma (Lecture 12).</p>\n'
         + tbl + '\n<h3>Contents</h3>')
assert G.count('\n<h3>Contents</h3>') == 1
G = G.replace('\n<h3>Contents</h3>', block)
G = G.replace('  <li><span class="n">Roadmap</span><a href="#roadmap">How the course fits together</a></li>',
              '  <li><span class="n">Roadmap</span><a href="#roadmap">How the course fits together</a></li>\n  <li><span class="n">Problems</span><a href="#problems">Homework and practice midterms</a></li>')
open('guide.html', 'w').write(G)
print('missing:', missing)
ids = set(re.findall(r'id="([\w-]+)"', G)); hrefs = set(re.findall(r'href="#([\w-]+)"', G))
print('dangling:', sorted(hrefs - ids)); print('exercises:', len(index_rows), 'rows', len(rows))
