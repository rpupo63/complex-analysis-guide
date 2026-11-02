# Complex Analysis Companion

The source for *Holomorphic Functions*, a one-page HTML textbook built from the slides of a 13-lecture complex analysis course (5 parts, 168 sections, 357 numbered items, 65 appendix entries). Read `AGENTS.md` for the source format and the house rules.

## Build

```
python3 build.py        # -> build/guide.html, build/items.json
```

You need Python 3 and PyYAML. The build fails with a list of errors if a label, an appendix id, a figure or a notation key is unknown.

## Check

```
just setup              # once: .venv with Playwright, and local MathJax 3.2.2 in node_modules/
just check              # build + check.py
just roundtrip          # compare with reference/guide.v17.html
```

`check.py` renders the page in the system Chromium (`CHROMIUM=/path` overrides `/usr/bin/chromium`) and serves MathJax from `node_modules/`, so it works without network access. It fails on any of these:
- a MathJax error (`[data-mml-node="merror"]`);
- horizontal overflow at a 400 px viewport;
- a duplicate id or a dangling `href="#…"`;
- unresolved source syntax;
- an unknown notation key;
- the `\frac\class` pitfall.

`check.py --no-render` runs only the structural checks.

## Publish

The page is the claude.ai artifact `https://claude.ai/artifact/NxvWHwcmzyxE99T6Fa26uf`. Give `build/guide.html` to a Claude session with artifact access and ask it to publish to that URL.

## Migration report (v17 → source tree)

`tools/extract.py` produced the source tree from `reference/guide.v17.html`. `tools/roundtrip.py` compares the build with that file and passes. These match exactly:
- every baseline count (175 sections, 357 items, 402 `.env`, 231 proofs, 38 exercises, 65 appendix entries, 287 appendix citations, 1494 `a.ir`, 26 figures, 108 notation entries, 2654 `\class{ntn-…}`);
- the set of element ids;
- the set of link targets;
- the normalised text of every section, appendix entry and lecture;
- the whole page markup, after the normalisations listed below.

Intentional differences:
1. **`data-from` in lecture overview boxes (8 links).** In v17, an appendix link in a lecture's overview box carried the context of the *previous* section, for example "L3 · Slide 21 · Rem. 3.19.2" inside Lecture 4's overview. The build writes "L4 · Overview". The "Cited in" rows of A6, D5, D7, E6, E16 and E18 change to match.
2. **`r-` citation ids are numbered in document order.** In v17 some were numbered in the order they were added (for example A12: 1, 2, 9, 3, …). The set of ids is unchanged. Each "Cited in" row now lists its places in document order.
3. **HTML comments and blank lines between blocks are regenerated uniformly.** For example, every section is preceded by `<!-- ============ L3 SLIDE 4 ============ -->`. They are not rendered.
4. **The `NOTE` JSON keys are in first-definition order** (the order of `notation.yaml`). The entries themselves are identical.

After the migration, a slide-by-slide audit against `Complex/lectures/*.pdf` led to content fixes in L1, L3, L5, L7, L8, L9, L12 and L13 (see the git history). Since then `just roundtrip` reports those sections as changed. That is expected.

`figures/gen_l01.py` generates the Lecture 1 figures added after the migration (x2-1, x2-2, x13-2, x16-1 to x16-4).

`legacy/` holds the scripts that produced v17 (`process.py`, `ex_insert.py`, `exercises.py`, `figs3.py` for the Lecture 12 figures, `chk4.py`) and the original handoff notes. They are history and are not used by the build.
