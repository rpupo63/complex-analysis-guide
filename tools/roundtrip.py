#!/usr/bin/env python3
"""Compare build/guide.html with reference/guide.v17.html (the migration acceptance gate).

    python tools/roundtrip.py [built.html] [reference.html]

Checks: baseline counts, element id set, href target set, appendix citations
(data-from per target, "Cited in" rows as sets), normalised text of every
section / .apx / .lecture, and a whole-page markup comparison after
normalising generated r- numbering, comments and whitespace.
Exit status 1 on any difference.
"""
import collections
import difflib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW = Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / 'build/guide.html').read_text()
OLD = Path(sys.argv[2] if len(sys.argv) > 2 else ROOT / 'reference/guide.v17.html').read_text()
fails = []


def counts(g):
    return {
        'section': len(re.findall(r'<section\b', g)),
        'lectures': len(re.findall(r'<div class="lecture" id="L\d+"', g)),
        'parts': len(re.findall(r'<div class="unit" id="P\d+"', g)),
        'numbered items': len(re.findall(r'id="it-\d+-\d+-\d+"', g)),
        'div.env': len(re.findall(r'<div class="env\b', g)),
        'proofs': len(re.findall(r'<div class="proof"', g)),
        'exercises': len(re.findall(r'<div class="env ex"', g)),
        'appendix entries': len(re.findall(r'<div class="apx" id=', g)),
        'appendix citations': len(re.findall(r'id="r-[A-E]\d+-\d+"', g)),
        'a.ir': len(re.findall(r'<a class="ir"', g)),
        'figures': len(re.findall(r'<figure\b', g)),
        'NOTE entries': len(re.findall(r'"tl": ', g)),
        '\\class{ntn-}': len(re.findall(r'\\class\{ntn-', g)),
    }


def check(name, ok, detail=''):
    print('%-4s %s%s' % ('ok' if ok else 'FAIL', name, (': ' + detail) if detail and not ok else ''))
    if not ok:
        fails.append(name)


# Intentional differences, normalised away before comparing (see README "Migration report").
# 1. Appendix links in a lecture's overview box: the reference's data-from carried over the
#    previous section's context (e.g. "L3 · Slide 21 · Rem. 3.19.2" inside Lecture 4's overview);
#    the build says "L4 · Overview".
def overview_fix(g):
    rids = set()

    def lec(m):
        def a(x):
            rids.add(x.group(1))
            return '<a class="x" id="%s" href="#%s" data-from="OVERVIEW">' % (x.group(1), x.group(2))
        return re.sub(r'<a class="x" id="(r-\w+-\d+)" href="#(\w+)" data-from="[^"]*">', a, m.group(0))
    g = re.sub(r'<div class="lecture" id="L\d+">.*?<div class="ov">.*?</div></div></div>', lec, g, flags=re.S)
    g = re.sub(r'(<a class="bk" href="#(r-\w+-\d+)" data-from="[^"]*">)[^<]*(</a>)',
               lambda m: m.group(1) + 'OVERVIEW' + m.group(3) if m.group(2) in rids else m.group(0), g)
    return g, len(rids)


NEW, n_ov = overview_fix(NEW)
OLD, _ = overview_fix(OLD)
print('note: %d appendix links in lecture overviews get data-from "Lk · Overview" (intentional fix)' % n_ov)

# 1. counts
cn, co = counts(NEW), counts(OLD)
for k in co:
    check('count %-20s %6d' % (k, co[k]), cn[k] == co[k], 'built %d' % cn[k])

# 2. ids and hrefs
ids_n, ids_o = set(re.findall(r'\bid="([^"]+)"', NEW)), set(re.findall(r'\bid="([^"]+)"', OLD))
check('element id set identical', ids_n == ids_o,
      'only built: %s; only reference: %s' % (sorted(ids_n - ids_o)[:10], sorted(ids_o - ids_n)[:10]))
def hrefs(g):
    return set(re.findall(r'href="#([^"]+)"', re.sub(r'<script>.*?</script>', '', g, flags=re.S)))


hr_n, hr_o = hrefs(NEW), hrefs(OLD)
plain_n, plain_o = {h for h in hr_n if not h.startswith('r-')}, {h for h in hr_o if not h.startswith('r-')}
check('href target set identical (r- back-links aside)', plain_n == plain_o,
      'only built: %s; only reference: %s' % (sorted(plain_n - plain_o)[:10], sorted(plain_o - plain_n)[:10]))
per = lambda hs: collections.Counter(re.match(r'r-(\w+)-', h).group(1) for h in hs if h.startswith('r-'))
check('r- back-link targets per appendix entry (numbering may differ)', per(hr_n) == per(hr_o))
check('no dangling href', not (hr_n - ids_n), str(sorted(hr_n - ids_n)[:10]))


