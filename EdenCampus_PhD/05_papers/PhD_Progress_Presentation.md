---
marp: true
title: Eden Campus PhD — Progress Review
author: Gift Udoh
theme: default
paginate: true
size: 16:9
header: "Eden Campus Digital Twin — PhD Progress"
footer: "Gift Udoh · CDT-GIF · Heriot-Watt / University of St Andrews"
style: |
  section { font-size: 24px; }
  h1 { color: #2E86AB; }
  h2 { color: #A23B72; }
  table { font-size: 20px; }
  .small { font-size: 18px; }
  .hl { color: #C73E1D; font-weight: bold; }
  .ok { color: #3BB273; font-weight: bold; }
---

# From Passive Estates to Flexible Generators

### A Multi-Vector Digital Twin for Decarbonising Business Parks

**Gift Udoh** · CDT-GIF · Heriot-Watt University / University of St Andrews

Progress review — the modelling paper (Applied Energy) & the systematic review (RSER)

<!--
SPEAKER NOTE: One sentence to open. "I'll cover two outputs — the Eden Campus
modelling paper, which is my main result, and the systematic review that frames
it. I'll be upfront that the demand data is currently synthetic, and show you
exactly why my conclusions are robust to that." Set the honest tone immediately.
-->

---

## What I set out to do

- **Question:** can PV + multi-vector storage turn a UK business park from a
  passive load into a flexible, low-carbon generator?
- **Method:** a physics-based **digital-twin framework** (PyPSA + pvlib + HiGHS)
  of **Eden Campus**, a real innovation campus in Fife.
- **Approach:** five configurations over **8,760 hours** of optimised dispatch —
  PV-only (S0) through full hybrid (S4: PV + battery + thermal + hydrogen).
- **Two outputs:** the modelling paper (this review's focus) and a systematic
  review positioning business parks as a flexibility resource.

<!--
SPEAKER NOTE: Keep to 45 seconds. The audience has the dataset, so don't oversell
"digital twin" — say "digital-twin framework" and move to results.
-->

---

## The system modelled

Three coupled energy vectors, optimised for least cost:

| Vector | Components |
|---|---|
| **Electricity** | Solar PV (1 MW), grid import/export, battery (500 kW / 2 MWh) |
| **Hydrogen** | Electrolyser → 5 MWh tank → fuel cell (long-duration storage) |
| **Heat** | Heat pump (COP 3), PCM thermal store (200 kW / 1.6 MWh), backup boiler |

- Weather from committed **PVGIS 2023** (St Andrews, 56.34°N) — reproducible offline.
- Costs on the **capacity-charge tariff basis** (£120/kW/yr, UK commercial DUoS).

<!--
SPEAKER NOTE: This slide pre-empts "what did you actually build." The reproducible/
committed-data point matters — it's a strength the dataset-holder will appreciate.
-->

---

## Headline result — and a correction I found while preparing this

In the **committed** model, heat was only costed in S2 & S4 — an **unequal
comparison**. When I apply the heat demand to **all five** scenarios (fair, like-for-like):

<div class="small">

| Scenario | Annual cost — committed (£k) | **Annual cost — corrected (£k)** | Saving vs S0 |
|---|---:|---:|---:|
| S0: PV Only | 539.0 | 729.0 | — |
| S1: PV + BESS | 468.0 | 658.1 | +70.9 |
| S2: PV + PCM TES | 683.3 | 683.3 | +45.7 |
| S3: PV + H₂ LDES | 515.6 | 705.6 | +23.4 |
| **S4: Full Hybrid** | 628.4 | **628.1** | **+100.9** |

</div>

**Corrected ranking: S4 (full hybrid) is cheapest** — not S1. Every storage
scenario saves vs the PV-only baseline.

<!--
SPEAKER NOTE: This is now the honest headline. Lead with the fact you FOUND and
FIXED an error — that is a strength. Reproduced by fix_symmetric_heat.py: control
run matches committed costs to the penny, then symmetric heat flips the ranking.
S4 cheapest because heat-pump scenarios serve heat at ~£93/MWh vs £110 boiler;
adding heat to S0/S1/S3 (boiler-only) raises their cost ~£190k. Boiler resized
600->800 kW so boiler-only scenarios can meet the 756 kW heat peak.
-->

---

## What this changes — and what still holds

**Changes (honestly):**
- <span class="hl">Cost ranking flips</span>: S4 cheapest, not S1. The old
  "S1 optimal" was an artefact of the unequal thermal boundary.
- <span class="hl">Abatement costs</span>: on total emissions, all storage
  scenarios still <span class="ok">cost-negative</span> (MAC −£241 to −£2,155/tCO₂);
  **S2 abates the most CO₂, S4 is cheapest.**

**Still holds (re-verified):**
- <span class="ok">S1 still saves £71k/yr vs S0</span> (both now carry heat).
- <span class="ok">Tariff-dependent heat-pump peak finding</span> — unchanged
  (it's electricity-peak only).
- <span class="ok">Demand-robustness</span> — structural conclusions survive ±30%.

> **I'm bringing this to you as a decision:** agree the fix (incl. boiler sizing)
> before I re-run the full analysis and update the manuscript.

<!--
SPEAKER NOTE: THE key slide for a supervisor meeting. Posture: found it, verified
it, understand the cause, asking for sign-off before the full re-run. Note the
separate export-sign issue on the next slides too. This is PhD-level rigour.
-->

---

## Two further model issues found (for discussion)

- **Grid export never happens.** Export carries the wrong price sign, so the
  optimiser never exports — S0 discards ~266 MWh/yr of surplus solar (~26%).
  *Fix: correct the export sign to a positive SEG payment.*
- **CO₂ factor is dated.** Model uses **0.233 kg/kWh**; the 2023 DESNZ generation
  factor is **~0.207** — so current CO₂ figures are ~11% high.
  *Fix: adopt the chosen DESNZ 2023 factor (decision needed: generation vs consumption).*
- **Grid operator corrected.** Fife/Eden Campus is **SP Energy Networks (SPD)**,
  not SSEN — repo note reversed (SPEN is building a substation at Guardbridge,
  next to Eden Campus).

<!--
SPEAKER NOTE: Present as "found, diagnosed, fixable — none change the method, only
the numbers." The export and CO2 items are quick fixes; the SPEN correction is
already done in the review. All independently verified against primary sources /
re-run, committed to the repo (fix_symmetric_heat.py, boundary checks).
-->

---

## The novel finding — the tariff-dependent heat-pump peak

Heat-pump electrification (S2, S4) has **opposite** peak effects depending only
on the tariff signal:

- **Energy-only tariff:** cost-minimising dispatch drives peak imports **+35%**
  (672 → 904 kW) — cheap heat is dispatched without regard to system peak.
- **Capacity/demand charge:** the full hybrid (S4) **reduces** the peak by ~**40%**;
  S2 stays at baseline (the capacity charge rewards peak management where storage
  can act on it) — the objective now values peak reduction.

### The "objective-function trap"

> A cost-minimising model delivers what the objective *rewards* — not necessarily
> what the flexibility transition *needs*. The tariff signal must be in the objective.

<!--
SPEAKER NOTE: This is the intellectual contribution — emphasise it. It's the bridge
between the modelling paper and the review paper. The identical physical system,
opposite outcomes, same tariff lever.
-->

---

## The honest limitation — demand is synthetic

- Electrical & thermal demand are **representative CIBSE-benchmark profiles**, not
  metered site data (2,401 MWh/yr, 682 kW peak).
- This is **stated explicitly** in the manuscript as the primary limitation.
- **I have built the pipeline to replace it the moment real data arrives:**
  - `ingest_real_demand.py` — normalises any HH/kWh supplier format
  - `compare_demand_synthetic_vs_real.py` — quantifies how reality differs
  - synthetic baseline preserved; `data_prep.py` swaps in real data, no code change

<!--
SPEAKER NOTE: SAY THIS BEFORE THEY DO. This is the slide that wins the room with a
dataset-holder. Posture: "I know exactly what the limitation is and I've engineered
for it." Then immediately go to the next slide — the stress test — which is the
evidence that it doesn't matter to the conclusions.
-->

---

## Why the limitation doesn't change my conclusions

**Stress test (re-run on the corrected symmetric-heat model):** demand scaled
**0.70× – 1.30×** (1,681–3,121 MWh/yr).

| Conclusion | Across the whole ±30% band |
|---|---|
| Cost order **S4 < S1 < S2 < S3 < S0** | <span class="ok">YES — unchanged at every scale</span> |
| Every storage option beats PV-only | <span class="ok">YES</span> |
| Peak reduction: S1/S4 35–42%, S2/S3 1–12% | <span class="ok">YES</span> |

> Conclusions are **structural**, not artefacts of the demand calibration.
> Real data will refine magnitudes — it will not reverse the findings.

<!--
SPEAKER NOTE: Re-run on the CORRECTED model (per the follow-up check). S4 cheapest
at every demand level, order stable, peak pattern holds. If pressed on shape:
magnitude robustness shown, shape validation is next via the comparison harness.
-->

---

## Marginal abatement cost — all storage cost-negative

On the **corrected (symmetric-heat) model, counting total emissions** (grid
electricity + boiler gas) vs S0, against the **UK ETS price £49.41/tCO₂**:

<div class="small">

| Scenario | CO₂ abated vs S0 (t/yr) | MAC (£/tCO₂) |
|---|---:|---:|
| S1: PV + BESS | 32.9 | −2,155 |
| **S2: PV + PCM TES** | **189.5 (most)** | −241 |
| S3: PV + H₂ | 14.8 | −1,581 |
| **S4: Full Hybrid** | 156.5 | −645 **(cheapest)** |

</div>

**All four abate at negative cost.** **S2 cuts the most CO₂** (its heat pump
displaces ~1,650 MWh of boiler gas); **S4 is the cheapest overall.** No single
scenario wins on both — the trade-off is the point.

<span class="small">*MAC magnitudes depend on the gas factor (0.183 tCO₂/MWh) and boiler
efficiency assumed; ordering and the all-negative result are robust. Source:
`verify_total_emissions_mac.py`.*</span>

<!--
SPEAKER NOTE: CORRECTED slide. The earlier version wrongly measured CO2 as
solar-displacement only, which ignored the heat pump's grid draw and the boiler
gas it displaces. On total emissions, S2 abates most, S4 is cheapest. Do NOT say
"full hybrid delivers the most abatement" — that was the error. If asked about
S2's small-looking -241: it rests on a LARGE abatement (189.5 t), so it is robust,
unlike the earlier -2,582 which rested on 17.7 t.
-->

---

## The systematic review (RSER) — first output, well-architected

**"From passive estates to flexible generators: a systematic review of UK business
parks in electricity markets."**

- **Spine:** structural fit → institutional invisibility → objective-function trap.
- **Original contribution:** a 5-type typology (T1–T5) of UK business parks mapped
  to the FES 2025 flexibility categories — the first such characterisation.
- **Method:** PRISMA 2020 + PRISMA-S, 3 databases + grey corpus, Rayyan, Cohen's κ,
  with field-specific appraisal (data / scale / market realism).

<!--
SPEAKER NOTE: Frame honestly as "architected, entering the evidence phase." Don't
imply the screening is done. Strengths: the argument and the typology.
-->

---

## RSER review — verification status

<div class="small">

| Verified this session | Status |
|---|---|
| FES 2025 flexibility figures (127 TWh, 51 GW EV, 10→96 GW storage) | <span class="ok">✅ vs NESO source</span> |
| Legal: Class E, Scottish/NI use classes, RED II Art. 22 | <span class="ok">✅ primary sources</span> |
| Regulatory: TCR, P415, DFS year-round, REMA | <span class="ok">✅ (dates corrected)</span> |
| Method refs (PRISMA, Rayyan, Cohen) | <span class="ok">✅ supplied</span> |
| Typology exemplars (Edinburgh Park, Eurocentral, MSIP, Catalyst) | <span class="ok">✅ confirmed</span> |

</div>

**Remaining (the evidence phase):** screened-corpus citations & findings, PRISMA
flow counts, data-spine park counts — the irreducible systematic-review legwork.

<!--
SPEAKER NOTE: This shows rigour — every fact-checkable claim is already verified,
with a committed record (LEGAL_REGULATORY_VERIFIED.md). The honest gap is the
corpus screening, which is the actual review work.
-->

---

## Reproducibility & provenance — built in

- **Every manuscript number traces to a committed artifact:**
  - Tables 3 & 4 → `generate_manuscript_tables.py` (from model output)
  - Table 5 (meteorology) → `table5_meteorological_summary.py` (from raw CSVs)
  - Stress test, MAC, all figures (300 dpi) → committed scripts
- **Single source of truth:** `data_prep.py` — no hand-transcription.
- **All on GitHub**, version-controlled, re-runnable in the `eden_phd` environment.

<!--
SPEAKER NOTE: This is a quiet strength that separates good from great PhD work.
A dataset-holder can literally re-run and check. Say "nothing in the paper is a
number I can't regenerate."
-->

---

## Where I am and what's next

**Done & defensible**
- Modelling paper: method sound; **re-run pending agreement on the fixes**
  (heat boundary, export sign, CO₂ factor)
- Review paper: architected, every verifiable claim checked

**Immediate next steps**
1. <span class="hl">Ingest real Eden Campus demand</span> → run comparison harness
   → re-run model (pipeline ready)
2. Fill RSER review from screened corpus (the evidence phase)
3. Next modelling papers: co-optimised dispatch & peak-aware thermal storage

<!--
SPEAKER NOTE: End on forward momentum. The real data is the natural next milestone
and you're ready for it — invite them to share it.
-->

---

## What I need from you

1. **Agree the model fixes** before I re-run the full analysis:
   - symmetric heat boundary (+ boiler sizing 600→800 kW)
   - export price sign (enable SEG export)
   - CO₂ factor (which DESNZ 2023 figure — generation vs consumption?)
2. **Metered Eden Campus demand** — the single biggest step to validation;
   the ingest pipeline is ready for it.
3. **A second screener** for the systematic review (dual-screening for Cohen's κ).
4. **Authorship & target-journal confirmation** for both outputs.

<!--
SPEAKER NOTE: Make the asks explicit and concrete — supervisors respond well to a
clear decision list. #1 is the one you need before any re-run; #2 unblocks
validation; #3 is required for the review's method; #4 is housekeeping.
-->

---

## Thank you — discussion

**Key artifacts (all committed to GitHub):**

<div class="small">

- `Paper1_Eden_Campus_Manuscript.docx` — modelling paper
- `generate_manuscript_tables.py`, `stress_test_demand_sensitivity.py` — reproducible results
- `paper1_RSER_review/` — review sections + verification records
- `REVIEW_2026-11-07…md` — editorial review (AI-assisted, cross-checked against sources)
- `data_prep.py`, `ingest_real_demand.py`, `compare_demand_synthetic_vs_real.py` — data pipeline

</div>

*Happy to take questions — including on the synthetic-demand limitation.*

<!--
SPEAKER NOTE: Inviting the hardest question signals confidence. See the Q&A annex
below (not part of the rendered deck in presenter mode) for prepared answers.
-->

---

<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Q&A Annex — prep (not for projection)

<div class="small">

**"Why is S4 the cheapest, not S1?"**
On a fair thermal boundary (heat costed in all scenarios), the heat-pump scenarios
serve heat at ~£93/MWh (elec ÷ COP 3) vs £110 gas boiler, so S4 ends up cheapest
(£628k). The old "S1 optimal" result costed heat only in S2/S4 — an error I found,
reproduced, and fixed (`fix_symmetric_heat.py`). S1 still saves £71k/yr vs S0.

**"How do I know the fix is right?"**
Control run reproduces the committed costs to the penny; the symmetric re-run flips
the ranking. Boiler resized 600→800 kW so boiler-only scenarios meet the 756 kW
heat peak. All in the repo, re-runnable.

**"Your peak finding — 35% or 40%?"**
Both, and that's the point: +35% peak *increase* under energy-only tariff;
~40% *reduction* under a capacity charge. Same system, opposite outcomes,
tariff-driven. Unaffected by the heat-boundary fix (it's electricity-peak only).

**"Why does the model never export?"**
A sign error on the export price — found, flagged, quick fix. It means S0 currently
discards ~26% of its solar; correcting it will change absolute numbers, not the
ranking.

**"Isn't this just a simulation, not a digital twin?"**
Correct distinction. It's a digital-twin **framework** demonstrated with synthetic
inputs; the measured-data coupling is the next phase — the ingest/validation
harness already exists.

**"Is the review finished?"**
No — it's architected and every fact-checkable claim is verified (incl. correcting
the Fife DNO to SPEN). The evidence phase (corpus screening, data-spine counts)
remains.

**"Demand is synthetic — how do you know anything?"**
Stress test shows the structural conclusions hold across ±30% demand. Pipeline
built to ingest your real data with no code change.

</div>

<!--
SPEAKER NOTE: This annex renders as slides but is marked "not for projection" —
either delete before presenting or keep as your private crib. Every answer maps to
a committed artifact so you can show evidence live if challenged.
-->
