# Section 4 — The UK Business-Park Landscape and Typology

**Paper 1 (RSER):** *From passive estates to flexible generator energy systems:
a systematic review of business parks in the United Kingdom's electricity markets*

**Section target:** ~2,300 words · Output: Table 3 (typology matrix)
**Role in paper:** the original empirical contribution — establishes *what a UK
business park is, how many exist, and how they differ* as the evidentiary basis
for the stream-by-stream review (Section 5) and the market-access map (Section 6).

---

> **DRAFTING CONVENTIONS**
> - `[REF: ...]` = a factual claim requiring a citation. Find the source and add
>   it in EndNote (RSER numeric citation-order style). **Do not leave any [REF] in
>   the submitted version.**
> - `[DATA: ...]` = a specific statistic (park count, floor area, capacity) that
>   must be verified against the named dataset before it can be stated. Placeholder
>   values are marked `≈X` and must be replaced with queried figures.
> - `[CHECK: ...]` = a factual/legal detail to confirm.
> These markers exist so nothing is asserted as verified when it is not.

---

## 4.1 A data spine for an institutionally invisible asset class

The United Kingdom has no statutory register of business parks. Unlike dwellings,
which are enumerated in the census, or grid-connected generators, which appear in
connection registers, a "business park" is not a category any single authority
records. The asset class is therefore *institutionally invisible*: it is
economically significant yet absent from the datasets that ordinarily anchor
energy-system analysis [REF: prior literature noting the absence of estate-level
energy data]. Characterising it empirically requires assembling a *data spine* —
a set of independently maintained registers that, triangulated, allow business
parks to be identified, sized, and located.

This section assembles that spine from nine sources spanning valuation, energy
consumption, network capacity, and scenario planning across the three GB
jurisdictions and Northern Ireland.

**Valuation and property registers.** The primary means of identifying commercial
estates is non-domestic rating data. In England and Wales, the Valuation Office
Agency (VOA) rating list classifies hereditaments by Special Category (SCAT)
codes, several of which map to business-park uses (offices, warehouses, light
industrial units) [REF: VOA rating manual / SCAT code documentation]. In Scotland,
the equivalent function is served by the Scottish Assessors' valuation roll
[REF: Scottish Assessors Association]; in Northern Ireland, by Land & Property
Services (LPS) and its Valuation List [REF: LPS NI]. These registers do not label
"business parks" as such, so estates must be inferred from spatial clustering of
compatible hereditaments under shared or coordinated management — the operational
definition established in Section 2.

**Energy-consumption data.** The National Energy Efficiency Data-Framework
(ND-NEED) provides non-domestic energy-consumption statistics that allow estate
demand to be characterised at aggregate level [REF: DESNZ ND-NEED]. Non-domestic
Energy Performance Certificate (EPC) registers add building-level fabric and
intensity data across the jurisdictions [REF: EPC register — England/Wales;
Scotland; NI]. Together these bound the electrical and thermal demand of the asset
class without requiring access to (commercially sensitive) metered data.

**Network-capacity data.** Distribution Network Operator (DNO) Embedded Capacity
Registers (ECRs), published under the ENA Open Networks programme, record
connected and accepted generation and storage at each grid supply point
[REF: ENA Open Networks; DNO ECR]. These reveal where estates already host — or
have applied to host — distributed generation and storage, a direct indicator of
flexibility potential. The DESNZ Heat Networks Planning Database locates existing
and planned heat networks, several of which serve business parks and campuses
[REF: DESNZ Heat Networks Planning Database].

**Scenario and planning data.** Sub-national energy scenarios provide the forward
view. SSEN's Distribution Future Energy Scenarios (DFES) for the North of Scotland,
reported at local-authority resolution, cover Fife — the region containing the
Eden Campus exemplar used later in this review [REF: SSEN DFES North of Scotland].
(Note: Fife is in SSEN/SHEPD licence area, not SPEN — see
DATA_SPINE_ACCESS_VERIFICATION.md.) For the Northern Ireland
comparator, SONI's Tomorrow's Energy Scenarios workbook provides the equivalent
projection [REF: SONI TES].

**Triangulation and limitations.** No single source is authoritative for
business-park identification; each was designed for another purpose. The spine
therefore works by triangulation — valuation registers to locate and delineate
estates, energy and EPC data to size them, capacity registers to assess their
network context, and scenarios to bound their trajectory. Two limitations must be
stated plainly. First, the mapping from SCAT/roll codes to "business park" is a
modelled inference, not a recorded fact, and carries clustering-estimation
uncertainty [CHECK: quantify approach to clustering — spatial threshold, unit
count]. Second, coverage is uneven across jurisdictions: GB registers are more
granular and openly published than NI equivalents, so the analysis is
GB-weighted, with Northern Ireland treated as a structured comparator rather than
a like-for-like case [REF: note on data-availability asymmetry].

---

## 4.2 A five-type typology of UK business parks

Triangulating the data spine against the operational definition (Section 2) yields
five business-park types, distinguished by ownership and governance structure,
dominant use, demand profile, and — critically for this review — their fit with
electricity-market flexibility routes. The typology is summarised in Table 3;
each type is described below with a named UK exemplar.

