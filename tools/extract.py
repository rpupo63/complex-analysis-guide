#!/usr/bin/env python3
"""One-time migration: reference/guide.v17.html -> source tree.

    python tools/extract.py [--force]

Writes content/, exercises/, appendix/, notation.yaml, figures/, theme/.
Refuses to run if content/ already has lecture files, unless --force:
the source tree is now the source of truth, and re-extracting would discard edits.
"""
import json
import re
import shutil
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from build import KINDS, LETTER_STATUS, PROBLEM_GROUPS, EXERCISE_HEADING, quote_attr, write_doc  # noqa: E402

G = (ROOT / 'reference/guide.v17.html').read_text()
WORD_KIND = {v[0]: k for k, v in KINDS.items()}
WORD_KIND.update({'Standing setting': 'setting', 'Standing assumption': 'assumption', 'Grid hypothesis': 'hypothesis'})
problems = []


def fail(msg):
    raise SystemExit('extract: ' + msg)


def close(s, i, tag='div'):
    """Index just past the tag that opens at s[i], matching nested tags of the same name."""
    d = 0
    for m in re.compile(r'<%s\b|</%s>' % (tag, tag)).finditer(s, i):
        d += -1 if m.group(0).startswith('</') else 1
        if d == 0:
            return m.end()
    fail('unbalanced <%s> at %d' % (tag, i))


def slug(s, words=6):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'\\class\{[^}]*\}', ' ', s)
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace("'", '').replace('’', '')
    parts = re.findall(r'[a-z0-9]+', s.lower())
    return '-'.join(parts[:words]) or 'x'


# ------------------------------------------------------------------ pass 1: items and labels
ITEM_OPEN = re.compile(r'<div class="env (\w+)" id="(it-[\d-]+)" data-label="([^"]*)">')
HD = re.compile(r'(<span class="tag (\w)">([^<]*)</span>)?<span class="hd">([A-Z][A-Za-z ]*?) (\d+\.\d+\.\d+)'
                r'( <span class="nm">(.*?)</span>)?\.</span>', re.S)
items = {}           # id -> dict
labels_used = set()


def make_label(prefix, base, lecture):
    lab = '%s:%s' % (prefix, base)
    if lab in labels_used:
        lab = '%s:%s-l%s' % (prefix, base, lecture)
    n = 2
    while lab in labels_used:
        lab = '%s:%s-l%s-%d' % (prefix, base, lecture, n)
        n += 1
    labels_used.add(lab)
    return lab


for m in ITEM_OPEN.finditer(G):
    cls, iid, dl = m.groups()
    end = close(G, m.start())
    inner = G[m.end():end - 6]
    h = HD.match(inner)
    if not h:
        fail('item header not understood: ' + iid)
    word, num, name = h.group(4), h.group(5), h.group(7)
    if name is not None:
        if not (name.startswith('(') and name.endswith(')')):
            fail('name without parentheses: ' + iid)
        name = name[1:-1]
    kind = WORD_KIND[word]
    body = inner[h.end():]
    if cls == 'thm':
        if not body.lstrip(' ').startswith('<span class="body">') or not body.endswith('</span>'):
            fail('thm without body span: ' + iid)
        lead = body[:body.index('<span class="body">')]
        if lead not in (' ', ''):
            fail('odd text before body span: ' + iid)
        body = lead + '\x00' + body[body.index('<span class="body">') + len('<span class="body">'):-len('</span>')]
    status = LETTER_STATUS.get(h.group(2)) if h.group(2) else None
    if h.group(2) == 'p':
        status = h.group(3).lower()
    prefix = KINDS[kind][4]
    nm_plain = name
    if kind == 'exercise' and name and re.search(r'; (Homework|Practice midterm)', name):
        nm_plain = name.split('; ')[0]
    text = re.sub(r'<[^>]+>', ' ', body)
    base = slug(nm_plain) if nm_plain else slug(re.sub(r'\$[^$]*\$|\\\[.*?\\\]', ' ', text, flags=re.S), 5)
    items[iid] = dict(id=iid, cls=cls, dl=dl, word=word, number=num, name=name, kind=kind, status=status,
                      tagtext=h.group(3), body=body, start=m.start(), end=end,
                      label=make_label(prefix, base, num.split('.')[0]))

