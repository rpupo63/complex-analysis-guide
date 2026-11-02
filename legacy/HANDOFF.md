# Handoff: turn the Complex Analysis study guide into a source project

You are a local coding agent. Your job: convert a single built HTML study guide into a maintainable source tree with a build script, so that future edits (by people or LLMs) are small, safe diffs instead of regex surgery on a 1.2 MB file. **The rendered output must stay the same.**

Read this whole file before starting.

---

## 1. What you are given

This bundle contains:

| File | What it is |
|---|---|
| `guide.html` | **The source of truth.** The current published guide (version 17), about 1.24 MB, self-contained. Everything must be recovered from this. |
| `legacy/process.py` | The script that merged Lectures 12–13 into the built HTML. Its parts (id assignment, reference linking, appendix "Cited in" bookkeeping, TOC, index) show the conventions the build must reproduce. |
| `legacy/ex_insert.py`, `legacy/exercises.py` | How the homework/midterm exercises were inserted. `exercises.py` holds their original source (statement, hint, solution, placement) as Python strings. Useful as a ready-made source for `exercises/`. |
| `legacy/figs3.py` | Example figure generator (Python → inline SVG strings). |
| `legacy/l12.html`, `legacy/l13.html` | Hand-written source for Lectures 12–13 before integration. Shows the authoring format at its cleanest. |
| `legacy/chk4.py` | Playwright render checker (MathJax errors, phone-width overflow). Reuse it. |

No other copies of the original source exist. An earlier build pipeline (`src.html`, `build.py`, `guide.js`) was lost. **Do not try to find it.**

---

## 2. Anatomy of `guide.html` (verified)

### Page skeleton (in order)
1. `<title>Complex Analysis Companion</title>`, Google Fonts links (STIX Two Text; IBM Plex Sans Condensed), one big `<style>` block. Colours are CSS custom properties on `:root`, with dark mode under `@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]) … }` and again under `:root[data-theme="dark"]`.
2. MathJax config `<script>`:
   ```js
   window.MathJax = {
     loader: { load: ['[tex]/html'] },
     tex: { packages: {'[+]': ['html']}, inlineMath: [['$','$']], displayMath: [['\\[','\\]']],
       macros: { eps: '\\varepsilon', R: '\\mathbb{R}', norm: ['\\lVert #1 \\rVert', 1] } },
     svg: { fontCache: 'global' }
   };
   ```
   Then `<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-svg.js">`.
   **Display math is `\[ … \]`, inline is `$…$`. `$$` is not enabled.**
3. `<div class="wrap">` with `<header>` (eyebrow, `<h1>Holomorphic Functions</h1>`, lede). Then front matter: "How to read this guide" with the tag legend, a roadmap table (`id="roadmap"`), "Homework and practice midterms" (`id="problems"`), and the contents (`<h3>Contents</h3>` + `.toc` lists).
4. Five parts: `<div class="unit" id="P1">` … `P5`. Each contains lectures `<div class="lecture" id="L1">` … `L13`. A lecture has an eyebrow, an `<h2>Lecture N · Title</h2>`, and an overview box `.ov` whose rows (`.ov-row`, key `.ov-k`) are Goal / Main results / Uses / Used later.
5. Sections follow the lecture div: `<section id="…">` → `<header><span class="eyebrow">L10 · Slide 2</span><h2>10.1 The identity theorem</h2></header>` → content.
6. Appendix: `id="apxA"` etc., entries `<div class="apx" id="A12">` with `.apx-hd` (`.apx-n` "A.12", `<h3>`, status tag), then `<p class="usedin">` ("Cited in" back-links), then body.
7. Index of the main text (`id="index"`), index of notation (`id="notation"`).
8. Floating back button `#backbtn` and tooltip `#tip`, then the main `<script>`: `var NOTE = {…JSON…};` followed by about 7 KB of JS (tooltips, jump stack, flash).

### Baseline counts (your rebuilt page must match these)
| Thing | Count |
|---|---|
| `<section>` | 175 |
| lectures / parts | 13 / 5 |
| numbered items `id="it-L-s-k"` | 357 |
| `<div class="env…">` (incl. unnumbered) | 402 |
| proofs `.proof` | 231 |
| exercises `.env.ex` | 38 (33 are homework/midterm) |
| appendix entries `.apx` | 65 (A1–A25, B1–B5, C1–C8, D1–D7, E1–E20) |
| appendix citations `id="r-X-N"` | 287 |
| internal links `a.ir` | 1494 |
| figures `<figure>` | 26 |
| notation entries in `NOTE` | 108 |
| `\class{ntn-…}` uses in TeX | 2654 |

