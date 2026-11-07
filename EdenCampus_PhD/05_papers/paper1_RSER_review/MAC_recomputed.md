# Marginal Abatement Cost — recomputed from corrected model (for §7.2)

**Date:** 7 November 2026
**Purpose:** Close the `[DATA]` MAC item in RSER review §7.2. Values are recomputed
from the corrected, reconciled full-year model (`full_year_scenario_comparison.xlsx`,
capacity-charge basis) — NOT the pre-correction skeleton numbers.

## Definition
MAC of scenario X vs the S0 PV-only baseline:
    MAC = (Annual cost_X − Annual cost_S0) / (CO2 saved_X − CO2 saved_S0)   [£ / tCO2]
A **negative** MAC means the scenario abates carbon *while also saving money*
(cost-negative abatement). A **positive** MAC above the carbon price means the
scenario buys abatement more expensively than the market price of carbon.

## Benchmark — UK ETS carbon price
**£49.41 / tCO₂e** for the 2026 scheme year (statutory determination).
Source: gov.uk, *UK ETS: Carbon price for use in civil penalties, 2026*
("the carbon price per tonne … for the scheme year beginning 1 January 2026 is
£49.41"). (Market UKA ≈ £48 on ICAP, Feb 2026 — consistent.)

## Results (vs S0, capacity-charge primary basis)

| Scenario | Δ annual cost vs S0 (£k/yr) | Δ CO₂ saved vs S0 (tCO₂/yr) | MAC (£/tCO₂) |
|---|---:|---:|---:|
| S1: PV + BESS | −71.0 | +39.2 | **−1,811** |
| S3: PV + H₂ LDES | −23.4 | +42.5 | **−551** |
| S4: Full Hybrid | +89.4 | +60.8 | **+1,470** |
| S2: PV + PCM TES | +144.3 | +17.7 | **+8,153** |

(S0 is the baseline; absolute annual figures: S0 cost £539.0k, 178.0 tCO₂/yr.)

## The honest interpretation (use this framing, not "all beat the ETS price")

The MAC splits the scenarios into two groups, and that split **reinforces the
objective-function-trap argument** rather than giving a single headline number:

1. **S1 and S3 are cost-negative abatement.** They cut carbon *and* cost less than
   the baseline (MAC −£1,811 and −£551/tCO₂). Against a UK ETS price of £49.41/tCO₂
   these are not just below the carbon price — they are below zero: the estate is
   paid to decarbonise. This is the strong, defensible rhetorical point.

2. **S2 and S4 are expensive abatement under this tariff** (+£1,470 and
   +£8,153/tCO₂), i.e. far above the £49.41 ETS price. This is precisely the
   objective-function-trap in numbers: heat-pump electrification adds carbon
   savings but, under the modelled tariff, at a cost per tonne that no carbon
   market would justify — because the cost-minimising objective is not valuing the
   abatement, it is incurring it as a side-effect of serving thermal load.

**Suggested §7.2 sentence (replace the [DATA] placeholder):**
> On a marginal-abatement-cost basis against the PV-only baseline, the
> battery and hydrogen electrical-storage configurations (S1, S3) abate carbon at
> **negative cost** (−£1,811 and −£551/tCO₂ respectively) — below the UK ETS
> carbon price of £49.41/tCO₂ [REF: gov.uk UK ETS 2026] and indeed below zero,
> meaning the estate is rewarded for decarbonising. By contrast, the heat-pump
> configurations (S2, S4) abate at **positive cost far above the carbon price**
> (+£1,470 and +£8,153/tCO₂) under the modelled tariff — a direct quantification
> of the objective-function trap, in which a cost-minimising objective incurs
> rather than values the abatement.

## Caveats (state if pressed)
- MAC is sensitive to the tariff basis (capacity-charge here). Under an energy-only
  tariff the cost deltas differ; recompute if the primary basis changes.
- Small Δ-CO₂ denominators (S2: +17.7 t) make its MAC numerically large/unstable —
  present S2's MAC as "very high / not cost-effective" rather than leaning on the
  exact £8,153 figure.
- CO₂ factor 0.233 tCO₂/MWh grid (as per model); if the grid factor is updated the
  Δ-CO₂ and MAC move proportionally.
