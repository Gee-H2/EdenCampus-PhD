# Data Reconciliation Note — Eden Campus Digital Twin

**Date:** 19 September 2026
**Purpose:** Establish a single source of truth for model inputs and document the corrections needed so the notebooks, data files, and manuscript agree.

---

## Problem found

Three different demand figures existed across the project:

| Source | Elec. peak | Elec. annual |
|---|---|---|
| Manuscript / Table 1 | 681 kW | **1,816 MWh** |
| Committed CSV (`eden_campus_demand_2023.csv`) | 681.6 kW | **2,401 MWh** |
| Model inline generator (`PyPSA Model.ipynb`) | ~500 kW | (not loaded from CSV) |

In addition:
- The PyPSA model and Full Year model **regenerated demand inline** instead of loading the committed CSV — two copies of the same synthetic logic that can drift.
- Both models **downloaded PVGIS weather live** at run time instead of using the committed weather CSVs, breaking offline reproducibility.

## Root cause

The committed demand CSV was itself produced by a synthetic profile generator
(base 150 kW, peak 500 kW, seasonal + hourly factors, `seed=42`), not metered
data. The manuscript's 1,816 MWh figure does not correspond to the CSV or the
model — it appears to be a legacy/target number that was never reconciled.

## Resolution

1. **Single source of truth:** `02_notebooks/data_prep.py` now loads all inputs
   from committed files only:
   - Electrical demand ← `01_data/demand/eden_campus_demand_2023.csv`
   - PV profile ← `01_data/weather/eden_campus_2023.csv` (no live PVGIS)
   - Thermal demand ← documented modelled function of the demand index

2. **Authoritative figures** (computed from committed data, printed by the module):

   | Quantity | Value |
   |---|---|
   | Electrical peak | 681.6 kW |
   | Electrical annual | 2,400.9 MWh |
   | Electrical load factor | 40.2 % |
   | Thermal peak | 755 kW |
   | PV annual (1 MW) | 1,029.7 MWh |
   | PV capacity factor | 11.8 % |

## Required manuscript corrections

Status updated 2026-09-24 (commit 958d497). Only items verified done are ticked.

- [x] Change annual electrical demand **1,816 MWh → 2,401 MWh**. Done in the
      Demand Inputs paragraph of `Paper1_Eden_Campus_Manuscript.docx`. NOTE: the
      demand figure was found only in that paragraph — it is NOT in Table 1, and
      the abstract does not state an annual-demand number, so no change was needed
      there. Verified against the CSV (2,400.9 MWh) and a full-year model run.
- [x] Also corrected annual **thermal** demand **1,648 MWh → 1,728 MWh** in the
      same paragraph (modelled series gives 1,727.6 MWh; this was not in the
      original checklist but was wrong and is now fixed).
- [x] Confirm peak stays at **681.6 kW** — confirmed unchanged and consistent
      (manuscript states 681 kW; thermal 755 kW also consistent).
- [x] Describe the electrical demand as a **representative / synthetic profile**,
      NOT metered — the Demand Inputs paragraph already states "In the absence of
      metered hourly site data, electrical and thermal demand profiles were
      synthesised…". Verified present.
- [x] Describe the thermal demand explicitly as a **modelled** profile — covered
      by the same "synthesised" sentence (peak 755 kW).
- [ ] STILL OPEN — framing inconsistency: the abstract / four-layer-architecture
      text still describes the digital twin as coupling **"measured site data"**,
      which contradicts the Demand Inputs paragraph's "in the absence of metered
      hourly site data". Reconcile this wording before submission so a reviewer
      does not catch the contradiction.
- [ ] STILL OPEN — state that PV is derived from committed PVGIS 2023 data for
      St Andrews (56.34 °N, −2.80 °E), reproducible offline. Not yet verified as
      present in the manuscript.
- [x] Peak-reduction headline (S1 = 39.7%): verified reproducible in the
      full-year model (S0 = 1.4%, S1 = 39.7%); not an error.

## Open decision for the researcher

Is there **real metered Eden Campus demand** available?
- If yes: replace the synthetic CSV with the metered series and re-run; the
  data_prep module needs no code change, only the CSV swap.
- If no: the paper must honestly describe demand as a representative synthetic
  profile. This is acceptable for a framework/methodology paper but must not be
  presented as measured data.
