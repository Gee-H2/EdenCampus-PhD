# Section 7 — Cross-Cutting Barriers and the Objective-Function Trap

**Paper 1 (RSER)** · Target: ~1,700 words · Output: Fig. 3 (barrier × type heatmap)
Purpose (skeleton): synthesis, pivot, and honest bounds.

> Conventions: `[REF]` = citation; numbers from the authors' Eden Campus modelling
> are the CORRECTED, reconciled figures (see EdenCampus-PhD repo — annual demand
> 2,401 MWh; the peak-import result is tariff-dependent). Do NOT reuse the
> pre-correction figures from the skeleton.

---

## 7.1 What the streams share

The seven streams (Section 5) and the market map (Section 6) converge on a common
structure. The technical capability of coordinated estates to provide flexibility
is established; the market routes exist and are maturing; enabling governance forms
exist in adjacent domains. What is consistently missing is the treatment of the UK
business park as a *coordinated, multi-vector, market-participating flexibility
provider* — and, beneath that, three cross-cutting barriers that recur regardless
of stream: **institutional invisibility** (no definition, no register, no
participant category), **governance fragmentation** (the landlord–tenant split and
multi-MPAN friction), and a subtler modelling barrier developed below.

## 7.2 The bivalence result

The authors' own estate-scale modelling of a representative innovation campus (Eden
Campus, Type T3) — reported in full in the successor paper and summarised here —
illustrates the cross-cutting barriers concretely. Across a five-configuration
comparison (PV-only baseline S0 through full hybrid S4), storage and multi-vector
integration raise the annual solar fraction from **31.8% (S0) to 42.7% (S4)** and
CO2 savings from **178.0 to 238.8 t/yr** [REF: authors' modelling]. So far, the
result is unambiguously positive.

The bivalence appears in the peak-demand dimension, and it is **tariff-dependent** —
a nuance central to the argument. Under an **energy-only tariff**, cost-minimising
dispatch drives peak grid imports *above* the unstored baseline by approximately
**35%** in the heat-pump scenarios (S2 and S4), because electrified heat is
dispatched on cheap energy without regard to system peak [REF: authors' modelling].
Under a **capacity/demand charge** representative of real UK commercial billing,
the same optimisation instead *reduces* the peak — by up to ~40% in the hybrid
case — because the objective now values peak reduction [REF]. The identical
physical system yields opposite peak outcomes depending only on the tariff signal.

*(Note for the author: the skeleton's "+32.1% in both S2 and S4 against −1.4% in
S1 and S3, identical penalty with and without a battery" describes the
energy-only-tariff case from the pre-correction model. Use the corrected,
tariff-contrasted framing above, and cite the reconciled figures. The
marginal-abatement-cost comparison — S1→S4 ~£X/tCO2 against a UK ETS price of
~£XX/tCO2 — must be recomputed from the corrected costs before it is stated
[DATA].)*

## 7.3 The objective-function trap

The bivalence result generalises to a methodological finding this review terms the
**objective-function trap**: a cost-minimising optimisation delivers the outcomes
that the objective rewards, which are not necessarily the outcomes the flexibility
transition requires. When the objective sees only energy cost, system-beneficial
peak reduction is not procured — and may be actively undermined — even by an estate
physically capable of providing it. The implication is twofold: (i) for modellers,
the objective function must encode the system service being sought (a capacity
charge, a peak signal) or the model will mis-specify the estate's value; and
(ii) for market designers, the tariff/product signal is what turns latent estate
capability (Section 4.3) into realised system benefit. The trap is why capability
and market signal must be analysed together, and why a business park's flexibility
value cannot be read off technical potential alone.

## 7.4 The model–shadow–twin capability ladder as a market precondition

Realising estate flexibility also requires a data and control capability that
Section 5's D7 stream frames as a ladder: a static **model**, a data-connected
**shadow**, and a fully operational **digital twin** [REF]. This review argues the
ladder is a *market precondition*: participation in the products of Section 6
(baselining for DFS, dispatch for BM/VLP, verification for local flexibility)
requires at least shadow-level, and often twin-level, capability. Estates without
it cannot participate regardless of physical potential — a further reason the
business-park flexibility resource remains latent.

## 7.5 Limitations and honest bounds

This review's bounds are stated plainly:
- **Single-estate empirical basis** — the modelling evidence draws on one T3
  exemplar; transferability to T1/T2/T5 is argued, not demonstrated, and is a task
  for the research agenda (Section 8) [REF].
- **Self-citation circularity** — the review sets up the authors' own successor
  work; the self-citation management of Section 3.6 mitigates but does not
  eliminate this, and the pivot to Eden Campus is a T3 *representative*, not a
  claim of generality.
- **Clustering estimation** — business-park identification (Section 4) is a modelled
  inference from valuation data, carrying uncertainty in counts and boundaries.
- **GB weighting** — the analysis is GB-centred with NI as a comparator; the
  jurisdictional asymmetry in data and market structures limits UK-wide claims.
- **Synthetic demand** — the empirical exemplar's demand profile is currently a
  representative synthetic profile, not metered data; conclusions on absolute
  magnitudes are provisional pending measured data [REF].

Figure 3 will present a barrier × type heatmap, showing how the three cross-cutting
barriers (invisibility, fragmentation, objective-function/data-capability) fall
across T1–T5.

---

## Notes for the researcher (not for submission)

- **Use the corrected Eden Campus numbers** (2,401 MWh; tariff-dependent peak
  result; recomputed MAC). The skeleton's figures predate the model corrections —
  do not reuse them. See the EdenCampus-PhD repo reconciliation notes.
- The MAC figure (£/tCO2 vs UK ETS ~£49) is a strong rhetorical point but MUST be
  recomputed from corrected costs before stating [DATA].
- ~1,150 words; expand 7.1 and 7.4 to reach ~1,700.
