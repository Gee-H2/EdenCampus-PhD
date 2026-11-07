# Rendering the progress presentation

`PhD_Progress_Presentation.md` is a [Marp](https://marp.app/) slide deck
(Markdown). Every figure in it is drawn from a committed, verified artifact in
this repo (cross-checked 7 Nov 2026).

## Quickest ways to render

**Option A — VS Code (no install beyond the extension):**
1. Install the "Marp for VS Code" extension.
2. Open `PhD_Progress_Presentation.md`.
3. Click the preview icon; use "Export slide deck…" → PDF / PPTX / HTML.

**Option B — Marp CLI (needs Node.js):**
```bash
npx @marp-team/marp-cli@latest PhD_Progress_Presentation.md --pdf
npx @marp-team/marp-cli@latest PhD_Progress_Presentation.md --pptx   # editable PowerPoint
npx @marp-team/marp-cli@latest PhD_Progress_Presentation.md --html   # self-contained
```
(Node is not installed in this environment, so render on your own machine.)

**Option C — marp.app:** paste the Markdown into the web editor.

## Presenter notes & Q&A

- Speaker notes are in HTML comments (`<!-- ... -->`) — visible in Marp presenter
  mode, not on the projected slide.
- The final **Q&A Annex** slide is marked "not for projection." Either delete it
  before exporting the client deck, or keep it as your private crib — it maps each
  likely question to a committed artifact so you can show evidence live.

## If a number is questioned

Regenerate from source and show it:
```bash
# Tables 3 & 4
python 02_notebooks/generate_manuscript_tables.py
# Robustness
python 02_notebooks/stress_test_demand_sensitivity.py
```
Sources: `manuscript_table3/4_*.csv`, `MAC_recomputed.md`,
`LEGAL_REGULATORY_VERIFIED.md`, `FES2025_VERIFIED_FIGURES.md`.
