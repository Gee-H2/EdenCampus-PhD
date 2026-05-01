# Paper 1 — Figure Refinement Plan

**Paper:** Multi-Vector Digital Twin Framework for Decarbonising Business Parks
**Target journal:** Applied Energy
**Status:** Manuscript draft complete; figures need publication-quality refinement
**Last updated:** 1 May 2026

---

## Purpose of This Document

The Paper 1 manuscript is complete and pushed to GitHub. The seven figures referenced in the manuscript exist in `04_results/figures/` but were generated as exploratory plots rather than publication-ready outputs. This document captures the refinement plan so the work can be resumed in a fresh session without losing context.

---

## Figure Inventory and Refinement Status

| # | Filename | Source notebook | Caption-promised content | Refinement priority |
|---|---|---|---|---|
| 1 | `figure1_pv_vs_demand.png` | `PV vs Demand.ipynb` | Two panels: summer (12 Jul 2023) + winter (11 Jan 2023), green/red shading | Verify panels match dates and shading |
| 2 | `figure2_digital_twin_architecture.png` | (diagram tool) | 4 layers + bidirectional feedback loop arrow | Likely needs full redraw |
| 3 | `figure3_modelling_workflow.png` | (diagram tool) | Input → demand modelling → optimisation → KPIs, with feedback loop | Verify components labelled |
| 4 | `scenario_comparison_S0_S4.png` | `Scenario comparison.ipynb` | 6 panels with dashed S0 baseline reference lines | Verify reference lines visible |
| 5 | `full_year_analysis.png` | `Full Year Model.ipynb` | 4 panels: monthly PV, monthly grid, annual SF, annual CO₂ | Verify panel layout |
| 6 | `sensitivity_analysis.png` | `Sensitivity Analysis.ipynb` | 6 panels: 3 weather + 3 design sensitivity | Verify panel layout and key annotations |
| 7 | `eden_campus_digital_twin_results.png` | `PyPSA Model.ipynb` | 6 panels of S4 dispatch across 4 representative weeks | Verify all panels present |

---

## Universal Quality Standards for Applied Energy

Every figure must meet these standards:

| Quality dimension | Standard |
|---|---|
| Resolution | ≥300 DPI (publication standard) |
| Format | PNG for first submission, EPS or PDF for camera-ready |
| Font size | Readable at column-width when printed (≥10 pt) |
| Axis labels | Units always shown in brackets, e.g. "Solar Fraction (%)" |
| Legend | All series labelled, no cropping |
| Colour | Colour-blind safe palette (avoid red-green pairs) |
| Grid | Light grey only, never bold |
| Title | Generally NOT on figure itself (caption serves that role) |

### Universal matplotlib settings

