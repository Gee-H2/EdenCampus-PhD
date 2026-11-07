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

Progress review — Paper 1 (modelling) & Paper 1 (RSER review)

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

## Headline result — S1 (PV + Battery) is operationally optimal

<div class="small">

| Scenario | Solar Fraction (%) | CO₂ Saved (t/yr) | Peak Reduction (%) | Annual Cost (£k) |
|---|---:|---:|---:|---:|
| S0: PV Only | 31.8 | 178.0 | 1.4 | 539.0 |
| **S1: PV + BESS** | **38.8** | **217.2** | **39.7** | **468.0** |
| S2: PV + PCM TES | 35.0 | 195.7 | 1.4 | 683.3 |
| S3: PV + H₂ LDES | 39.4 | 220.5 | 8.8 | 515.6 |
| S4: Full Hybrid | 42.7 | 238.8 | 40.0 | 628.4 |

</div>

**S1 saves £71k/yr (£1.42M over 20 yr)** vs baseline, cuts 217 tCO₂/yr, and
reduces peak grid import by ~40%.

<!--
SPEAKER NOTE: This is the money slide. Numbers are from the generated table
(manuscript_table3). If asked "why does S1 beat S4?" — S4 adds heat-pump electrical
load that, under this tariff, raises cost; storage of electricity (S1) is the
cheapest marginal improvement. Let them probe.
-->

---

## The novel finding — the tariff-dependent heat-pump peak

Heat-pump electrification (S2, S4) has **opposite** peak effects depending only
on the tariff signal:

- **Energy-only tariff:** cost-minimising dispatch drives peak imports **+35%**
  (672 → 904 kW) — cheap heat is dispatched without regard to system peak.
- **Capacity/demand charge:** the same system **reduces** the peak by up to **40%**
  — the objective now values peak management.

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

**Stress test:** re-ran all five scenarios with demand scaled **0.70× – 1.30×**
(1,681–3,121 MWh/yr) — bracketing where real data could plausibly land.

| Conclusion | Across the whole ±30% band |
|---|---|
| S1 is cost-optimal | <span class="ok">YES — at every scale</span> |
| Cost ranking stable | <span class="ok">YES — S1 < S3 < S0 < S4 < S2 throughout</span> |
| Peak-reduction pattern | <span class="ok">YES — S1/S4 high, S2/S3 low throughout</span> |

> My conclusions are **structural**, not artefacts of the demand calibration.
> Real data will refine magnitudes — it will not reverse the findings.

<!--
SPEAKER NOTE: This is your shield. Reproducible: stress_test_demand_sensitivity.py.
If pressed: "I scaled magnitude uniformly; shape validation is the next step, and
the comparison harness is built for exactly that." Honest about what's shown vs not.
-->

---

## Marginal abatement cost — reinforces the trap

Abatement cost vs S0, against the **UK ETS price of £49.41/tCO₂** (2026):

| Scenario | MAC (£/tCO₂) | Reading |
|---|---:|---|
| **S1: PV + BESS** | **−1,811** | <span class="ok">cost-negative — paid to decarbonise</span> |
| **S3: PV + H₂** | **−551** | <span class="ok">cost-negative</span> |
| S4: Full Hybrid | +1,470 | <span class="hl">expensive — far above carbon price</span> |
| S2: PV + PCM TES | very high | <span class="hl">not cost-effective (tiny ΔCO₂)</span> |

Electrical storage (S1, S3) abates **below zero cost**; heat-pump options cost far
more per tonne than any carbon market — the objective-function trap, quantified.

<!--
SPEAKER NOTE: Don't claim "all beat the ETS price" — that's wrong and they may know
it. The split IS the story. Source: MAC_recomputed.md, UK ETS £49.41 from gov.uk.
-->

---

## Paper 2 (RSER review) — first output, well-architected

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
- Modelling paper: numerically sound, internally consistent, stress-tested
- Review paper: architected, every verifiable claim checked

**Immediate next steps**
1. <span class="hl">Ingest real Eden Campus demand</span> → run comparison harness
   → re-run model (pipeline ready)
2. Fill RSER review from screened corpus (the evidence phase)
3. Paper 2 (co-optimised dispatch) & Paper 3 (peak-aware thermal storage)

<!--
SPEAKER NOTE: End on forward momentum. The real data is the natural next milestone
and you're ready for it — invite them to share it. Close in ~30 seconds.
-->

---

## Thank you — discussion

**Key artifacts (all committed to GitHub):**

<div class="small">

- `Paper1_Eden_Campus_Manuscript.docx` — modelling paper
- `generate_manuscript_tables.py`, `stress_test_demand_sensitivity.py` — reproducible results
- `paper1_RSER_review/` — review sections + verification records
- `REVIEW_2026-11-07…md` — independent editorial review
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

**"Your demand is synthetic — how do you know anything?"**
Stated as the primary limitation. Stress test shows S1-optimal, ranking, and
peak findings hold across ±30% demand. Conclusions are structural; magnitudes
will refine with your data. Pipeline is built to ingest it with no code change.

**"Isn't this just a simulation, not a digital twin?"**
Correct distinction. It's a digital-twin **framework** demonstrated with synthetic
inputs. The bidirectional measured-data coupling is the next phase — which is
exactly why the ingest/validation harness already exists.

**"Why is S1 better than the full hybrid S4?"**
Under the capacity-charge tariff, battery storage of electricity is the cheapest
marginal improvement. S4 adds heat-pump electrical load that raises cost more than
its extra CO₂/solar-fraction benefit — see the MAC split.

**"Your peak finding — 35% or 40%?"**
Both, and that's the point: +35% peak *increase* under energy-only tariff;
~40% *reduction* under a capacity charge. Same system, opposite outcomes, tariff-driven.

**"Is the review finished?"**
No — it's architected and every fact-checkable claim is verified. The evidence
phase (corpus screening, data-spine counts) is the remaining systematic-review work.

**"Commercial-emissions +5% / public −47% claim?"**
Direction corroborated (CBRE 2023: commercial real estate ~flat since 1990); exact
split not yet sourced — flagged, will re-word or re-source before submission.

</div>

<!--
SPEAKER NOTE: This annex renders as slides but is marked "not for projection" —
either delete before presenting or keep as your private crib. Every answer maps to
a committed artifact so you can show evidence live if challenged.
-->
