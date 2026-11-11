#!/usr/bin/env python3
"""Build the Complex Analysis Companion from source.

    python build.py            # writes build/guide.html and build/items.json

Reads content/, exercises/, appendix/, notation.yaml, figures/ and theme/.
Never reads build/. See AGENTS.md for the source format.
"""
import html
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent

# ---------------------------------------------------------------- tables
# directive name -> (display word, env class, data-label word, default reference word, label prefix)
KINDS = {
    'theorem':     ('Theorem',     'thm', 'Thm.',    'Theorem',    'thm'),
    'proposition': ('Proposition', 'thm', 'Prop.',   'Prop.',      'prop'),
    'lemma':       ('Lemma',       'thm', 'Lemma',   'Lemma',      'lem'),
    'corollary':   ('Corollary',   'thm', 'Cor.',    'Cor.',       'cor'),
    'fact':        ('Fact',        'thm', 'Fact',    'Fact',       'fact'),
    'definition':  ('Definition',  'def', 'Def.',    'Def.',       'def'),
    'convention':  ('Convention',  'def', 'Conv.',   'Convention', 'conv'),
    'example':     ('Example',     None,  'Ex.',     'Example',    'eg'),
    'remark':      ('Remark',      'rem', 'Rem.',    'Remark',     'rem'),
    'exercise':    ('Exercise',    'ex',  'Exercise', 'Exercise',  'ex'),
    'hypothesis':  ('Hypothesis',  'asm', 'Hyp.',    'Hypothesis', 'hyp'),
    'setting':     ('Setting',     'asm', 'Setting', 'Setting',    'set'),
    'assumption':  ('Assumption',  'asm', 'Assumption', 'assumption', 'asm'),
}
PREFIX_KIND = {v[4]: k for k, v in KINDS.items()}
STATUS = {'defined': ('d', 'Defined'), 'derived': ('r', 'Derived'), 'assumed': ('a', 'Assumed'),
          'cited': ('c', 'Cited'), 'context': ('p', 'Context'), 'preview': ('p', 'Preview')}
LETTER_STATUS = {'d': 'defined', 'r': 'derived', 'a': 'assumed', 'c': 'cited'}
DEFAULT_STATUS = {'thm': 'derived', 'def': 'defined', 'asm': 'assumed', 'rem': None, 'ex': None}
ROMAN = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
PROBLEM_GROUPS = ['Homework 1', 'Homework 2', 'Practice midterm 1', 'Practice midterm 2', 'Practice midterm 3']
EXERCISE_HEADING = ('\n<h3>Exercises</h3>\n<p class="ext">From the homework and the practice midterms. '
                    'Each has a hint and a full solution; open them only after trying.</p>\n')

LABEL_RE = r'[A-Za-z0-9]+(?:[-.][A-Za-z0-9]+)*'
REF_PREFIXES = '|'.join(sorted(PREFIX_KIND) + ['sec', 'apx'])
# [text](@label)  [text](=label)  [text](apx:ID)   (text may hold one level of [...] )
BRACKET_RE = re.compile(r'\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\((@|=|apx:)((?:(?:%s):)?%s)\)' % (REF_PREFIXES, LABEL_RE))
AT_RE = re.compile(r'@((?:%s):%s)' % (REF_PREFIXES, LABEL_RE))
FIG_RE = re.compile(r'\{\{fig:([\w-]+)\}\}')


NOT_LISTED = {'How to read'}   # citations from these places get no back-link in "Cited in" rows


class BuildError(Exception):
    pass


# ---------------------------------------------------------------- source files
def read_doc(path):
    """Return (front matter dict, body) of a source file. Front matter is YAML between --- lines."""
    text = Path(path).read_text()
    if text.startswith('---\n'):
        end = text.index('\n---\n', 4)
        meta = yaml.safe_load(text[4:end]) or {}
        return meta, text[end + 5:]
    return {}, text


def write_doc(path, meta, body):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    head = ''
    if meta:
        head = '---\n' + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False, width=10**6) + '---\n'
    path.write_text(head + body)