### Section ids (irregular, historical: preserve them, since links use them)
| Lecture | ids | §-number → id |
|---|---|---|
| L1 | x1–x16 | §1.k → x*k* |
| L2 | w1–w10 | §2.k → w*k* |
| L3 | s2–s21, no s19 | §3.k → s(k+1) for k ≤ 17; §3.18 → s20; §3.19 → s21 (ids follow slide numbers; §3.17 covers slides 18–19) |
| L4 | t2–t13 | §4.k → t(k+1) |
| L5 | v2–v13 | §5.k → v(k+1) |
| L6 | f1–f19 | f*k* |
| L7 | g1–g5 | g*k* |
| L8 | h1–h16 | h*k* |
| L9 | j1–j10 | j*k* |
| L10 | k1–k14 | k*k* |
| L11 | m1–m10 | m*k* |
| L12 | n1–n17 | n*k* |
| L13 | o1–o8 | o*k* |

Some sections hold no numbered items (overflow slides). Section numbering comes from the `<h2>` text ("10.1 …"), not from the id.

### Item block
```html
<div class="env thm" id="it-10-1-1" data-label="Thm. 10.1.1"><span class="tag r">Derived</span><span class="hd">Theorem 10.1.1 <span class="nm">(identity theorem)</span>.</span> <span class="body">…</span></div>
```
- `env` kinds: `thm` (theorems, props, lemmas, corollaries), `def` (definitions, examples, conventions), `rem`, `asm` (assumptions/hypotheses/settings), `ex` (exercises), plain `env` (unnumbered, e.g. inside the appendix).
- Status tags: `tag d` Defined · `tag r` Derived (in the appendix the text is "Proved here") · `tag a` Assumed · `tag c` Cited · `tag p` Context / Preview.
- `data-label` is the short form used in tooltips and "Cited in" text: Thm., Prop., Lemma, Cor., Def., Ex., Rem., Hyp., Conv., Fact, Setting…
- Numbering is lecture.section.k, counted within each section in order of appearance.
- Proofs: `<div class="proof"><span class="hd">Proof.</span> … <span class="qed">∎</span></div>`. Some are split as "Proof, Step 1." across sections.
- Exercises: same `env ex` block, then `<details class="sol"><summary>Hint</summary>…</details><details class="sol"><summary>Solution</summary>…</details>`. Older exercises have only a Solution.

### Links (three kinds)
1. **Internal:** `<a class="ir" href="#it-3-6-4">Prop. 3.6.4</a>` or `href="#s12"` for "§3.11". Generated from text patterns (see `legacy/process.py`, `KW`/`REF` regexes). In the source, write these as labels (§4).
2. **Appendix:** `<a class="x" id="r-A12-9" href="#A12" data-from="L3 · Slides 18–19 · Exercise 3.17.4">Cauchy–Schwarz<span class="xl">A.12</span></a>`.
   - `id` is `r-<target>-<n>`, a running count per target.
   - `data-from` is "\<section eyebrow\> · \<data-label of the enclosing item\>" (or "Appendix X.n").
   - The `.xl` chip is shown only when the link text differs from the label.
   - Each target's `.usedin` row lists one back-link per distinct `data-from`, pointing to `#r-…`.
   - All of this is derived data. Regenerate it; never author it.
3. **Notation:** inside TeX, `\class{ntn-KEY}{…}` tints a symbol. `NOTE[KEY] = {h: display HTML, d: description, t: target id, tl: target label}`. A symbol can mean different things in different lectures, so those are separate keys. The notation index table is generated from `NOTE` in first-definition order.

### Figures
Inline SVG inside `<figure>` (sometimes `.fpanels` > `.fpanel`), using `currentColor` and CSS variables so dark mode works. Lecture 12 figures came from `legacy/figs3.py`. Others exist only as inline SVG: extract them to `figures/*.svg` verbatim.

---

## 3. Target layout

