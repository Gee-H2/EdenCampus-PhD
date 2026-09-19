# Heat-Pump Peak Finding — Verification & Manuscript Note

**Date:** 19 September 2026
**Purpose:** Verify the manuscript's headline "~32% electrical peak increase from
heat pump electrification" against the corrected model, and document a tension
introduced by the capacity/demand charge.

---

## Verified numbers (corrected model, full year 8760 h)

Metric: peak grid import (kW), heat-pump scenarios (S2, S4) vs baseline (S0).

### WITHOUT capacity charge (the basis the manuscript was written on)

| Scenario | Grid-import peak | vs S0 |
|---|---|---|
| S0: PV Only | 671.9 kW | — |
| S2: PV + PCM + Heat Pump | 904.4 kW | **+34.6%** |
| S4: Full Hybrid | 904.4 kW | **+34.6%** |

→ The manuscript's "approximately 32%" is essentially correct (true value +34.6%).
  The finding is REAL: heat-pump load piles onto low-solar winter evening peaks.

### WITH capacity charge (£120/kW/yr — realistic UK billing)

| Scenario | Grid-import peak | vs S0 |
|---|---|---|
| S0: PV Only | 671.9 kW | — |
| S2: PV + PCM + Heat Pump | 671.9 kW | +0.0% |
| S4: Full Hybrid | 408.9 kW | **−39.1%** |

→ With a demand charge, the optimiser actively manages the peak. The heat-pump
  penalty is neutralised (S2) or reversed (S4).

---

## The tension (important for the manuscript)

The capacity charge added to make the battery peak-shave (fixing the previously
near-zero peak-reduction KPI) also **removes the headline heat-pump peak-penalty
finding**, because the optimiser now has an incentive to manage that peak.

The two findings are mutually exclusive under a single model configuration:
- **Energy-only tariff** → heat-pump peak penalty (+35%) is visible; battery
  peak-shaving is invisible (~0%).
- **Energy + capacity charge** → battery peak-shaving is strong (−40%); heat-pump
  penalty is neutralised.

## Recommendation

Present BOTH as explicit tariff scenarios rather than choosing one:

1. Under energy-only billing, heat-pump electrification raises peak grid imports
   by ~35% — the under-reported penalty (retain as a finding).
2. Introducing a capacity/demand charge (realistic UK commercial billing) induces
   active peak management: the battery shaves ~40% and the heat-pump penalty is
   eliminated — the mitigation.

This converts a single fragile claim into a richer, more defensible two-part
narrative (problem + solution) and demonstrates the framework's value for tariff
design, not just technology comparison.

## Manuscript corrections still required (independent of the above)

- Annual electrical demand: 1,816 MWh → **2,401 MWh**
- S1 annual cost saving vs S0: £42.4k → **£71k** (was the 1000x cost bug:
  the real figure was £42.4 *million*, mislabelled as £42.4k)
- S1 20-year saving: £847k → **£1,420k**
- Solar fraction (38.8%), CO2 savings (217 t/yr) — unchanged, still correct.