def parse_attrs(s):
    """Parse '#label key=value key="quoted \\" value" flag' into a dict."""
    out, i, n = {}, 0, len(s)
    while i < n:
        if s[i].isspace():
            i += 1
            continue
        if s[i] == '#':
            m = re.compile(r'#(\S+)').match(s, i)
            out['label'] = m.group(1)
            i = m.end()
            continue
        m = re.compile(r'([\w-]+)(=?)').match(s, i)
        if not m:
            raise BuildError('bad directive attributes: %r' % s)
        key, i = m.group(1), m.end()
        if not m.group(2):
            out[key] = True
            continue
        if i < n and s[i] == '"':
            j, buf = i + 1, []
            while s[j] != '"':
                if s[j] == '\\' and j + 1 < n and s[j + 1] in '"\\':
                    buf.append(s[j + 1])
                    j += 2
                else:
                    buf.append(s[j])
                    j += 1
            out[key] = ''.join(buf)
            i = j + 1
        else:
            m = re.compile(r'\S+').match(s, i)
            out[key] = m.group(0)
            i = m.end()
    return out


def quote_attr(v):
    if re.fullmatch(r'[\w.:-]+', v):
        return v
    return '"' + v.replace('\\"', '\\\\"').replace('"', '\\"') + '"'


DIRECTIVE_RE = re.compile(r'^::: (\w+)(?: \{([^\n]*)\})?\n(.*?)\n:::$', re.M | re.S)


def split_directives(body):
    """Yield ('text', str) and ('dir', name, attrs, inner) chunks in order."""
    pos = 0
    for m in DIRECTIVE_RE.finditer(body):
        if m.start() > pos:
            yield ('text', body[pos:m.start()])
        yield ('dir', m.group(1), parse_attrs(m.group(2) or ''), m.group(3))
        pos = m.end()
    if pos < len(body):
        yield ('text', body[pos:])