### T1 — Multi-let office park
*Exemplar: Edinburgh Park, Edinburgh* [REF/CHECK: Edinburgh Park profile].
Multiple separately occupied office buildings under single or coordinated estate
management, typically with shared infrastructure (parking, district services,
common landlord). Demand is daytime-dominated and weekday-weighted, closely
correlated with occupancy, and increasingly shaped by EV charging and
office-cooling loads [REF: commercial office demand profiles]. The landlord–tenant
split and multiple MPANs are the defining flexibility challenge: the party that
could contract flexibility (the landlord) often does not hold the supply
relationship (the tenant) [REF: split-incentive literature].

### T2 — Industrial and logistics estate
*Exemplar: Eurocentral, North Lanarkshire* [REF/CHECK: Eurocentral profile].
Warehousing, distribution, and light-manufacturing units. Demand is more
continuous than T1 (shift patterns, refrigeration, process loads) and often
larger per unit, giving higher connection capacities and, potentially, greater
absolute flexibility. Rooftop area on large-footprint sheds is a significant
latent PV resource [REF: warehouse rooftop PV potential]. Governance is more
fragmented where units are individually owned.

### T3 — Innovation campus
*Exemplars: Eden Campus, Fife; Michelin Scotland Innovation Parc, Dundee;
Catalyst, Belfast* [REF/CHECK: campus profiles]. Research-and-development and
knowledge-economy campuses, frequently university- or anchor-institution-led,
with coordinated single management and an explicit decarbonisation mandate. This
governance coherence makes T3 the most tractable type for integrated flexibility
and multi-vector energy systems — and is why Eden Campus serves as the modelling
exemplar whose results are synthesised in Section 7. Demand combines office,
laboratory, and pilot-scale process loads, often with significant thermal demand
suited to heat-pump and thermal-storage integration [REF: campus microgrid
literature].

### T4 — Retail and leisure park
*Defined out of scope.* Retail and leisure parks meet the physical criteria
(clustered units, shared infrastructure) but are excluded on governance grounds:
their tenant mix, lease structures, and consumer-facing operating patterns place
them closer to the retail-property literature than to the coordinated-estate
flexibility question this review addresses [REF: justification — governance basis
for exclusion]. They are retained in Table 3 only to make the exclusion explicit.

### T5 — Single-owner corporate campus
*Exemplar: [CHECK: named single-owner corporate campus — e.g. a corporate HQ
campus].* A single occupier owning and operating the whole estate (corporate
headquarters, large single-tenant campuses). Governance is maximally coherent —
one owner, one balance sheet, one supply relationship — removing the split-incentive
barrier entirely, but the type is comparatively rare and its lessons may not
transfer to the multi-tenant majority [REF: corporate campus energy management].

---

## Table 3 — Typology of UK business parks

| Type | Label | Exemplar | Ownership / governance | Dominant use | Demand profile | Flexibility-route fit |
|---|---|---|---|---|---|---|
| **T1** | Multi-let office park | Edinburgh Park | Single/coordinated landlord; multi-tenant | Offices | Daytime, weekday-weighted | Moderate — limited by landlord–tenant split, multi-MPAN |
| **T2** | Industrial & logistics | Eurocentral | Mixed; often individually owned units | Warehousing, light industry | More continuous; higher per-unit capacity | High latent (rooftop PV, larger loads); fragmented governance |
| **T3** | Innovation campus | Eden Campus; MSIP; Catalyst | Anchor-institution-led; coordinated single mgmt | R&D, office, pilot process | Mixed electrical + significant thermal | **High** — governance coherence enables multi-vector integration |
| **T4** | Retail & leisure park | *(defined out)* | Retail landlord; consumer-facing tenants | Retail, leisure | Evening/weekend-weighted | Excluded on governance grounds |
| **T5** | Single-owner corporate campus | [CHECK exemplar] | Single owner-occupier | Corporate HQ / single tenant | Occupier-specific | High per-site, but rare; transferability limited |

*[DATA: add an estimated population/count column per type once the VOA/Assessors/
LPS clustering has been run — e.g. "≈X estates GB-wide". Do not state counts until
queried.]*

---

## 4.3 Mapping the typology to the Future Energy Scenarios flexibility categories

The value of this typology for the present review is not descriptive but
functional: it allows each business-park type to be read as a *latent provider*
of the specific flexibility that the National Energy System Operator's Future
Energy Scenarios (FES 2025) identifies as necessary for a secure, low-cost net-zero
system [REF: NESO FES 2025]. FES frames flexibility as a system requirement met by
a portfolio of sources — distributed storage, consumer-led and demand-side
flexibility, electric-vehicle smart charging, and industrial-and-commercial (I&C)
demand shifting — growing sharply to 2030 and 2050 [DATA: insert the FES 2025
figures from the data workbook — e.g. batteries ≈X GW, LDES ≈X GW, consumer-led
flexibility ≈X GW by 2030; verify each against the FES 2025 workbook before
stating]. Business parks are largely absent from the way this flexibility is
currently enumerated and procured, yet each type in the typology maps onto one or
more of these FES categories.