```
complex-analysis-guide/
├── AGENTS.md              # house rules for future agents (write this; see §6)
├── README.md              # how to build, check, publish
├── build.py               # source → build/guide.html (+ build/items.json)
├── check.py               # structural + render checks; non-zero exit on failure
├── content/
│   ├── front.md           # header, how-to-read, legend (roadmap/TOC/problem table are generated)
│   ├── parts.yaml         # P1–P5: title, lecture list, roadmap question/answer
│   └── L01/ … L13/
│       ├── lecture.md     # title, eyebrow, overview box (Goal/Main results/Uses/Used later)
│       └── 01-<slug>.md   # one file per section; front matter: id (x1…), slide, number
├── exercises/<source>-<problem>.md   # front matter: source, title, placement (section id), order
├── appendix/A12-cauchy-schwarz.md    # front matter: id, title, status
├── notation.yaml          # KEY: {h, d, target: <label>}  (order = first definition)
├── figures/*.svg (+ generators *.py)
├── theme/style.css, theme/guide.js, theme/mathjax-config.js
└── build/                 # generated only; gitignored except guide.html if you like
```

### Source format (recommended)
Markdown, with fenced block directives for items and **TeX passed through untouched**:

```markdown
::: thm {#thm:identity status=derived name="identity theorem"}
Let $f,g$ be holomorphic on a [connected](apx:C4) open set $U$ …
:::

::: proof
**Step 1.** … by @thm:taylor-remainder …
:::
```

- **Labels instead of numbers.** Write `@thm:identity`; the build resolves it to `<a class="ir" href="#it-10-1-1">Theorem 10.1.1</a>`. Use a kind word that matches the item (`@thm:`, `@prop:`, `@lem:`, `@cor:`, `@def:`, `@ex:`, `@rem:` …) or allow `@identity` with the kind taken from the item. Provide `@sec:<id>` for "§10.1". Unknown label → build error.
- **Keep the HTML ids exactly as now** (`it-10-1-1`, `x16`, `A12`…). Existing deep links depend on them. The build maps label → number → id.
- **Appendix refs:** `[text](apx:A12)` → class `x` link plus the auto-generated id, `data-from` and chip.
- **Notation:** keep writing `\class{ntn-KEY}{…}` inside TeX as now. The build checks every KEY exists in `notation.yaml`.

**Critical pitfall: protect math before Markdown processing.** Markdown will eat `_`, `*`, `\\`, `\[` inside TeX. Before rendering, replace every `$…$` and `\[…\]` with an opaque placeholder; restore it afterwards. Alternatively use markdown-it-py with a dollarmath-style plugin configured for `\[ \]`. Test on a formula with `a_{n}^{*}` and `\\`. Also allow raw HTML blocks (tables, `<details>`, figures), since much existing content is HTML.

A pragmatic first pass is acceptable: keep each item and section body as **HTML+TeX fragments** in the `.md` files (Markdown allows raw HTML) and convert only the structure (item wrappers, numbers, references, appendix links). Prose can be converted to Markdown later. Byte-for-byte prose fidelity matters more than Markdown purity.

### `build.py` must generate
- item numbering and ids; `data-label`; `hd`/`nm`/tag spans;
- all `a.ir` references from labels; all `a.x` appendix links with `r-` ids, `data-from`, chips, and every `.usedin` row;
- the lecture overview "Main results" row may stay hand-written, but its references must be labels;
- TOC, index of the main text, notation index, roadmap table, "Homework and practice midterms" table (from exercise front matter, grouped HW1, HW2, PM1, PM2, PM3, sorted by problem);
- the `NOTE` JSON from `notation.yaml`, inlined before `theme/guide.js`;
- `build/items.json`: `[{label, number, id, kind, name, status, file, section, statement_first_sentence}]`. This is the map future agents read instead of the 1 MB page.

The output stays **one self-contained HTML file** (inline CSS/JS/SVG). Only the fonts and MathJax load from a CDN.

---

## 4. Migration plan