Add this block to the top of every notebook used to generate publication figures:

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 11,
    'font.family': 'serif',
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.dpi': 100,         # Display
    'savefig.dpi': 300,        # Save
    'savefig.bbox': 'tight',
    'savefig.format': 'png',
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.linewidth': 0.5,
})
```

This single block makes all figures look journal-grade.

---

## Specific Refinement Tasks Per Figure

### Figure 1 — PV vs Demand (motivation)

**Source:** `PV vs Demand.ipynb`

- Confirm summer date is **12 July 2023**, winter date is **11 January 2023**
- Add green-shaded "PV surplus" region (between PV curve and demand curve where PV > demand)
- Add red-shaded "Grid import required" region (where demand > PV)
- Y-axis label: "Power (kW)"
- X-axis label: "Hour of day"
- Single combined legend with: PV generation (orange), Demand (blue), Surplus (green fill), Import required (red fill)
- Two panels stacked vertically: summer top, winter bottom

### Figure 2 — Digital Twin Architecture

**Source:** Diagram tool (recommended: diagrams.net / draw.io, free web-based)

- 4 layers stacked vertically with consistent colour scheme:
  1. Data Acquisition (smart meters, BMS, weather, PV inverters, grid signals)
  2. Model Layer (PV, BESS, PCM TES, heat pump, hydrogen LDES, building loads)
  3. Optimisation and Control (PyPSA dispatch, KPIs, sensitivity)
  4. Visualisation and Dashboard
- Bidirectional feedback arrow between Visualisation ↔ Data Acquisition
- Software stack labels (PyPSA, pvlib, HiGHS) on appropriate boxes

### Figure 3 — Modelling Workflow

**Source:** Diagram tool

- Top-down or left-right flow: Input data → Building demand → Optimisation → KPIs
- Calibration feedback arrow visible
- Scenarios S0–S4 listed inside the optimisation box

### Figure 4 — Scenario Comparison (6 panels)

**Source:** `Scenario comparison.ipynb`

- All 5 scenarios coloured consistently across panels (define `SCENARIO_COLOURS` dict at top)
- Dashed reference line marking S0 in panels (a), (d), (f)
- Y-axes labels with units
- Panel titles: (a) Solar Fraction (%), (b) Self-Consumption (%), (c) CO₂ Saved (t/yr), (d) Grid Import (MWh), (e) Peak Reduction (%), (f) Annual Cost (£k)

### Figure 5 — Full-Year Monthly

**Source:** `Full Year Model.ipynb`

- 2×2 panel layout
- Top-left: stacked monthly PV by scenario
- Top-right: monthly grid import lines
- Bottom-left: annual solar fraction bars
- Bottom-right: annual CO₂ saving bars

### Figure 6 — Sensitivity Analysis (6 panels)

**Source:** `Sensitivity Analysis.ipynb`

- Top row: weather years 2020–2023
  - (a) Solar Fraction (%)
  - (b) CO₂ Savings (t/yr)
  - (c) Annual Cost (£k)
- Bottom row: market and design sensitivity
  - (d) Solar Fraction across grid prices £180–£380/MWh
  - (e) Solar Fraction across BESS sizing 200–4,000 kWh, colour-coded by storage duration
  - (f) Cost vs Solar Fraction trade-off across BESS configurations
- **Critical:** Annotate the 250 kW/1,000 kWh and 500 kW/1,000 kWh points in panel (f) so the headline finding (energy capacity dominates power rating) is visually obvious

### Figure 7 — Hybrid System Hourly Operation

**Source:** `PyPSA Model.ipynb`

- 4 weekly panels (one per representative season week)
- Stacked area plot for electricity bus dispatch
- Storage state-of-charge subplots for BESS, PCM, H₂ tank
- Multi-vector clearly distinguishable through colour and panel grouping

---

## Recommended Session Workflow

### Phase 1 — Audit (30 min)
Open each existing figure on Mac, compare against the captions in the manuscript. List which ones need:
- Minor tweaks (axis labels, font sizes, DPI)
- Major regeneration (layout changes, missing panels)
- Full redraw (Figures 2 and 3 architecture diagrams)

### Phase 2 — Re-generate (2–3 hours)
Work through the notebooks in order, applying the universal matplotlib settings and the figure-specific tasks above.

### Phase 3 — Quality Pass (30 min)
Apply universal quality standards to each refined figure. Save with `dpi=300` and consistent filenames in `04_results/figures/`.

### Phase 4 — Commit and Push (5 min)
```bash
cd ~/Documents/GitHub/EdenCampus-PhD
git add EdenCampus_PhD/04_results/figures/
git commit -m "Refine all 7 manuscript figures to publication quality"
git push origin main
```

---

## Suggested Scenario Colour Palette (Colour-Blind Safe)

```python
SCENARIO_COLOURS = {
    'S0': '#999999',  # Grey (baseline)
    'S1': '#0072B2',  # Blue (BESS)
    'S2': '#E69F00',  # Orange (PCM)
    'S3': '#009E73',  # Green (H2)
    'S4': '#CC79A7',  # Pink (Hybrid)
}
```

This palette is from the Wong (2011) colour-blind safe set, widely used in *Nature* and *Science* journals.

---

## What Tools To Use

| Figure | Tool | Reason |
|---|---|---|
| 1, 4, 5, 6, 7 | matplotlib in Jupyter | Direct generation from model outputs |
| 2, 3 | diagrams.net (free, web) or matplotlib + patches | Architecture and workflow diagrams |

For Figures 2 and 3, drawing them from scratch in matplotlib is doable but time-consuming. A free tool like diagrams.net allows you to export PNG at high resolution and produces cleaner diagrams.

---

## Reminder of Manuscript Captions

The captions are already locked in the manuscript. Each figure must satisfy its caption — the caption is the contract.

See `Paper1_Eden_Campus_Manuscript.docx` Section "Figure Captions" for the full text of all 7 captions.

---

**End of plan. Pick up here next session.**
