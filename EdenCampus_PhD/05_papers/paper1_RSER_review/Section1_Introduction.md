# Section 1 — Introduction

**Paper 1 (RSER):** *From passive estates to flexible generator energy systems:
a systematic review of business parks in the United Kingdom's electricity markets*

**Section target:** ~1,200 words. Purpose (per skeleton): install the spine —
structural fit, institutional invisibility, and the objective-function trap.

---

> **DRAFTING CONVENTIONS** — `[REF: ...]` = citation to add in EndNote (RSER
> numeric style); `[VERIFY: ...]` = figure to confirm before submission. FES 2025
> figures below are VERIFIED against the NESO source (see
> `FES2025_VERIFIED_FIGURES.md`) unless marked `[VERIFY]`.

---

## 1.1 Context and motivation

Great Britain's electricity system is being re-architected around flexibility. As
the system decarbonises, the National Energy System Operator (NESO) projects that
balancing a renewables-dominated grid will depend on large and growing volumes of
flexibility drawn from a portfolio of sources — distributed storage, electric
vehicles, demand-side response, and shiftable industrial and commercial load. In
its *Future Energy Scenarios 2025* (FES 2025), NESO finds that total storage
capacity rises from 10 GW in 2024 to between 38 and 96 GW by 2050 across its
pathways, and that electric vehicles, through smart charging and vehicle-to-grid,
"could be the largest source of flexibility capacity across supply and demand,
providing 51 GW at peak" [REF: NESO FES 2025]. On the demand side, FES 2025
estimates that improvements to building and appliance efficiency could cut
electricity demand by up to 127 TWh — an 18% reduction, from 694 TWh to 567 TWh —
by 2050 [REF: NESO FES 2025]. Flexibility is no longer a marginal system service;
it is a structural requirement of the net-zero transition.

Crucially, FES 2025 names industry and commercial activity as part of this
flexibility resource, noting that "industry and commercial can also offer
flexibility in shifting non-time critical demand," including thermal storage for
high-temperature and cooling loads [REF: NESO FES 2025]. Yet the commercial-estate
scale at which much of this load actually sits — the business park — is almost
entirely absent from the way this flexibility is enumerated, modelled, and
procured. This review addresses that gap.

## 1.2 The structural fit between business parks and system flexibility

UK business parks are, in aggregate, a materially significant electrical load and
a latent flexibility resource. They concentrate the very load types FES identifies
as flexible — workplace EV charging, HVAC and cooling, refrigeration, and process
demand — behind shared or coordinated infrastructure, often with substantial
rooftop area suited to embedded generation and space for behind-the-meter storage
[REF: commercial demand / estate energy literature]. In principle, a business park
is well positioned to make the transition the title of this review describes: from
a *passive estate* that draws power to a *flexible generator* that provides
storage, generation, and demand-side services to the system.

This structural fit matters because the commercial building stock has decarbonised
slowly. Commercial-sector emissions are reported to have risen since 1990, in
contrast with sharp reductions achieved in the public sector [VERIFY: commercial
emissions +5% since 1990 vs public sector −47% — confirm against the DESNZ /
BEIS greenhouse-gas or building-emissions statistics before stating]. If accurate,
this underlines both the scale of the opportunity and the inadequacy of current
approaches to unlocking it.

## 1.3 Institutional invisibility

Despite this fit, the business park is institutionally invisible in the datasets
and market structures that govern flexibility. There is no statutory UK definition
of a business park and no register that enumerates them (Section 2); they must be
inferred by triangulating valuation, energy, and network-capacity data
(Section 4). They are not a recognised participant category in most flexibility
procurement, and the routes that do exist fit the different park types unevenly
(Section 6). A resource that FES implicitly relies upon is therefore neither
counted nor systematically enabled — an invisibility this review argues is a
barrier in its own right.

## 1.4 The objective-function trap

A further, subtler barrier emerges once estate-scale flexibility is modelled
rather than merely described. Optimisation frameworks that minimise operational
cost — the standard basis for dispatch and investment analysis — do not
necessarily deliver the system outcomes flexibility is meant to provide.
Cost-minimising dispatch can, for example, *increase* peak grid imports when
low-cost electrified heat is added, because the objective rewards cheap energy at
the point of use rather than system-beneficial peak reduction [REF: Paper 2 /
present authors' modelling]. This "objective-function trap" — the gap between what
a cost-minimising model optimises and what the flexibility transition requires —
recurs throughout the review and is developed as a cross-cutting finding in
Section 7. It also motivates the empirical, multi-vector modelling of a
representative estate that this review sets up as its successor work.

## 1.5 Aim, scope, and contribution

Against this backdrop, the review has three aims: (i) to establish, empirically,
what UK business parks are and how they differ (a data spine, definition, and
typology, Sections 2 and 4); (ii) to assess, across seven literature streams and
the live market-access stack, how far business parks are recognised and enabled as
flexibility providers (Sections 5 and 6); and (iii) to surface the cross-cutting
barriers — including institutional invisibility and the objective-function trap —
that stand between their latent capability and realised system value (Section 7),
before setting a research agenda (Section 8).

The contribution is threefold: the first systematic characterisation of the UK
business-park landscape as a flexibility resource mapped to the FES flexibility
categories; a structured review of the evidence and market routes at estate scale;
and the identification of practitioner- and policy-relevant barriers, motivating
the estate-scale modelling that follows. The review is GB-weighted, with Northern
Ireland treated as a structured comparator, and is implemented with open,
reproducible sources throughout.

---

## Notes for the researcher (not for submission)

- **Verified FES figures used:** 127 TWh/18%, 51 GW EV/V2G, 10→38–96 GW storage —
  all confirmed against FES 2025 (see FES2025_VERIFIED_FIGURES.md). Safe to cite.
- **[VERIFY] items:** the "batteries 23–27 GW / LDES 4–6 GW / consumer-led 10–12 GW
  by 2030" figures from the skeleton are NOT yet confirmed — locate in the FES 2025
  Data Workbook or drop. The commercial-emissions +5%/−47% claim needs a DESNZ/BEIS
  source. Do not state either unverified.
- **Objective-function trap (1.4):** the concrete +peak-import result comes from
  your Eden Campus modelling — and recall that figure is tariff-dependent (energy-only
  tariff shows the penalty; a capacity charge removes it). Frame Section 1 to promise
  the finding, and let Section 7 present it with the corrected, reconciled numbers.
- **Word count:** ~1,150 words as drafted — within the 1,200 target. Trim 1.2 or 1.3
  if references push it over.
- **Consistency:** 1.5 promises a typology "mapped to the FES flexibility
  categories" — that is delivered by Section 4.3. Keep the two aligned.