The mapping is developed here at the level of *physical and governance capability*
— what flexibility each type can, in principle, provide. The distinct question of
*which market routes allow that flexibility to be monetised* is deferred to
Section 6, and the two should not be conflated: capability is necessary but not
sufficient for participation.

- **Demand shifting (I&C flexibility).** All park types carry shiftable load
  (HVAC, refrigeration, process, EV charging), but the shiftable *fraction* and
  the governance ability to act on it differ. T3 and T5, with coordinated single
  management, can commit shiftable load directly; T1 and T2 are constrained by the
  landlord–tenant split and multi-MPAN fragmentation [REF: I&C DSR potential].
- **Distributed storage.** Behind-the-meter batteries and thermal storage align
  with the FES distributed-storage category. T2 (large rooftops, space for
  containerised BESS) and T3 (mandate plus multi-vector demand suited to thermal
  storage) have the highest latent storage potential.
- **Consumer-led / demand-side flexibility.** FES's consumer-led category maps to
  aggregated, controllable estate loads. Coordinated estates (T3, T5) are the
  natural aggregation unit; fragmented estates require an aggregator to overcome
  the split-incentive barrier.
- **EV smart charging.** FES identifies EVs as the single largest flexibility
  source. Office and campus parking (T1, T3, T5) concentrates workplace charging —
  a daytime, solar-coincident flexibility resource of direct FES relevance.
- **Embedded generation.** Rooftop and ground-mount PV (T2, T3) positions parks as
  distributed generators, not merely flexible loads — the "passive estate to
  flexible generator" transition of the paper's title.

**Table 3b — Business-park types as FES flexibility providers** (qualitative
capability: ●●● high, ●● moderate, ● low; ratings are the authors' assessment
pending the empirical characterisation and must be justified against the stream
evidence in Section 5).

| Type | Demand shifting (I&C) | Distributed storage | Consumer-led / DSR | EV smart charging | Embedded generation | Overall FES-flexibility fit |
|---|---|---|---|---|---|---|
| **T1** Multi-let office | ●● | ● | ●● | ●●● | ● | Moderate — high EV potential, governance-limited |
| **T2** Industrial & logistics | ●●● | ●●● | ●● | ● | ●●● | High — storage + generation + process shifting |
| **T3** Innovation campus | ●●● | ●●● | ●●● | ●● | ●● | **Highest — coordinated multi-vector flexibility** |
| **T4** Retail & leisure | ●● | ● | ●● | ●● | ● | Excluded on governance grounds |
| **T5** Single-owner campus | ●●● | ●● | ●●● | ●● | ●● | High per-site; limited transferability |

The mapping supports the review's central proposition: the flexibility the FES
requires is, in substantial part, flexibility that UK business parks are
structurally positioned to supply. It also identifies *which* types are most
ready — T2 and T3 on capability grounds, with T3 distinguished by the governance
coherence needed to act on that capability across multiple vectors. This
motivates the stream-by-stream review (Section 5), which tests how far the
existing literature has recognised and quantified this potential, and the
market-access map (Section 6), which examines whether the routes to monetise it
actually fit these types.

*[REF/DATA discipline: every ● rating must be defensible from Section 5 stream
evidence or the empirical characterisation; the FES category figures must be
taken from the FES 2025 data workbook, not from secondary summaries.]*

---

## Notes for the researcher (not for submission)

**Priority order to complete this section:**
0. **Verify FES 2025 flexibility figures** against the NESO FES 2025 data workbook
   (batteries/LDES/consumer-led/EV/I&C shifting GW by 2030 and 2050). These anchor
   the Section 4.3 mapping and Section 1 — do not state any GW figure unverified.
1. **Confirm data access.** Establish which spine datasets you can actually query
   (VOA SCAT, ECRs, ND-NEED, EPC, Heat Networks DB are the key ones). This
   determines whether Table 3 can carry real population counts or stays qualitative.
2. **Fill the exemplar gaps.** T5 needs a named exemplar; verify Edinburgh Park,
   Eurocentral, and the T3 campuses against a public profile source.
3. **Resolve every [REF].** ~15–25 citations sit in this section; add them in
   EndNote. Key clusters: the data-source documentation (each register), the
   split-incentive literature, and the campus-microgrid literature.
4. **Cross-link Section 7.** The Eden Campus modelling numbers cited in the
   skeleton's Section 7.2 (solar fraction 31.8%→42.7%, CO₂ 178→238.8 t/yr, the
   peak-import result) come from your PyPSA work — note that those figures were
   corrected during model verification (see the EdenCampus-PhD repo: annual demand
   2,401 MWh not 1,816; and the "+32% peak" is tariff-dependent). Section 7 must
   use the corrected, reconciled figures.

**Consistency with Section 2:** this section assumes Section 2 has established the
operational definition (≥5 separately occupied units; ≥10,000 m² GIA or ≥2 ha;
shared infrastructure; single or coordinated management). If that definition
changes, the T1–T5 boundaries and the clustering approach here must change with it.