# ------------------------------------------------------------------ sections
SEC_RE = re.compile(r'<section id="(\w+)">\n<header><span class="eyebrow">L(\d+) · (Slides? [^<]*)</span>'
                    r'<h2>(\d+)\.(\d+) (.*?)</h2></header>\n')
sections = {}
for m in SEC_RE.finditer(G):
    sid, L, slide, l2, k, title = m.groups()
    if L != l2:
        fail('lecture mismatch in ' + sid)
    end = G.index('</section>', m.end())
    sections[sid] = dict(id=sid, L=int(L), k=int(k), slide=slide, title=title, start=m.start(),
                         body_start=m.end(), end=end, number='%s.%s' % (L, k))
APX_IDS = set(re.findall(r'<div class="apx" id="([A-E]\d+)">', G))

# toc titles
toc = dict(re.findall(r'<li><span class="n">[^<]*</span><a href="#(\w+)">(.*?)</a></li>', G))


# ------------------------------------------------------------------ fragment conversion
def default_ref(it):
    return KINDS[it['kind']][3] + ' ' + it['number']


def labelish_next(s, j):
    return j < len(s) and re.match(r'[A-Za-z0-9-]', s[j]) is not None


def delink(s, where):
    """Turn generated links back into source shorthands."""
    out, pos = [], 0
    pat = re.compile(r'<a class="ir" href="#([\w-]+)">(.*?)</a>|'
                     r'<a class="x" id="r-\w+-\d+" href="#(\w+)" data-from="[^"]*">(.*?)</a>', re.S)
    for m in pat.finditer(s):
        out.append(s[pos:m.start()])
        pos = m.end()
        nxt = labelish_next(s, m.end())
        if m.group(1):
            target, text = m.group(1), m.group(2)
            if '#' in text or '[' in text or ']' in text:
                fail('%s: link text needs escaping: %r' % (where, text))
            if target in items:
                it = items[target]
                lab, num, dflt = it['label'], it['number'], default_ref(it)
            elif target in sections:
                sec = sections[target]
                lab, num, dflt = 'sec:' + target, sec['number'], '§' + sec['number']
            elif target in APX_IDS:
                lab, num, dflt = 'apx:' + target, target[0] + '.' + target[1:], 'Appendix ' + target[0] + '.' + target[1:]
            else:
                fail('%s: ir link to unknown target %s' % (where, target))
            if text == dflt and not nxt:
                out.append('@' + lab)
            else:
                t = text.replace(num, '#', 1) if num in text else text
                out.append('[%s](@%s)' % (t, lab))
        else:
            tid, text = m.group(3), m.group(4)
            lab = tid[0] + '.' + tid[1:]
            chip = '<span class="xl">%s</span>' % lab
            if text.endswith(chip):
                text = text[:-len(chip)]
                if re.sub('<.*?>', '', text).strip() == lab:
                    fail('%s: chip on a link whose text is its label' % where)
            elif re.sub('<.*?>', '', text).strip() != lab:
                fail('%s: appendix link without chip: %r' % (where, text))
            if '[' in text or ']' in text:
                if not re.fullmatch(r'(?:[^\[\]]|\[[^\[\]]*\])*', text):
                    fail('%s: unbalanced brackets in appendix link text %r' % (where, text))
            out.append('[%s](apx:%s)' % (text, tid))
    out.append(s[pos:])
    s = ''.join(out)
    if '<a class="ir"' in s or '<a class="x"' in s:
        fail('%s: unconverted link remains' % where)
    return s


def unlinked_numbers(s, where):
    """Hard-coded item numbers in prose (outside TeX and tags) -> [#](=label)."""
    by_num = {it['number']: it for it in items.values()}
    parts = re.split(r'(<[^>]+>|\$[^$]*\$|\\\[.*?\\\]|\[[^\]]*\]\((?:@|=|apx:)[^)]*\))', s, flags=re.S)
    for i in range(0, len(parts), 2):
        def f(m):
            it = by_num.get(m.group(0))
            if not it:
                problems.append('%s: number %s is not an item; left as text' % (where, m.group(0)))
                return m.group(0)
            return '[#](=%s)' % it['label']
        parts[i] = re.sub(r'(?<![\d.])\d+\.\d+\.\d+(?![\d.]?\d)', f, parts[i])
    return ''.join(parts)