1. `git init`; commit the untouched `guide.html` as `reference/guide.v17.html`.
2. **Extraction script** (`tools/extract.py`, keep it in the repo): parse `reference/guide.v17.html` with BeautifulSoup or lxml and write the source tree.
   - Item labels: derive from kind + name, slugified (`thm:identity`, `lem:products`); fall back to `it-10-1-1` → `x10.1.1` when there is no name. Make them unique.
   - Turn every `a.ir` back into `@label` / `@sec:id`, and every `a.x` into `[text](apx:ID)`. Drop generated `r-` ids, chips and `.usedin` rows.
   - Pull `NOTE` into `notation.yaml`. Copy the CSS and JS verbatim to `theme/`.
   - Exercises: build `exercises/*.md` from `legacy/exercises.py` or from the HTML. Pre-existing lecture exercises (e.g. 8.16.1–8.16.5) stay in their section files.
3. Write `build.py`.
4. **Round-trip test (acceptance gate).** Build, then compare with `reference/guide.v17.html`:
   - all baseline counts in §2 match;
   - the set of element ids is identical;
   - every `href="#…"` target set is identical (allowing reordering of `r-` numbers, but each `.usedin` row must have the same set of `data-from` texts);
   - normalised text diff (strip tags, collapse whitespace) of each `<section>`, `.apx` and `.lecture` is empty. Write `tools/roundtrip.py` and iterate until it passes. Report any intentional differences.
5. **Render check:** `check.py` reuses `legacy/chk4.py`:
   - Playwright Chromium, route the MathJax CDN to a local `node_modules/mathjax/es5` (`npm install mathjax@3.2.2`);
   - count `[data-mml-node="merror"]`, which must be 0 (do **not** check `mjx-merror`, which misses errors in SVG output);
   - at 400 px viewport, `document.documentElement.scrollWidth` must be 400 (wide display math inside its scroll container is fine);
   - no dangling `href="#…"`.
6. Write `AGENTS.md` and `README.md`. Push to a private GitHub repo if the user provides one.

---

## 5. Lessons already learned (avoid repeating them)
- **`\class` needs braces after argument-taking commands.** `\frac\class{…}{…}`, `\sqrt\class…` and `\frac\pi\class…` cause "Missing argument for \class". Write `\frac{\class{ntn-x}{x}}{2}`.
- **Never run a transforming script on its own output.** It duplicates content. The build reads source and writes `build/` only.
- **Don't `pkill -f` a pattern that matches your own shell command.**
- **MathJax from the CDN may be blocked in sandboxes.** Use the local npm copy for checks.
- **Very wide inline formulas break phone layout.** Make them display math.
- **Figure colours:** a third series uses the `--asm-ink` brown, because blue and purple were indistinguishable. Keep colours as CSS variables, never hard-coded hex.
- **Text style:** plain, precise sentences. Steps are justified by citing numbered items or the appendix.

---

## 6. `AGENTS.md` should state
- **Status tags:** Defined / Derived / Assumed / Cited / Context / Preview. Every numbered item has exactly one.
- **Citation rule:** every non-trivial step in a proof or solution cites the item it uses (`@label`) or an appendix entry (`apx:`). Forward references (to a later lecture) are allowed only if marked "(Lecture N)".
- **How to add:**
  - an item: put a directive in the right section file; the number is assigned automatically;
  - an exercise: a new file in `exercises/` with `placement:` the section id where its last needed tool appears; include a Hint and a Solution;
  - a notation entry: `notation.yaml` plus `\class{ntn-KEY}` in formulas;
  - an appendix entry: a file in `appendix/`.
- Run `python build.py && python check.py` before publishing; never edit `build/`.
- **Publishing:** the guide is a claude.ai artifact at `https://claude.ai/artifact/NxvWHwcmzyxE99T6Fa26uf`. To update it, give `build/guide.html` to a Claude session with artifact access and ask it to publish to that URL. A local agent cannot publish it.

## 7. Definition of done
- [ ] Repo with the layout above; `python build.py` produces `build/guide.html` and `build/items.json` with no errors.
- [ ] Round-trip test passes against `reference/guide.v17.html` (or every difference is listed and justified).
- [ ] `check.py`: 0 MathJax errors, scrollWidth 400 at 400 px, 0 dangling links.
- [ ] No hard-coded item numbers remain in `content/`, `exercises/` or `appendix/` (grep for `\b\d+\.\d+\.\d+\b` outside TeX and front matter).
- [ ] `AGENTS.md`, `README.md` written; extraction and round-trip tools committed.
- [ ] A short report to the user: what was built, any content differences, and how to make an edit.
