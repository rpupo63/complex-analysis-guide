# AGENTS.md: Complex Analysis Companion

This repo (`Complex Analysis/guide/`) is the source for a one-page HTML textbook of a complex analysis course (Lectures 1–13 and 15; there is no Lecture 14 yet). `python build.py` turns the source into `build/guide.html`, a self-contained page (inline CSS, JS and SVG; only the fonts and MathJax 3.2.2 load from a CDN).

## Rules

- **Do not edit `build/`.** It is generated. Change the source and rebuild.
- **Do not edit `reference/guide.v17.html`.** It is the frozen v17 page that the migration was checked against.
- **Do not run `tools/extract.py` again.** It was a one-time migration. It overwrites `content/`, `exercises/`, `appendix/`, `notation.yaml`, `figures/` and `theme/`, so it would discard every edit made since. It refuses to run without `--force`.
- **Do not write item numbers by hand** (for example "Theorem 6.3.1") anywhere in `content/`, `exercises/`, `appendix/` or the YAML files. Write a label instead (see "References"). Numbers inside TeX are not checked, but avoid them too.
- **Before you publish, run** `just check`. It runs the build and the structural and render checks.
- **Use `build/items.json` to find items.** It maps every label to its number, id, file, section and first sentence. Use it instead of reading the 1.2 MB page.

## Layout

| Path | What it holds |
|---|---|
| `content/front.md` | Header, "How to read this guide", roadmap text, threads, techniques, problem-table intro. `{{roadmap-rows}}`, `{{problems-table}}` and `{{toc}}` are generated. |
| `content/parts.yaml` | Parts P1–P5: numeral, title, lecture list, intro, roadmap question and answer. |
| `content/LNN/lecture.md` | Lecture title (`toc:` if the contents line differs), overview box (`goal`, `main_results`, `uses`, `used_later`), body text. |
| `content/LNN/KK-slug.md` | One file per section, in order. Front matter has `id` (historical, e.g. `x16`, `s20`; never change it), `slide`, `title` and an optional `toc`. The file order sets the section number. |
| `content/index.yaml` | Index of the main text: groups of `[status, description, [labels]]`. |
| `exercises/*.md` | Homework and practice-midterm problems (see "Adding things"). |
| `appendix/*.md`, `appendix/parts.yaml` | Appendix entries A1–E20 (front matter `id`, `title`, `status` list) and the intros of parts A–E. |
| `notation.yaml` | Notation entries, in order of first definition. |
| `figures/*.svg` | Inline SVG figures, included with `{{fig:NAME}}`. |
| `theme/` | `page.html` skeleton, `style.css`, `mathjax-config.js`, `guide.js` (`__NOTE__` is replaced by the notation JSON). |
| `tools/` | `extract.py` (the one-time migration) and `roundtrip.py` (compares the build with the reference). |

## Course material (source of truth for content)

This repo lives at `Complex Analysis/guide/`. Next to it, `Complex Analysis/Complex/` is the teacher's repo (`maksym-radziwill/Complex`): a read-only clone that must stay identical to his remote. Never edit, add, commit or push anything there; only `git pull` to get new material. The guide must agree with this material:

| Material | Path (from this repo) | Covered in the guide by |
|---|---|---|
| Lecture N slides | `../Complex/lectureNN.pdf` (PDF page = slide number) | `content/LNN/`; each section's `slide:` front matter names its slides |
| Homework 1 / Homework 2 | `../Complex/hw.pdf`, `../Complex/hw2.pdf` | `exercises/hw1-*.md`, `exercises/hw2-*.md` |
| Practice midterms 1–3 | `../Complex/practice-midterm-K.pdf` | `exercises/pmK-*.md` |
| FreeFEM (teacher's files) | `../Complex/FreeFEM/` | `exercises/hw1-optional-freefem-bonus.md` |
| Coin-change handout (not in the teacher's repo) | `../handouts/coin_counting.pdf` | §6.20, `content/L06/20-worked-example-making-change.md` |
| Lecture 15 slides, "Reflection and polygons" (not in the teacher's repo; **unverified, may be wrong in places**) | `../handouts/lecture15.pdf` | `content/L15/`. Do not copy these slides blindly: check each claim. Where a slide is wrong, the guide corrects it in a remark named "correction to the slide" (`grep -l 'correction to the slide' content/L15/*.md`). If the teacher later adds `../Complex/lecture15.pdf`, compare it with this file and switch the source. |
| Beto's own FreeFEM work | `../freefem-work/` | not part of the guide |

Read PDFs with `pdftotext -layout FILE -`; look at the page image when formulas come out garbled. The build never reads them.

## Resolving a reference in a question

Beto may name things in any of these ways. Resolve each to a file before answering, and answer from the guide's source and, when accuracy matters, the PDF.

| He says | Means | Find it with |
|---|---|---|
| "Theorem 6.11.3", "Prop 3.6.4", "Exercise 11.10.4" | numbered item lecture.section.k | `grep -B2 -A6 '"number": "6.11.3"' build/items.json` (gives label, file, section) |
| `thm:the-stamp-formula` | item label (stable even if numbers shift) | `grep -A8 '"label": "thm:the-stamp-formula"' build/items.json` |
| "§6.11", "section 6.11" | section 11 of Lecture 6 | `content/L06/11-*.md` (file prefix = section number) |
| `f11`, `s20`, `x16` | section id (historical, irregular) | `grep -l '^id: f11$' content/*/*.md` |
| "Lecture 6", "L6" | the whole lecture | `content/L06/` (`lecture.md` has the overview) |
| "L6 slide 12" | a slide of the original lecture | the section whose `slide:` range contains 12: `grep -H '^slide:' content/L06/*.md`; the slide itself is page 12 of `../Complex/lecture06.pdf` |
| "HW2 problem 1(b)", "PM3 4(a)" | a homework or practice-midterm problem | `exercises/hw2-p1b.md`, `exercises/pm3-p4a.md` (`source:` front matter gives the exact sheet problem) |
| "A.12", "appendix C.4" | appendix entry | `appendix/A12-*.md` |
| a symbol, e.g. "$V^g_\eps$ in L3" | notation entry | `notation.yaml` (key is the `ntn-KEY` used in TeX; `target:` is the defining item) |

Numbers are assigned by the build, so after an edit rebuild (`python build.py`) before trusting `build/items.json`. If a number does not resolve, say so instead of guessing; it may come from an older version of the page.

## Source format

The bodies are **HTML + TeX fragments**. They are **not** Markdown: `**bold**` stays as literal asterisks, so write `<b>`, `<em>`, `<p>`, `<ul>` and so on. The build adds only these constructs:

**Items.** A directive block. The `:::` lines must start at column 0.
```
::: theorem {#thm:identity-theorem-l10 name="identity theorem"}
Let $f,g$ be holomorphic on a [connected](apx:C4) open set $U$ ...
:::
::: proof
<b>Step 1.</b> ... by @cor:isolated-zeros ...
:::
```
- Kinds: `theorem proposition lemma corollary fact definition convention example remark exercise hypothesis setting assumption`.
- Attributes:
  - `#label` (required) uses a kind prefix: `thm: prop: lem: cor: fact: def: conv: eg: rem: ex: hyp: set: asm:`.
  - `name=` is the parenthesised name.
  - `status=` is `defined`, `derived`, `assumed`, `cited`, `context` or `preview`. The default is `derived` for theorem-like items, `defined` for definitions and examples, and `assumed` for hypotheses. Remarks and exercises have no tag.
  - Rare overrides: `kind="Standing setting"` (heading word), `short=` (tooltip word), `class=` (CSS class), and `tight` (no space after the heading).
- Numbering is lecture.section.k, counted in order within the section. The id is `it-L-s-k`, so **inserting an item renumbers the later items in that section and changes their ids.**
- `::: proof {title="Proof, Step 1."}`: the default title is "Proof.". The build adds the ∎ unless the body already contains a `class="qed"` span or the directive has `noqed`.

**References.** The build resolves every label. An unknown label stops the build.

| Write | Get |
|---|---|
| `@thm:cauchy-riemann` | link "Theorem 1.5.2" (default word per kind: Theorem, Prop., Lemma, Cor., Def., Example, Remark, Exercise, …) |
| `[Theorems #](@thm:x)`, `[#](@thm:x)`, `[Lemma #(b)](@lem:x)` | link with your text; `#` becomes the number |
| `[Proof of Lemma #.](=lem:x)` | the same text **without** a link (used in proof titles and tooltips) |
| `@sec:x16` | link "§1.16" |
| `@apx:C4` | link "Appendix C.4" |
| `[connected](apx:C4)` | an appendix link with the "C.4" chip. The build generates its `r-` id, its `data-from` ("L1 · Slide 4 · Thm. 1.3.1") and the entry's "Cited in" row. |

**Notation.** In TeX, write `\class{ntn-KEY}{...}` to tint a symbol. KEY must exist in `notation.yaml`. Add braces after argument-taking commands: write `\frac{\class{ntn-x}{x}}{2}`, never `\frac\class...`.

**Math.** Use `$…$` for inline math and `\[ … \]` for display math. `$$` is not enabled. Make a formula display math if it is too wide for a phone.

## Writing rules

- **Status tags.** Every numbered theorem, definition and assumption has exactly one tag: Defined, Derived, Assumed, Cited, Context or Preview. Remarks and exercises have none.
- **Citations.** Every non-trivial step in a proof or solution cites the item it uses (`@label`) or an appendix entry (`apx:`). A forward reference to a later lecture is allowed only if it is marked "(Lecture N)".
- **Style.** Write plain, precise sentences.
- **Figure colours.** Use `currentColor` and the CSS variables, never hard-coded hex. A third series uses the `--asm-ink` brown, because blue and purple are hard to tell apart.

## Adding things

- **An item:** add a directive to the right section file. The number is assigned automatically.
- **A section:** add a file `content/LNN/KK-slug.md` with a new unique `id`. Later section files must be renamed so the file order stays correct. Adding a section renumbers the later sections of that lecture, and the TOC updates itself.
- **An exercise:** add a file `exercises/<hw1|hw2|pm1|pm2|pm3>-<problem>.md` with front matter `label`, `source` (for example "Homework 2, Problem 1(b)"; separate several sources with "; "), `title`, `placement` and `order`.
  - `placement` is the id of the section that supplies the last tool the exercise needs.
  - `order` sets the position among the exercises placed in the same section.
  - The body is the statement, followed by `<details class="sol"><summary>Hint</summary>…</details>` and `<details class="sol"><summary>Solution</summary>…</details>`.
  - The exercise is appended to that section, and the "Homework and practice midterms" table updates itself.
- **A notation entry:** add it to `notation.yaml` (`h` symbol HTML, `d` meaning, `target` label of the defining item), then use `\class{ntn-KEY}{…}` in formulas.
- **An appendix entry:** add a file `appendix/<ID>-slug.md` with `id`, `title` and `status`. `derived` is shown as "Proved here".
- **An index row:** add it to `content/index.yaml`.

## Checks

```
python build.py                  # build/guide.html + build/items.json; non-zero exit on any error
.venv/bin/python check.py        # structure; MathJax errors (data-mml-node="merror"); 400 px overflow; dangling links
python tools/roundtrip.py        # compare with reference/guide.v17.html (expected to drift once content changes)
just check                       # build + check.py (roundtrip is separate: just roundtrip)
```

`roundtrip.py` was the migration's acceptance gate. After the first intentional content change it will report differences. That is expected: read them, and check that they are the changes you meant.

## Publishing

The guide is on GitHub Pages at https://rpupo63.github.io/complex-analysis-guide/ (the repo is public). `.github/workflows/pages.yml` runs `build.py` on every push to `master` and deploys `build/guide.html` as `index.html`. To publish, run `just check`, commit, and push. An older copy is the claude.ai artifact `https://claude.ai/artifact/NxvWHwcmzyxE99T6Fa26uf`; it updates only when a Claude session with artifact access republishes it.