fig_count = {}


def figures(s, where):
    def f(m):
        n = fig_count[where] = fig_count.get(where, 0) + 1
        name = '%s-%d' % (where, n)
        (ROOT / 'figures' / (name + '.svg')).write_text(m.group(0))
        return '{{fig:%s}}' % name
    return re.sub(r'<svg\b.*?</svg>', f, s, flags=re.S)


def attrs_str(d):
    parts = []
    for k, v in d.items():
        if k == 'label':
            parts.insert(0, '#' + v)
        elif v is True:
            parts.append(k)
        else:
            parts.append('%s=%s' % (k, quote_attr(v)))
    return ' '.join(parts)


def item_attrs(it):
    kind = it['kind']
    word, cls, short, refw, prefix = KINDS[kind]
    a = {'label': it['label']}
    if it['word'] != word:
        a['kind'] = it['word']
    if it['name'] is not None:
        a['name'] = it['name']
    status = it['status']
    if kind == 'example':
        dcls = 'thm' if (status or 'defined') == 'derived' else 'def'
        if status != 'defined':
            a['status'] = status
    else:
        dcls = cls
        from build import DEFAULT_STATUS
        if status != DEFAULT_STATUS[cls if it['cls'] == cls else it['cls']]:
            a['status'] = status or 'none'
    if it['cls'] != dcls:
        a['class'] = it['cls']
        from build import DEFAULT_STATUS
        if status == DEFAULT_STATUS[it['cls']]:
            a.pop('status', None)
    if it['dl'] != short + ' ' + it['number']:
        a['short'] = it['dl'][:-len(it['number']) - 1]
    if it['status'] and it['tagtext'] != {'defined': 'Defined', 'derived': 'Derived', 'assumed': 'Assumed',
                                          'cited': 'Cited', 'context': 'Context', 'preview': 'Preview'}[status]:
        fail('odd tag text in ' + it['id'])
    return a


def directives(s, base, where):
    """Replace numbered items and proofs in s (which starts at G[base]) by ::: directives."""
    out, pos = [], 0
    pat = re.compile(r'<div class="env \w+" id="(it-[\d-]+)"|<div class="proof">')
    i = 0
    while True:
        m = pat.search(s, i)
        if not m:
            break
        end = close(s, m.start())
        if (m.start() > 0 and s[m.start() - 1] != '\n') or (end < len(s) and s[end] != '\n'):
            fail('%s: block at %d is not on its own line: %r' % (where, base + m.start(), s[max(0, m.start() - 40):m.start() + 60]))
        out.append(s[pos:m.start()])
        if m.group(1):
            it = items[m.group(1)]
            inner = it['body']
            a = item_attrs(it)
            if '\x00' in inner:  # thm: the separator sits outside the body span
                lead, inner = inner.split('\x00', 1)
                if lead == '':
                    a['tight'] = True
            elif not inner.startswith(' ') and not inner.startswith('\n'):
                a['tight'] = True
            elif inner.startswith(' '):
                inner = inner[1:]
            if re.search(r'<div class="env \w+" id=|<div class="proof">', inner):
                fail('nested block in ' + it['id'])
            out.append('::: %s {%s}\n%s\n:::' % (it['kind'], attrs_str(a), inner))
        else:
            blk = s[m.start():end]
            h = re.match(r'<div class="proof"><span class="hd">(.*?)</span>', blk, re.S)
            if not h:
                fail('%s: proof without header' % where)
            inner = blk[h.end():-6]
            a = {}
            if h.group(1) != 'Proof.':
                a['title'] = h.group(1)
            if inner.startswith(' '):
                inner = inner[1:]
            elif not inner.startswith('\n'):
                a['tight'] = True
            if inner.endswith(' <span class="qed">∎</span>') and inner.count('class="qed"') == 1:
                inner = inner[:-len(' <span class="qed">∎</span>')]
            elif 'class="qed"' not in inner:
                a['noqed'] = True
            if '<div class="proof">' in inner:
                fail('nested proof')
            out.append('::: proof%s\n%s\n:::' % (' {%s}' % attrs_str(a) if a else '', inner))
        pos = i = end
    out.append(s[pos:])
    return ''.join(out)