# ---------------------------------------------------------------- the guide model
class Guide:
    def __init__(self, root=ROOT):
        self.root = Path(root)
        self.items = []          # dicts in document order
        self.labels = {}         # label -> item / section / appendix dict
        self.sections = []
        self.errors = []

    def err(self, msg):
        self.errors.append(msg)

    # ---- loading
    def load(self):
        r = self.root
        self.parts = yaml.safe_load((r / 'content/parts.yaml').read_text())
        self.front = (r / 'content/front.md').read_text()
        self.index = yaml.safe_load((r / 'content/index.yaml').read_text())
        self.notation = yaml.safe_load((r / 'notation.yaml').read_text())
        self.apx_parts = yaml.safe_load((r / 'appendix/parts.yaml').read_text())
        self.exercises = []
        for p in sorted((r / 'exercises').glob('*.md')):
            meta, body = read_doc(p)
            meta['file'] = str(p.relative_to(r))
            meta['body'] = body
            self.exercises.append(meta)
        self.lectures = []
        for part in self.parts:
            for L in part['lectures']:
                d = r / 'content' / ('L%02d' % L)
                meta, body = read_doc(d / 'lecture.md')
                meta.update(number=L, part=part, body=body, sections=[])
                for k, p in enumerate(sorted(x for x in d.glob('*.md') if x.name != 'lecture.md'), 1):
                    smeta, sbody = read_doc(p)
                    smeta.update(lecture=L, k=k, number='%d.%d' % (L, k), body=sbody,
                                 file=str(p.relative_to(r)))
                    meta['sections'].append(smeta)
                    self.sections.append(smeta)
                self.lectures.append(meta)
        self.apx = []
        for p in sorted((r / 'appendix').glob('*.md'), key=lambda p: (p.name[0], int(re.match(r'.(\d+)', p.name).group(1)))):
            meta, body = read_doc(p)
            meta.update(body=body, file=str(p.relative_to(r)))
            self.apx.append(meta)

    # ---- pass 1: numbers and labels
    def number(self):
        for s in self.sections:
            self.add_label('sec:' + s['id'], dict(kind='section', id=s['id'], number=s['number'], ref='§' + s['number']))
        for a in self.apx:
            n = a['id'][0] + '.' + a['id'][1:]
            self.add_label('apx:' + a['id'], dict(kind='appendix', id=a['id'], number=n, ref='Appendix ' + n))
        exs = {}
        for e in self.exercises:
            exs.setdefault(e['placement'], []).append(e)
        known = {s['id'] for s in self.sections}
        for sid in exs:
            if sid not in known:
                self.err('exercise placement %r is not a section id (%s)' % (sid, [e['file'] for e in exs[sid]]))
        for s in self.sections:
            k = 0
            s['chunks'] = list(split_directives(s['body']))
            s['exercises'] = sorted(exs.get(s['id'], []), key=lambda e: e['order'])
            for n, c in enumerate(s['chunks']):
                if c[0] == 'dir' and c[1] in KINDS:
                    k += 1
                    s['chunks'][n] = ('item', self.make_item(c[1], c[2], c[3], s, k, s['file']))
            for e in s['exercises']:
                k += 1
                attrs = {'label': e['label'], 'name': '%s; %s' % (e['title'], e['source'])}
                e['item'] = self.make_item('exercise', attrs, e['body'].rstrip('\n'), s, k, e['file'])
            for c in s['chunks']:
                if c[0] == 'dir' and c[1] != 'proof':
                    self.err('%s: unknown directive "::: %s"' % (s['file'], c[1]))

    def add_label(self, label, obj):
        if label in self.labels:
            self.err('duplicate label %s' % label)
        self.labels[label] = obj

    def make_item(self, kind, attrs, inner, sec, k, file):
        word, cls, short, refw, prefix = KINDS[kind]
        word = attrs.get('kind', word)
        status = attrs.get('status')
        if kind == 'example':
            status = status or 'defined'
            cls = 'thm' if status == 'derived' else 'def'
        cls = attrs.get('class', cls)
        if status is None:
            status = DEFAULT_STATUS[cls]
        if status == 'none':
            status = None
        num = '%s.%d' % (sec['number'], k)
        label = attrs.get('label')
        if not label:
            self.err('%s: item %s has no #label' % (file, num))
            label = '%s:%s' % (prefix, num)
        elif not label.startswith(prefix + ':'):
            self.err('%s: label %s should start with %s:' % (file, label, prefix))
        it = dict(label=label, kind=kind, word=word, cls=cls, status=status, number=num,
                  id='it-' + num.replace('.', '-'), short=attrs.get('short', short) + ' ' + num,
                  ref=attrs.get('ref', refw), name=attrs.get('name'), inner=inner, file=file,
                  section=sec['id'], attrs=attrs)
        self.items.append(it)
        self.add_label(label, it)
        return it

    # ---- references
    def resolve(self, text, where):
        def lookup(label):
            obj = self.labels.get(label)
            if obj is None:
                self.err('%s: unknown label %s' % (where, label))
                return None
            return obj

        def bracket(m):
            txt, mode, target = m.groups()
            if mode == 'apx:':
                if 'apx:' + target not in self.labels:
                    self.err('%s: unknown appendix entry apx:%s' % (where, target))
                return '<a class="x" href="#%s">%s</a>' % (target, txt)
            obj = lookup(target)
            if obj is None:
                return txt
            txt = txt.replace('#', obj['number'], 1)
            return txt if mode == '=' else '<a class="ir" href="#%s">%s</a>' % (obj['id'], txt)

        def at(m):
            obj = lookup(m.group(1))
            if obj is None:
                return m.group(0)
            text = obj['ref'] if obj['kind'] in ('section', 'appendix') else obj['ref'] + ' ' + obj['number']
            return '<a class="ir" href="#%s">%s</a>' % (obj['id'], text)

        text = BRACKET_RE.sub(bracket, text)
        return AT_RE.sub(at, text)

    def figures(self, text, where):
        def f(m):
            p = self.root / 'figures' / (m.group(1) + '.svg')
            if not p.exists():
                self.err('%s: missing figure %s' % (where, p.name))
                return ''
            return p.read_text()
        return FIG_RE.sub(f, text)

    def content(self, text, where):
        out = []
        for c in split_directives(text):
            if c[0] == 'text':
                out.append(c[1])
            elif c[1] == 'proof':
                out.append(self.render_proof(c[2], c[3]))
            else:
                self.err('%s: "::: %s" is only allowed in section files' % (where, c[1]))
        return self.resolve(self.figures(''.join(out), where), where)

    # ---- rendering blocks
    def render_item(self, it):
        tag = ''
        if it['status']:
            letter, word = STATUS[it['status']]
            tag = '<span class="tag %s">%s</span>' % (letter, word)
        nm = ' <span class="nm">(%s)</span>' % it['name'] if it['name'] else ''
        inner = it['inner']
        sep = '' if it['attrs'].get('tight') or (inner.startswith('\n') and it['cls'] != 'thm') else ' '
        if it['cls'] == 'thm':
            inner = '<span class="body">%s</span>' % inner
        return ('<div class="env %s" id="%s" data-label="%s">%s<span class="hd">%s %s%s.</span>%s%s</div>'
                % (it['cls'], it['id'], it['short'], tag, it['word'], it['number'], nm, sep, inner))

    def render_proof(self, attrs, inner):
        title = attrs.get('title', 'Proof.')
        sep = '' if inner.startswith('\n') or attrs.get('tight') else ' '
        qed = '' if (attrs.get('noqed') or 'class="qed"' in inner) else ' <span class="qed">∎</span>'
        return '<div class="proof"><span class="hd">%s</span>%s%s%s</div>' % (title, sep, inner, qed)

    def render_section(self, s):
        out = []
        for c in s['chunks']:
            if c[0] == 'text':
                out.append(c[1])
            elif c[0] == 'item':
                out.append(self.render_item(c[1]))
            else:
                out.append(self.render_proof(c[2], c[3]))
        body = ''.join(out)
        if s['exercises']:
            if 'class="env ex"' not in body:
                body += EXERCISE_HEADING
            for e in s['exercises']:
                body += self.render_item(e['item']) + '\n'
        slide = s['slide']
        comment = '<!-- ============ L%d %s ============ -->' % (s['lecture'], slide.upper().replace('–', '-'))
        head = ('%s\n<section id="%s">\n<header><span class="eyebrow">L%d · %s</span><h2>%s %s</h2></header>\n'
                % (comment, s['id'], s['lecture'], slide, s['number'], s['title']))
        return head + self.content(body, s['file']) + '</section>'

    def render_unit(self, p):
        return ('<div class="unit" id="%s">\n  <span class="eyebrow">Part %s</span>\n  <h2>%s</h2>\n  %s\n</div>'
                % (p['id'], p['numeral'], p['title'], self.content(p['intro'], 'parts.yaml')))

    def render_lecture(self, lec):
        p = lec['part']
        rows = [('Goal', lec['goal']), ('Main results', lec['main_results']), ('Uses', lec['uses']),
                ('Used later', lec['used_later'])]
        ov = '<div class="ov">' + ''.join('<div class="ov-row"><span class="ov-k">%s</span><div>%s</div></div>' % r
                                          for r in rows) + '</div>'
        where = 'content/L%02d/lecture.md' % lec['number']
        return ('<div class="lecture" id="L%d">\n  <span class="eyebrow">Part %s · %s</span>\n  <h2>Lecture %d · %s</h2>\n  %s%s</div>'
                % (lec['number'], p['numeral'], p['title'], lec['number'], lec['title'],
                   self.content(ov, where), self.content(lec['body'], where)))

    # ---- generated tables
    def roadmap_rows(self):
        rows = []
        for p in self.parts:
            ls = p['lectures']
            if len(ls) == 1:
                lec = 'Lecture %d' % ls[0]
            elif ls == list(range(ls[0], ls[-1] + 1)):
                lec = 'Lectures %d–%d' % (ls[0], ls[-1])
            else:
                lec = 'Lectures ' + ', '.join(map(str, ls))
            rows.append('<tr><td><a href="#%s">%s</a> · %s</td><td>%s</td><td>%s</td></tr>'
                        % (p['id'], p['numeral'], lec, p['question'], p['answer']))
        return '\n'.join(rows)

    def toc(self):
        o = ''
        for p in self.parts:
            o += '<p class="toc-unit"><a href="#%s">Part %s · %s</a></p>\n' % (p['id'], p['numeral'], p['title'])
            for lec in self.lectures:
                if lec['part'] is not p:
                    continue
                o += '<p class="toc-part"><a href="#L%d">Lecture %d · %s</a></p>\n<ol class="toc">\n' % (
                    lec['number'], lec['number'], lec.get('toc', lec['title']))
                for s in lec['sections']:
                    o += '  <li><span class="n">%s</span><a href="#%s">%s</a></li>\n' % (
                        s['slide'], s['id'], s.get('toc', s['title']))
                o += '</ol>\n'
        return o

    def problems_table(self):
        rows = []
        for e in self.exercises:
            for part in e['source'].split('; '):
                g = next((i for i, x in enumerate(PROBLEM_GROUPS) if part.startswith(x)), None)
                if g is None:
                    self.err('%s: source %r is not in %s' % (e['file'], part, PROBLEM_GROUPS))
                    continue
                m = re.search(r'Problem (\d+)(?:\(([a-z])\))?', part)
                pn = (int(m.group(1)), m.group(2) or '') if m else (99, '')
                rows.append((g, pn, part, e))
        rows.sort(key=lambda r: (r[0], r[1]))
        t = ('<div class="tbl"><table>\n<thead><tr><th>Problem</th><th>Topic</th><th>Exercise</th>'
             '<th>Lecture</th></tr></thead><tbody>\n')
        last = None
        for g, _, part, e in rows:
            grp = PROBLEM_GROUPS[g]
            if grp != last:
                t += '<tr><td colspan="4" class="idx-part">%s</td></tr>\n' % grp
                last = grp
            it = e['item']
            t += '<tr><td>%s</td><td>%s</td><td><a class="ir" href="#%s">Exercise %s</a></td><td>%s</td></tr>\n' % (
                part[len(grp):].lstrip(', ') or part, e['title'], it['id'], it['number'], it['number'].split('.')[0])
        return t + '</tbody></table></div>\n'

    def render_index(self):
        ix = self.index
        rows = []
        for group in ix['groups']:
            rows.append('<tr><td colspan="3" class="idx-part">%s</td></tr>' % group['title'])
            for status, text, labels in group['rows']:
                letter, word = STATUS[status]
                links = ', '.join('[#](@%s)' % lb for lb in labels)
                rows.append('<tr><td><span class="tag %s">%s</span></td><td>%s</td><td>%s</td></tr>'
                            % (letter, word, text, links))
        body = ('<!-- ============ INDEX ============ -->\n<section id="index">\n'
                '<header><span class="eyebrow">Index</span><h2>Index of the main text</h2></header>\n'
                '%s\n<div class="tbl"><table>\n<thead><tr><th>Status</th><th>Item</th><th>Where</th></tr></thead>\n'
                '<tbody>\n%s\n</tbody></table></div>\n</section>') % (ix['intro'], '\n'.join(rows))
        return self.content(body, 'content/index.yaml')

    def note_entries(self):
        """[(key, entry, target id, target label)] in notation.yaml order."""
        out = []
        for key, e in self.notation['entries'].items():
            obj = self.labels.get(e['target'])
            if obj is None:
                self.err('notation.yaml: %s: unknown target %s' % (key, e['target']))
                continue
            tl = obj['ref'] if obj['kind'] == 'appendix' else obj['short']
            e = dict(e, h=self.resolve(e['h'], 'notation.yaml'), d=self.resolve(e['d'], 'notation.yaml'))
            out.append((key, e, obj['id'], tl))
        return out

    def render_notation(self):
        def esc(s):
            parts = re.split(r'(<[a-zA-Z/][^<>]*>)', s)
            for i in range(0, len(parts), 2):
                parts[i] = parts[i].replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#x27;')
            return ''.join(parts)
        pos = {i['id']: n for n, i in enumerate(self.items)}
        pos.update({a['id']: len(pos) + n for n, a in enumerate(self.apx)})
        ents = self.note_entries()
        ents.sort(key=lambda e: pos.get(e[2], len(pos)))
        rows, last = [], None
        for key, e, tid, tl in ents:
            m = re.match(r'it-(\d+)-', tid)
            grp = 'Lecture %s' % m.group(1) if m else 'Background'
            if grp != last:
                rows.append('<tr><td colspan="3" class="idx-part">%s</td></tr>' % grp)
                last = grp
            rows.append('<tr><td class="ntn-sym">%s</td><td>%s</td><td><a class="ir" href="#%s">%s</a></td></tr>'
                        % (esc(e['h']), esc(e['d']), tid, tl))
        return ('<!-- ============ NOTATION ============ -->\n<section id="notation">\n'
                '<header><span class="eyebrow">Notation</span><h2>Index of notation</h2></header>\n'
                '%s\n<div class="tbl"><table class="ntn-tbl"><thead><tr><th>Symbol</th><th>Meaning</th>'
                '<th>Defined in</th></tr></thead><tbody>%s</tbody></table></div>\n</section>'
                % (self.content(self.notation['intro'], 'notation.yaml'), ''.join(rows)))

    def note_json(self):
        d = {k: {'h': e['h'], 'd': e['d'], 't': tid, 'tl': tl} for k, e, tid, tl in self.note_entries()}
        return json.dumps(d, ensure_ascii=False)

    def render_appendix(self):
        out = ['<!-- ================================================================ -->\n'
               '<!-- ========================= APPENDIX ============================= -->\n'
               '<!-- ================================================================ -->']
        for letter, part in self.apx_parts.items():
            ents = []
            for a in self.apx:
                if a['id'][0] != letter:
                    continue
                n = a['id'][0] + '.' + a['id'][1:]
                tags = ''.join('<span class="tag %s">%s</span>' % (
                    STATUS[s][0], 'Proved here' if s == 'derived' else STATUS[s][1]) for s in a['status'])
                ents.append('<div class="apx" id="%s">\n<div class="apx-hd"><span class="apx-n">%s</span><h3>%s</h3>%s</div>\n%s</div>'
                            % (a['id'], n, a['title'], tags, self.content(a['body'], a['file'])))
            intro = self.content(part['intro'], 'appendix/parts.yaml')
            out.append('<section id="apx%s" class="part">\n<header><span class="eyebrow">Appendix %s</span><h2>%s</h2></header>\n%s\n%s\n</section>'
                       % (letter, letter, part['title'], intro + '\n' if intro else '', '\n\n'.join(ents)))
        return '\n\n'.join(out)

    # ---- appendix citations: ids, data-from, chips, "Cited in" rows
    def cite_pass(self, doc):
        counts, cites = {}, {}
        state = {'where': '', 'item': ''}
        tok = re.compile(r'<!--CTX:(.*?)-->|<div class="env [a-z]+" id="it-[\d-]+" data-label="([^"]*)">'
                         r'|<a class="x" href="#(\w+)">(.*?)</a>', re.S)

        def sub(m):
            if m.group(1) is not None:
                state['where'], state['item'] = m.group(1), ''
                return ''
            if m.group(2) is not None:
                state['item'] = m.group(2)
                return m.group(0)
            tid, text = m.group(3), m.group(4)
            counts[tid] = counts.get(tid, 0) + 1
            rid = 'r-%s-%d' % (tid, counts[tid])
            where = state['where'] + (' · ' + state['item'] if state['item'] and state['where'].startswith('L') else '')
            cites.setdefault(tid, []).append((rid, where))
            lab = tid[0] + '.' + tid[1:]
            chip = '' if re.sub('<.*?>', '', text).strip() == lab else '<span class="xl">%s</span>' % lab
            return '<a class="x" id="%s" href="#%s" data-from="%s">%s%s</a>' % (rid, tid, html.escape(where), text, chip)

        doc = tok.sub(sub, doc)

        def usedin(m):
            tid = m.group(1)
            seen, links = set(), ''
            for rid, where in cites.get(tid, []):
                if where in seen or where in NOT_LISTED:
                    continue
                seen.add(where)
                links += '<a class="bk" href="#%s" data-from="Appendix %s">%s</a>' % (
                    rid, tid[0] + '.' + tid[1:], html.escape(where))
            row = '<p class="usedin"><span>Cited in</span>%s</p>\n' % links if links else ''
            return m.group(0) + row
        return re.sub(r'<div class="apx" id="(\w+)">\n<div class="apx-hd">.*?</div>\n', usedin, doc, flags=re.S)

    # ---- whole page
    def render(self):
        self.load()
        self.number()
        front = self.front
        front = front.replace('{{roadmap-rows}}', self.roadmap_rows())
        front = front.replace('{{problems-table}}', self.problems_table())
        front = front.replace('{{toc}}', self.toc())
        blocks = ['<!--CTX:How to read-->' + self.content(front, 'content/front.md').rstrip('\n')]
        for p in self.parts:
            blocks.append(self.render_unit(p))
            for lec in self.lectures:
                if lec['part'] is p:
                    blocks.append('<!--CTX:L%d · Overview-->' % lec['number'] + self.render_lecture(lec))
                    for s in lec['sections']:
                        blocks.append('<!--CTX:L%d · %s-->' % (s['lecture'], s['slide']) + self.render_section(s))
        blocks.append('<!--CTX:Index-->' + self.render_index())
        blocks.append(self.render_notation())
        apx = self.render_appendix()
        apx = re.sub(r'(<div class="apx" id="(\w)(\d+)">)', r'<!--CTX:Appendix \2.\3-->\1', apx)
        blocks.append(apx)
        body = self.cite_pass('\n\n'.join(blocks))
        page = (self.root / 'theme/page.html').read_text()
        js = (self.root / 'theme/guide.js').read_text().replace('__NOTE__', self.note_json())
        for k, v in (('{{STYLE}}', (self.root / 'theme/style.css').read_text()),
                     ('{{MATHJAX_CONFIG}}', (self.root / 'theme/mathjax-config.js').read_text()),
                     ('{{GUIDE_JS}}', js), ('{{BODY}}', body)):
            page = page.replace(k, v, 1)
        self.check_tex(body)
        return page

    def check_tex(self, body):
        keys = set(self.notation['entries'])
        for k in sorted(set(re.findall(r'\\class\{ntn-([\w-]+)\}', body)) - keys):
            self.err('\\class{ntn-%s} used but %s is not in notation.yaml' % (k, k))
        for m in re.finditer(r'\\(?:frac|sqrt|dfrac|tfrac)\s*\\class', body):
            self.err('"%s": put braces around \\class after an argument-taking command' % m.group(0))
        for m in re.finditer(r'\\frac\s*\\\w+\s*\\class', body):
            self.err('"%s": put braces around \\class after an argument-taking command' % m.group(0))

    def items_json(self):
        out = []
        for i in self.items:
            text = re.sub(r'<[^>]+>', '', i['inner'])
            text = re.sub(r'\s+', ' ', self.resolve_plain(text)).strip()
            m = None
            for m in re.finditer(r'[.!?](?=\s+[A-Z(]|$)', text):
                if not re.search(r'\b(?:Cor|Def|Rem|Hyp|Thm|Ex|Conv|Props?|cf|e\.g|i\.e|resp)$', text[:m.start()]):
                    break
            out.append(dict(label=i['label'], number=i['number'], id=i['id'], kind=i['word'],
                            name=i['name'], status=i['status'], file=i['file'], section=i['section'],
                            statement_first_sentence=(text[:m.end()] if m else text)[:300]))
        return out

    def resolve_plain(self, text):
        return re.sub(r'<[^>]+>', '', self.resolve(text, 'items.json'))


def main():
    g = Guide()
    page = g.render()
    if g.errors:
        for e in g.errors:
            print('error:', e, file=sys.stderr)
        print('build failed: %d error(s)' % len(g.errors), file=sys.stderr)
        sys.exit(1)
    out = ROOT / 'build'
    out.mkdir(exist_ok=True)
    (out / 'guide.html').write_text(page)
    (out / 'items.json').write_text(json.dumps(g.items_json(), ensure_ascii=False, indent=1) + '\n')
    print('built build/guide.html (%d bytes, %d items, %d sections)' % (len(page.encode()), len(g.items), len(g.sections)))


if __name__ == '__main__':
    main()
