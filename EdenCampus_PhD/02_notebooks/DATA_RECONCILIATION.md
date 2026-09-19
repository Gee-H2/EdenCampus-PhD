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

- [ ] Change annual electrical demand **1,816 MWh → 2,401 MWh** in Table 1,
      the abstract, and the site-description section.
- [ ] Confirm peak stays at **681.6 kW** (already consistent).
- [ ] Describe the electrical demand as a **representative / synthetic profile**
      calibrated to a business-park shape, NOT as metered data — unless real
      metered Eden Campus data is obtained to replace it.
- [ ] Describe the thermal demand explicitly as a **modelled** heating-dominated
      profile (peak 755 kW), not measured.
- [ ] State that PV is derived from committed PVGIS 2023 data for St Andrews
      (56.34 °N, −2.80 °E), reproducible offline.

## Open decision for the researcher

Is there **real metered Eden Campus demand** available?
- If yes: replace the synthetic CSV with the metered series and re-run; the
  data_prep module needs no code change, only the CSV swap.
- If no: the paper must honestly describe demand as a representative synthetic
  profile. This is acceptable for a framework/methodology paper but must not be
  presented as measured data.