def convert(s, base, where, figs=None):
    if figs:
        s = figures(s, figs)
    s = directives(s, base, where)
    s = delink(s, where)
    return unlinked_numbers(s, where)


# ------------------------------------------------------------------ write everything
def main():
    if (ROOT / 'content/L01').exists() and '--force' not in sys.argv:
        fail('content/ already exists; the source tree is the source of truth now. Use --force to overwrite.')
    for d in ('content', 'exercises', 'appendix', 'figures', 'theme'):
        if (ROOT / d).exists():
            for p in (ROOT / d).iterdir():
                if p.is_dir():
                    shutil.rmtree(p)
                elif p.suffix != '.py':
                    p.unlink()
        (ROOT / d).mkdir(exist_ok=True)

    # ---- theme
    css = G[G.index('<style>\n') + 8:G.index('</style>')]
    (ROOT / 'theme/style.css').write_text(css)
    i = G.index('<script>\nwindow.MathJax') + 9
    (ROOT / 'theme/mathjax-config.js').write_text(G[i:G.index('</script>', i)])
    js_start = G.index('<script>\n(function(){') + 9
    js = G[js_start:G.index('</script>', js_start)]
    nj = js.index('var NOTE = ') + 11
    nk = js.index(';\n', nj)
    note = json.loads(js[nj:nk])
    (ROOT / 'theme/guide.js').write_text(js[:nj] + '__NOTE__' + js[nk:])
    head = G[:G.index('<style>\n') + 8]
    mid = G[G.index('</style>'):G.index('<script>\nwindow.MathJax') + 9]
    mid2 = G[G.index('</script>', G.index('<script>\nwindow.MathJax')):G.index('<div class="wrap">\n') + 19]
    tail = G[G.index('</div>\n\n<div id="tip"'):js_start]
    end = G[G.index('</script>', js_start):]
    (ROOT / 'theme/page.html').write_text(head + '{{STYLE}}' + mid + '{{MATHJAX_CONFIG}}' + mid2 + '{{BODY}}\n'
                                          + tail + '{{GUIDE_JS}}' + end)

    # ---- front matter
    fs = G.index('<div class="wrap">\n') + 19
    fe = G.index('<div class="unit" id="P1">')
    front = G[fs:fe]
    r0 = front.index('<tbody>\n', front.index('<table class="roadmap">')) + 8
    r1 = front.index('\n</tbody>', r0)
    roadmap = front[r0:r1]
    p0 = front.index('<div class="tbl"><table>', front.index('id="problems"'))
    p1 = front.index('</table></div>\n', p0) + 15
    t0 = front.index('<p class="toc-unit"><a href="#P1">')
    t1 = front.index('<p class="toc-unit">Reference</p>')
    front = front[:r0] + '{{roadmap-rows}}' + front[r1:p0] + '{{problems-table}}' + front[p1:t0] + '{{toc}}' + front[t1:]
    (ROOT / 'content/front.md').write_text(convert(front, fs, 'front'))

    # ---- parts and lectures
    rows = re.findall(r'<tr><td><a href="#(P\d)">(\w+)</a> · Lectures? [\d–]+</td><td>(.*?)</td><td>(.*?)</td></tr>', roadmap)
    if len(rows) != roadmap.count('<tr>'):
        fail('roadmap rows')
    parts = []
    for pid, numeral, q, ans in rows:
        m = re.search(r'<div class="unit" id="%s">\n  <span class="eyebrow">Part %s</span>\n  <h2>(.*?)</h2>\n  (.*?)\n</div>' % (pid, numeral), G, re.S)
        lecs = []
        parts.append(dict(id=pid, numeral=numeral, title=m.group(1), lectures=lecs,
                          intro=convert(m.group(2), m.start(2), pid),
                          question=convert(q, 0, pid + ' roadmap'), answer=convert(ans, 0, pid + ' roadmap')))
    lec_re = re.compile(r'<div class="lecture" id="L(\d+)">\n  <span class="eyebrow">Part (\w+) · (.*?)</span>\n  <h2>Lecture \d+ · (.*?)</h2>\n  '
                        r'<div class="ov"><div class="ov-row"><span class="ov-k">Goal</span><div>(.*?)</div></div>'
                        r'<div class="ov-row"><span class="ov-k">Main results</span><div>(.*?)</div></div>'
                        r'<div class="ov-row"><span class="ov-k">Uses</span><div>(.*?)</div></div>'
                        r'<div class="ov-row"><span class="ov-k">Used later</span><div>(.*?)</div></div></div>(.*?)</div>\n', re.S)
    ex_files = []
    for m in lec_re.finditer(G):
        L = int(m.group(1))
        part = next(p for p in parts if p['numeral'] == m.group(2))
        if part['title'] != m.group(3):
            fail('lecture eyebrow L%d' % L)
        part['lectures'].append(L)
        w = 'L%d' % L
        meta = dict(title=m.group(4))
        lt = re.search(r'<p class="toc-part"><a href="#L%d">Lecture %d · (.*?)</a></p>' % (L, L), G).group(1)
        if lt != m.group(4):
            meta['toc'] = lt
        meta.update(goal=convert(m.group(5), 0, w), main_results=convert(m.group(6), 0, w),
                    uses=convert(m.group(7), 0, w), used_later=convert(m.group(8), 0, w))
        meta = dict(meta)
        write_doc(ROOT / ('content/L%02d/lecture.md' % L), meta, convert(m.group(9), m.start(9), w))
        secs = sorted((s for s in sections.values() if s['L'] == L), key=lambda s: s['start'])
        for n, s in enumerate(secs, 1):
            if s['k'] != n:
                fail('section numbering in L%d' % L)
            body = G[s['body_start']:s['end']]
            body, exs = split_exercises(body, s)
            sm = dict(id=s['id'], slide=s['slide'], title=s['title'])
            if toc.get(s['id']) != s['title']:
                sm['toc'] = toc[s['id']]
            write_doc(ROOT / ('content/L%02d/%02d-%s.md' % (L, n, slug(toc[s['id']], 5))), sm,
                      convert(body, s['body_start'], s['id'], figs=s['id']))
            ex_files += exs
    for path, meta, body in ex_files:
        write_doc(path, meta, body)
    (ROOT / 'content/parts.yaml').write_text(dump(parts))

    # ---- index
    s = G.index('<section id="index">')
    X = G[s:G.index('</section>', s)]
    intro = re.search(r'</header>\n(.*?)\n<div class="tbl">', X, re.S).group(1)
    groups = []
    for m in re.finditer(r'<tr><td colspan="3" class="idx-part">(.*?)</td></tr>|<tr><td><span class="tag (\w)">[^<]*</span></td><td>(.*?)</td><td>(.*?)</td></tr>', X):
        if m.group(1):
            groups.append(dict(title=m.group(1), rows=[]))
        else:
            labs = [items[i]['label'] for i in re.findall(r'href="#(it-[\d-]+)"', m.group(4))]
            groups[-1]['rows'].append([LETTER_STATUS[m.group(2)], convert(m.group(3), 0, 'index'), labs])
    (ROOT / 'content/index.yaml').write_text(
        '# Index of the main text. Each row: [status, description (HTML+TeX), [item labels]].\n'
        + dump(dict(intro=convert(intro, 0, 'index'), groups=groups), flow_rows=True))

    # ---- notation
    s = G.index('<section id="notation">')
    nintro = re.search(r'</header>\n(.*?)\n<div class="tbl">', G[s:], re.S).group(1)
    ents = {}
    pos = {m.group(1): m.start() for m in re.finditer(r'<div class="(?:env \w+|apx)" id="([\w-]+)"', G)}
    order = sorted(note.items(), key=lambda kv: pos.get(kv[1]['t'], 10**9))
    for key, v in order:
        target = items[v['t']]['label'] if v['t'] in items else 'apx:' + v['t']
        ents[key] = dict(h=unlinked_numbers(v['h'], 'notation'), d=unlinked_numbers(v['d'], 'notation'), target=target)
    (ROOT / 'notation.yaml').write_text(
        '# Notation entries, in order of first definition. KEY is used in TeX as \\class{ntn-KEY}{...}.\n'
        '# h: symbol as HTML; d: meaning; target: label of the defining item (or apx:ID).\n'
        + dump(dict(intro=convert(nintro, 0, 'notation'), entries=ents)))

    # ---- appendix
    aparts = {}
    for m in re.finditer(r'<section id="apx(\w)" class="part">\n<header><span class="eyebrow">Appendix \w</span><h2>(.*?)</h2></header>\n', G):
        intro = G[m.end():G.index('<div class="apx"', m.end())]
        if not intro.endswith('\n'):
            fail('appendix part intro')
        intro = intro[:-1].rstrip('\n') if intro != '\n' else ''
        aparts[m.group(1)] = dict(title=m.group(2), intro=convert(intro, m.end(), 'apx' + m.group(1)))
    (ROOT / 'appendix/parts.yaml').write_text(dump(aparts))
    for m in re.finditer(r'<div class="apx" id="(\w+)">\n<div class="apx-hd"><span class="apx-n">[\w.]+</span><h3>(.*?)</h3>((?:<span class="tag \w">[^<]*</span>)*)</div>\n', G):
        aid = m.group(1)
        end = close(G, m.start())
        body = G[m.end():end - 6]
        body = re.sub(r'^<p class="usedin">.*?</p>\n', '', body)
        st = []
        for letter, word in re.findall(r'<span class="tag (\w)">([^<]*)</span>', m.group(3)):
            st.append({'d': 'defined', 'r': 'derived', 'a': 'assumed', 'c': 'cited'}.get(letter) or word.lower())
        write_doc(ROOT / ('appendix/%s-%s.md' % (aid, slug(m.group(2), 4))),
                  dict(id=aid, title=convert(m.group(2), 0, aid), status=st),
                  convert(body, m.end(), aid, figs=aid))

    for p in problems:
        print('note:', p)
    print('items %d, sections %d, exercises %d, figures %d' % (len(items), len(sections), len(ex_files),
                                                             len(list((ROOT / 'figures').glob('*.svg')))))


