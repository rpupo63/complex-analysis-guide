# AGENTS.md: Complex Analysis Companion

This repo is the source for a one-page HTML textbook of a 13-lecture complex analysis course. `python build.py` turns the source into `build/guide.html`, a self-contained page (inline CSS, JS and SVG; only the fonts and MathJax 3.2.2 load from a CDN).

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

The guide is the claude.ai artifact `https://claude.ai/artifact/NxvWHwcmzyxE99T6Fa26uf`. To update it, give `build/guide.html` to a Claude session with artifact access and ask it to publish to that URL. A local agent without artifact access cannot publish it.