# 3. appendix citations
def cites(g):
    return collections.Counter(re.findall(r'<a class="x" id="r-\w+-\d+" href="#(\w+)" data-from="([^"]*)">', g))


def usedin(g):
    out = {}
    for m in re.finditer(r'<div class="apx" id="(\w+)">.*?(?:<p class="usedin">(.*?)</p>|(?=<div class="apx"))', g, re.S):
        out[m.group(1)] = set(re.findall(r'>([^<]*)</a>', m.group(2) or ''))
    return out


cn_, co_ = cites(NEW), cites(OLD)
check('appendix links: same (target, data-from) multiset', cn_ == co_,
      'only built: %s; only reference: %s' % (list((cn_ - co_).items())[:6], list((co_ - cn_).items())[:6]))
un, uo = usedin(NEW), usedin(OLD)
bad = [k for k in uo if un.get(k) != uo[k]]
check('"Cited in" rows: same set of places per entry', not bad, str(bad[:10]))


# 4. normalised text of blocks
def blocks(g):
    out = {}
    for m in re.finditer(r'<section id="([\w-]+)"[^>]*>(.*?)</section>', g, re.S):
        out['section#' + m.group(1)] = m.group(2)
    for m in re.finditer(r'<div class="(apx|lecture)" id="(\w+)">', g):
        d, i = 0, m.start()
        for t in re.finditer(r'<div\b|</div>', g[i:]):
            d += -1 if t.group(0) == '</div>' else 1
            if d == 0:
                out[m.group(1) + '#' + m.group(2)] = g[i:i + t.end()]
                break
    return out


def text(s):
    s = re.sub(r'<p class="usedin">.*?</p>', '', s, flags=re.S)
    s = re.sub(r'<!--.*?-->|<[^>]+>', ' ', s, flags=re.S)
    return re.sub(r'\s+', ' ', s).strip()


bn, bo = blocks(NEW), blocks(OLD)
check('same block set', set(bn) == set(bo), str(set(bn) ^ set(bo)))
tbad = [k for k in bo if k in bn and text(bn[k]) != text(bo[k])]
check('normalised text of every section / .apx / .lecture', not tbad, str(tbad[:10]))
for k in tbad[:3]:
    a, b = text(bo[k]), text(bn[k])
    i = next(i for i in range(min(len(a), len(b)) + 1) if i == min(len(a), len(b)) or a[i] != b[i])
    print('   %s\n     ref:   ...%s\n     built: ...%s' % (k, a[max(0, i - 80):i + 80], b[max(0, i - 80):i + 80]))


# 5. whole-page markup, modulo generated numbering, comments, whitespace and NOTE key order
def norm(g):
    g = re.sub(r'<!--.*?-->', '', g, flags=re.S)
    g = re.sub(r'var NOTE = \{.*?\};\n', 'var NOTE = {};\n', g, flags=re.S)
    seq = collections.defaultdict(int)
    ren = {}

    def r(m):
        seq[m.group(1)] += 1
        new = 'r-%s-%d' % (m.group(1), seq[m.group(1)])
        ren[m.group(0)[4:-1]] = new
        return 'id="%s"' % new
    g = re.sub(r'id="r-(\w+)-\d+"', r, g)
    g = re.sub(r'href="#(r-\w+-\d+)"', lambda m: 'href="#%s"' % ren.get(m.group(1), m.group(1)), g)

    def row(m):
        links = sorted(re.findall(r'<a class="bk".*?</a>', m.group(1)))
        return '<p class="usedin"><span>Cited in</span>' + ''.join(links) + '</p>'
    g = re.sub(r'<p class="usedin"><span>Cited in</span>(.*?)</p>', row, g)
    return re.sub(r'\s+', ' ', g).strip()


nn, no = norm(NEW), norm(OLD)
same = nn == no
check('whole page markup (normalised)', same)
if not same:
    lo, ln = no.replace('>', '>\n').split('\n'), nn.replace('>', '>\n').split('\n')
    diff = [d for d in difflib.unified_diff(lo, ln, 'reference', 'built', n=1, lineterm='')]
    print('   %d differing lines; first ones:' % sum(1 for d in diff if d[:1] in '+-'))
    for d in diff[2:40]:
        print('   ' + d[:200])

note_n = re.search(r'var NOTE = (\{.*?\});\n', NEW, re.S).group(1)
note_o = re.search(r'var NOTE = (\{.*?\});\n', OLD, re.S).group(1)
import json  # noqa: E402
check('NOTE entries identical (key order aside)', json.loads(note_n) == json.loads(note_o))

print('\nroundtrip: %s' % ('PASS' if not fails else 'FAIL (%d)' % len(fails)))
sys.exit(1 if fails else 0)