def split_exercises(body, s):
    """Cut homework/midterm exercises off the tail of a section body."""
    found = []
    for m in re.finditer(r'<div class="env ex" id="(it-[\d-]+)"', body):
        it = items[m.group(1)]
        if it['name'] and re.search(r'; (Homework|Practice midterm)', it['name']):
            found.append((m.start(), close(body, m.start()), it))
    if not found:
        return body, []
    cut = found[0][0]
    tail = body[cut:]
    expect = ''.join(body[a:b] + '\n' for a, b, _ in found)
    if tail != expect:
        fail('%s: homework exercises are not a clean tail' % s['id'])
    head = body[:cut]
    if head.endswith(EXERCISE_HEADING):
        head = head[:-len(EXERCISE_HEADING)]
        if 'class="env ex"' in head:
            fail('%s: heading with other exercises' % s['id'])
    elif 'class="env ex"' not in head:
        fail('%s: homework exercises without heading' % s['id'])
    out = []
    for order, (a, b, it) in enumerate(found, 1):
        title, source = it['name'].split('; ', 1)
        g = next(i for i, x in enumerate(PROBLEM_GROUPS) if source.startswith(x))
        code = ['hw1', 'hw2', 'pm1', 'pm2', 'pm3'][g]
        pm = re.search(r'Problem (\d+)(\([a-z]\))?', source)
        prob = ('p%s%s' % (pm.group(1), (pm.group(2) or '').strip('()'))) if pm else slug(source[len(PROBLEM_GROUPS[g]):], 3)
        inner = it['body']
        if not inner.startswith(' '):
            fail('exercise spacing ' + it['id'])
        meta = dict(label=it['label'], source=source, title=title, placement=s['id'], order=order)
        out.append((ROOT / 'exercises' / ('%s-%s.md' % (code, prob)), meta,
                    convert(inner[1:], 0, it['id']) + '\n'))
    return head, out


def dump(obj, flow_rows=False):
    import yaml
    text = yaml.safe_dump(obj, allow_unicode=True, sort_keys=False, width=10**6)
    return text


if __name__ == '__main__':
    main()
