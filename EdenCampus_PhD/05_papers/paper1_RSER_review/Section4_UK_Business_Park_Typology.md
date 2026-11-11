# Section 4 — The UK Business-Park Landscape and Typology

**Paper 1 (RSER):** *From passive estates to flexible generator energy systems:
a systematic review of business parks in the United Kingdom's electricity markets*

**Section target:** ~2,300 words · Output: Table 3 (typology matrix)
**Role in paper:** the original empirical contribution — establishes *what a UK
business park is, how many exist, and how they differ* as the evidentiary basis
for the stream-by-stream review (Section 5) and the market-access map (Section 6).

---

> **DRAFTING CONVENTIONS (updated 11 Nov 2026)**
> - Citations are now numbered `[n]` in order of first appearance and listed under
>   "References for Section 4" below. The numbers are **section-local**: EndNote
>   will renumber them in RSER citation order across the whole paper.
> - Every reference was located and its bibliographic details checked online on
>   11 Nov 2026. That confirms each source exists and is on-topic; it does not
>   replace reading it. See "Read before submission" in the notes.
> - **One marker remains open**: the `[DATA]` park-count column under Table 3,
>   which cannot be filled until the clustering is run. Nothing else in the
>   submission text carries a placeholder.

---

## 4.1 A data spine for an institutionally invisible asset class

The United Kingdom has no statutory register of business parks. Unlike dwellings,
which are enumerated in the census, or grid-connected generators, which appear in
connection registers, a "business park" is not a category any single authority
records. The asset class is therefore *institutionally invisible*: it is
economically significant yet absent from the datasets that ordinarily anchor
energy-system analysis. National non-domestic stock data are organised around
premises and buildings rather than estates [1], and an earlier classification of
techno-economic energy models found none tailored to the business-park scale [2].
Characterising the asset class empirically requires assembling a *data spine* —
a set of independently maintained registers that, triangulated, allow business
parks to be identified, sized, and located.

This section assembles that spine from nine sources spanning valuation, energy
consumption, network capacity, and scenario planning across the three GB
jurisdictions and Northern Ireland.

**Valuation and property registers.** The primary means of identifying commercial
estates is non-domestic rating data. In England and Wales, the Valuation Office
Agency (VOA) rating list classifies hereditaments by Special Category (SCat)
codes [3,4], several of which map to business-park uses (offices, warehouses,
light industrial units) — for example SCat 096, "Factories, Workshops and
Warehouses" [4]. In Scotland, the equivalent function is served by the valuation
roll maintained by the Scottish Assessors, searchable Scotland-wide through the
Scottish Assessors Association portal [5]; in Northern Ireland, by the
Non-Domestic Valuation List maintained by Land & Property Services (LPS), which
covers some 75,000 non-domestic properties [6]. These registers do not label
"business parks" as such, so estates must be inferred from spatial clustering of
compatible hereditaments under shared or coordinated management — the operational
definition established in Section 2.

**Energy-consumption data.** The Non-Domestic National Energy Efficiency
Data-Framework (ND-NEED) links the rating list to metered electricity and gas
consumption, allowing estate demand to be characterised at aggregate level; it
covers England and Wales only [7]. Non-domestic Energy Performance Certificate
(EPC) data add building-level fabric and intensity information, held in three
separately governed registers: an open-data register for England and Wales [8], a
Scottish register with quarterly open extracts [9], and a Northern Ireland
register operated on the England-and-Wales platform under the control of the
Northern Ireland Executive [10]. Together these bound the electrical and thermal
demand of the asset class without requiring access to (commercially sensitive)
metered data.

**Network-capacity data.** Embedded Capacity Registers (ECRs) were developed
through the ENA Open Networks programme and made a requirement on distribution
network operators (DNOs) by code modification DCP350 in 2020 [11]. Each DNO's
register now records generation and storage of 50 kW and above that is connected,
or accepted to connect, to its network, updated monthly [11,12]. These reveal
where estates already host — or have applied to host — distributed generation and
storage, a direct indicator of flexibility potential. The DESNZ Heat Networks
Planning Database tracks district and communal heat-network projects across the
UK through the planning system, allowing schemes on or adjacent to business parks
and campuses to be identified [13].

**Scenario and planning data.** Sub-national energy scenarios provide the forward
view. SP Energy Networks' Distribution Future Energy Scenarios (DFES) for the SP
Distribution licence area — within which Fife and the Eden Campus exemplar lie —
report forecasts at grid-supply-point and primary-substation level, with key
metrics by local authority, and are aligned with the FES 2025 pathway framework
[14]. For the Northern Ireland comparator, Tomorrow's Energy Scenarios 2023,
published jointly by SONI and EirGrid, provides the equivalent projection to 2050
[15].

**Triangulation and limitations.** No single source is authoritative for
business-park identification; each was designed for another purpose. The spine
therefore works by triangulation — valuation registers to locate and delineate
estates, energy and EPC data to size them, capacity registers to assess their
network context, and scenarios to bound their trajectory. Three limitations must
be stated plainly. First, the mapping from SCat/roll codes to "business park" is a
modelled inference, not a recorded fact. Estates are delineated by density-based
spatial clustering (DBSCAN) of geocoded hereditaments in compatible categories,
with a minimum cluster size of five hereditaments (criterion 1 of the operational
definition), a neighbourhood radius of 150 m, and retention only of clusters
meeting the scale threshold (≥10,000 m² GIA or ≥2 ha); candidate clusters are then
screened for shared infrastructure and coordinated management (criteria 3 and 4).
The estate count is sensitive to the radius, and that sensitivity is to be
reported across 100–250 m. Second, the sizing sources are partial: ND-NEED is
aggregated rather than per-estate and excludes Scotland and Northern Ireland [7],
and the ECRs omit assets below 50 kW, so smaller behind-the-meter installations
are invisible [12]. Third, coverage is uneven across jurisdictions: valuation and
EPC data sit in three separately governed sets of registers, each with its own
classification scheme and access route [3–6,8–10]. The analysis is therefore
GB-weighted — and, for metered consumption, weighted towards England and Wales —
with Northern Ireland treated as a structured comparator rather than a
like-for-like case.

---

## 4.2 A five-type typology of UK business parks

Triangulating the data spine against the operational definition (Section 2) yields
five business-park types, distinguished by ownership and governance structure,
dominant use, demand profile, and — critically for this review — their fit with
electricity-market flexibility routes. The typology is summarised in Table 3;
each type is described below with a named UK exemplar.

### T1 — Multi-let office park
*Exemplar: Edinburgh Park, Edinburgh* [16].
Multiple separately occupied office buildings under single or coordinated estate
management, typically with shared infrastructure (parking, district services,
common landlord). Demand is daytime-dominated and weekday-weighted, closely
correlated with occupancy [17], predominantly electrical [18], and increasingly
shaped by EV charging and office-cooling loads. The landlord–tenant split and
multiple MPANs are the defining flexibility challenge: the party that could
contract flexibility (the landlord) often does not hold the supply relationship
(the tenant) [19,20].

### T2 — Industrial and logistics estate
*Exemplar: Eurocentral, North Lanarkshire* [21].
Warehousing, distribution, and light-manufacturing units. Demand is more
continuous than T1 (shift patterns, refrigeration, process loads) and often
larger per unit, giving higher connection capacities and, potentially, greater
absolute flexibility. Rooftop area on large-footprint sheds is a significant
latent PV resource: one industry study estimates that the largest fifth of UK
warehouses offer about 75 million m² of roof, enough for up to 15 GW of rooftop
solar [22]. Governance is more fragmented where units are individually owned.

### T3 — Innovation campus
*Exemplars: Eden Campus, Fife [23,24]; Michelin Scotland Innovation Parc, Dundee
[25]; Catalyst, Belfast [26].* Research-and-development and knowledge-economy
campuses, frequently university- or anchor-institution-led, with coordinated
single management and an explicit decarbonisation mandate. This governance
coherence makes T3 the most tractable type for integrated flexibility and
multi-vector energy systems — and is why Eden Campus serves as the modelling
exemplar whose results are synthesised in Section 7. Eden Campus already combines
a biomass energy centre and district-heating network with a solar array of about
1 MW and battery storage [23,24]. Demand combines office, laboratory, and
pilot-scale process loads, often with significant thermal demand suited to
heat-pump and thermal-storage integration [27,28].

### T4 — Retail and leisure park
*Defined out of scope.* Retail and leisure parks meet the physical criteria
(clustered units, shared infrastructure) but are excluded on governance grounds:
their tenant mix, lease structures, and consumer-facing operating patterns place
them closer to the retail-property literature [29,30] than to the
coordinated-estate flexibility question this review addresses (Section 2.4). They
are retained in Table 3 only to make the exclusion explicit.

### T5 — Single-owner corporate campus
*Exemplar: NatWest Group headquarters campus, Gogarburn, Edinburgh* [31], whose
car park hosts 264 EV-charging sockets [32]. A single occupier owning and
operating the whole estate (corporate headquarters, large single-tenant
campuses). Governance is maximally coherent — one owner, one balance sheet, one
supply relationship — so the split-incentive barrier that lease terms create in
tenanted buildings [33] does not arise in the same form, although energy
management in owner-occupied property still depends on relationships within the
organisation [34]. The type is comparatively rare and its lessons may not
transfer to the multi-tenant majority.

---

## Table 3 — Typology of UK business parks

| Type | Label | Exemplar | Ownership / governance | Dominant use | Demand profile | Flexibility-route fit |
|---|---|---|---|---|---|---|
| **T1** | Multi-let office park | Edinburgh Park | Single/coordinated landlord; multi-tenant | Offices | Daytime, weekday-weighted | Moderate — limited by landlord–tenant split, multi-MPAN |
| **T2** | Industrial & logistics | Eurocentral | Mixed; often individually owned units | Warehousing, light industry | More continuous; higher per-unit capacity | High latent (rooftop PV, larger loads); fragmented governance |
| **T3** | Innovation campus | Eden Campus; MSIP; Catalyst | Anchor-institution-led; coordinated single mgmt | R&D, office, pilot process | Mixed electrical + significant thermal | **High** — governance coherence enables multi-vector integration |
| **T4** | Retail & leisure park | *(defined out)* | Retail landlord; consumer-facing tenants | Retail, leisure | Evening/weekend-weighted | Excluded on governance grounds |
| **T5** | Single-owner corporate campus | NatWest Gogarburn | Single owner-occupier | Corporate HQ / single tenant | Occupier-specific | High per-site, but rare; transferability limited |

*[DATA — OPEN: add an estimated population/count column per type once the
VOA/Assessors/LPS clustering has been run — e.g. "≈X estates GB-wide". Do not
state counts until queried.]*

---

## 4.3 Mapping the typology to the Future Energy Scenarios flexibility categories

The value of this typology for the present review is not descriptive but
functional: it allows each business-park type to be read as a *latent provider*
of the specific flexibility that the National Energy System Operator's Future
Energy Scenarios (FES 2025) identifies as necessary for a secure, low-cost net-zero
system [35]. FES frames flexibility as a system requirement met by a portfolio of
sources — distributed storage, consumer-led and demand-side flexibility,
electric-vehicle smart charging, and industrial-and-commercial (I&C) demand
shifting — that grows sharply to 2050. Across the four FES 2025 pathways, total
electricity storage capacity rises from 10 GW in 2024 to 38–96 GW in 2050, and
maximum vehicle-to-grid capacity from zero to 9–81 GW; in the Holistic Transition
pathway, electric vehicles (smart charging and vehicle-to-grid combined) supply
51 GW of flexibility at peak, the largest single source on either the supply or
the demand side [35]. FES 2025 also names industrial and commercial consumers
explicitly as flexibility providers, through shifting of non-time-critical
demand, thermal storage, and large-scale refrigeration [35]. Business parks are
largely absent from the way this flexibility is currently enumerated and
procured, yet each type in the typology maps onto one or more of these FES
categories.

The mapping is developed here at the level of *physical and governance capability*
— what flexibility each type can, in principle, provide. The distinct question of
*which market routes allow that flexibility to be monetised* is deferred to
Section 6, and the two should not be conflated: capability is necessary but not
sufficient for participation.

- **Demand shifting (I&C flexibility).** All park types carry shiftable load
  (HVAC, refrigeration, process, EV charging), but the shiftable *fraction* and
  the governance ability to act on it differ. T3 and T5, with coordinated single
  management, can commit shiftable load directly; T1 and T2 are constrained by the
  landlord–tenant split and multi-MPAN fragmentation [17,19].
- **Distributed storage.** Behind-the-meter batteries and thermal storage align
  with the FES distributed-storage category. T2 (large rooftops, space for
  containerised BESS) and T3 (mandate plus multi-vector demand suited to thermal
  storage) have the highest latent storage potential.
- **Consumer-led / demand-side flexibility.** FES's consumer-led category maps to
  aggregated, controllable estate loads. Coordinated estates (T3, T5) are the
  natural aggregation unit; fragmented estates require an aggregator to overcome
  the split-incentive barrier.
- **EV smart charging.** In the FES 2025 Holistic Transition pathway, EVs are the
  single largest source of flexibility capacity [35]. Office and campus parking
  (T1, T3, T5) concentrates workplace charging — a daytime, solar-coincident
  flexibility resource of direct FES relevance.
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

---

## References for Section 4

*Section-local numbering, in order of first citation. All web sources accessed
11 November 2026.*

[1] Steadman P, Evans S, Liddiard R, Godoy-Shimizu D, Ruyssevelt P, Humphrey D.
Building stock energy modelling in the UK: the 3DStock method and the London
Building Stock Model. Buildings and Cities 2020;1(1):100–19.
https://doi.org/10.5334/bc.52

[2] Timmerman J, Vandevelde L, Van Eetvelde G. Towards low carbon business park
energy systems: classification of techno-economic energy models. Energy
2014;75:68–80. https://doi.org/10.1016/j.energy.2014.05.092

[3] Valuation Office Agency. The Rating Manual. GOV.UK; last updated 5 April 2022.
https://www.gov.uk/government/publications/valuation-office-agency-rating-manual

[4] Valuation Office Agency. Non-domestic rating: SCat codes (28 August 2025).
https://assets.publishing.service.gov.uk/media/68b86369536d629f9c82aa54/2025-08-28_NDR_SCat_codes.pdf

[5] Scottish Assessors Association. The Valuation Roll. Scottish Assessors Portal.
https://www.saa.gov.uk/non-domestic-valuation/the-valuation-roll/

[6] Department of Finance (Northern Ireland), Land & Property Services. Valuation
lists. https://www.finance-ni.gov.uk/topics/valuation-lists

[7] Department for Energy Security and Net Zero. The Non-Domestic National Energy
Efficiency Data-Framework (England and Wales). Latest edition 2026 (covers
2012–2024); cite the latest at submission.
https://www.gov.uk/government/collections/non-domestic-national-energy-efficiency-data-framework-nd-need

[8] Ministry of Housing, Communities and Local Government. Energy Performance of
Buildings Data: England and Wales. https://epc.opendatacommunities.org

[9] Scottish Government. Scottish Energy Performance Certificate Register:
publicly available data extracts.
https://www.energycertificate.service.gov.scot/data-extracts

[10] Department for Levelling Up, Housing and Communities. Energy Performance of
Buildings Certificates: notes and definitions. GOV.UK.
https://www.gov.uk/energy-performance-of-buildings-certificates-notes-and-definitions

[11] Ofgem. DCP350 – Creation of Embedded Capacity Registers: decision.
1 July 2020.
https://www.ofgem.gov.uk/decision/dcp350-creation-embedded-capacity-registers

[12] Energy Networks Association. Open Networks WS2 P1: Embedded Capacity Register
(ECR) – implementation plan for inclusion of assets down to 50 kW.
22 December 2021. ENA resource library, https://www.energynetworks.org

[13] Department for Energy Security and Net Zero. Heat Networks Planning Database
(HNPD). Quarterly.
https://www.data.gov.uk/dataset/desnz-heat-networks-planning-database

[14] SP Energy Networks. Distribution Future Energy Scenarios: SP Distribution.
May 2026. https://www.spenergynetworks.co.uk/userfiles/file/SPD_DFES_2026.pdf

[15] EirGrid, SONI. Tomorrow's Energy Scenarios 2023: final report. 2024.
https://cms.eirgrid.ie/sites/default/files/publications/TES-2023-Final-Full-Report.pdf

[16] Edinburgh Park Management Ltd. Edinburgh Park: The Park.
https://edinburghpark.com/the-park

[17] Grünewald P, Torriti J. Demand response from the non-domestic sector: early
UK experiences and future opportunities. Energy Policy 2013;61:423–9.
https://doi.org/10.1016/j.enpol.2013.06.051

[18] Department for Business, Energy and Industrial Strategy. Building Energy
Efficiency Survey, 2014–15: overarching report. November 2016.
https://www.gov.uk/government/publications/building-energy-efficiency-survey-bees

[19] Axon CJ, Bright SJ, Dixon TJ, Janda KB, Kolokotroni M. Building communities:
reducing energy use in tenanted commercial property. Building Research &
Information 2012;40(4):461–72. https://doi.org/10.1080/09613218.2012.680701

[20] Janda KB, Bright S, Patrick J, Wilkinson S, Dixon TJ. The evolution of green
leases: towards inter-organizational environmental governance. Building Research &
Information 2016;44(5–6):660–74. https://doi.org/10.1080/09613218.2016.1142811

[21] North Lanarkshire Council. North Lanarkshire Local Development Plan: policy
document (adopted July 2022).
https://www.northlanarkshire.gov.uk/sites/default/files/2022-11/North%20Lanarkshire%20Local%20Development%20Plan.pdf

[22] Robinson L, Blacklaws K. Investment case for rooftop solar power in
warehousing. Delta-EE for the UK Warehousing Association; August 2022.
https://www.ukwa.org.uk/wp-content/uploads/2022/09/Investment-Case-for-Rootop-Solar-Power-in-Warehousing-August-2022.pdf

[23] University of St Andrews. Eden Campus: locate here.
https://innovation.st-andrews.ac.uk/about/locate/

[24] University of St Andrews. Energy and water.
https://www.st-andrews.ac.uk/sustainability/energy

[25] Scottish Development International. Michelin Scotland Innovation Parc (MSIP).
https://www.sdi.co.uk/invest/locations-for-your-business/commercial-properties-and-land/michelin-scotland-innovation-parc-msip

[26] Catalyst. Catalyst: science and technology hub, Northern Ireland.
https://wearecatalyst.org

[27] Muqeet HA, Munir HM, Javed H, Shahzad M, Jamil M, Guerrero JM. An energy
management system of campus microgrids: state-of-the-art and future challenges.
Energies 2021;14(20):6525. https://doi.org/10.3390/en14206525

[28] Alhawsawi EY, Salhein K, Zohdy MA. A comprehensive review of existing and
pending university campus microgrids. Energies 2024;17(10):2425.
https://doi.org/10.3390/en17102425

[29] Guy CM. Alternative-use valuation, open A1 planning consent, and the
development of retail parks. Environment and Planning A 1998;30:37–47.
https://doi.org/10.1068/a300037

[30] Thomas CJ, Bromley RDF, Tallon AR. Retail parks revisited: a growing
competitive threat to traditional shopping centres? Environment and Planning A
2004;36(4):647–66. https://doi.org/10.1068/a3683

[31] NatWest Group. Worldwide locations: our headquarters (Gogarburn, Edinburgh).
https://www.rbs.com/rbs/about/worldwide-locations.html

[32] Equans. Equans delivers one of the largest electric vehicle charging car park
installations in the UK at NatWest office. Case study.
https://jobs.equans.co.uk/case-studies/equans-delivers-one-largest-electric-vehicle-charging-car-park-installations-uk

[33] Kahn ME, Kok N, Quigley JM. Carbon emissions from the commercial building
sector: the role of climate, quality, and incentives. Journal of Public Economics
2014;113:1–12. https://doi.org/10.1016/j.jpubeco.2014.03.003

[34] Janda KB. Building communities and social potential: between and beyond
organizations and individuals in commercial properties. Energy Policy
2014;67:48–55. https://doi.org/10.1016/j.enpol.2013.08.058

[35] National Energy System Operator. Future Energy Scenarios: Pathways to Net
Zero (FES 2025). July 2025.
https://www.neso.energy/publications/future-energy-scenarios-fes

---

## Notes for the researcher (not for submission)

### What changed on 11 Nov 2026
- All citation and exemplar placeholders are resolved into 35 numbered references.
- The FES placeholder in 4.3 is filled with the 2050 figures already verified in
  `FES2025_VERIFIED_FIGURES.md`. The 2030 figures were dropped (see below).
- T5 now has an exemplar (NatWest Gogarburn). It was chosen to sit beside the
  other Scottish exemplars; swap it if you prefer another campus.
- The clustering method is now written out in 4.1.
- The in-text research note about SPEN being the Fife DNO was cut from 4.1; the
  evidence stays in `DATA_SPINE_ACCESS_VERIFICATION.md`.
- Limitations in 4.1 went from two to three (ECR 50 kW floor and ND-NEED
  aggregation added).
- The Heat Networks Planning Database is a real, quarterly, UK-wide planning
  tracker, not only the HNDU funding pipeline. The sentence now describes it as
  tracking projects through planning, and no longer asserts that several
  networks serve business parks.

### Still open — only you can close these
1. **Park counts (Table 3 `[DATA]`).** Needs the VOA/Assessors/LPS clustering to
   be run. No count has been stated anywhere. **Method is now built and tested**
   (`cluster_business_parks.py`); it is blocked only on obtaining the valuation
   data. England & Wales is a bulk download; **Scotland has no bulk download** —
   get a Fife extract via a supervisor/University introduction or a formal request
   to the Fife Assessor (draft: `DATA_REQUEST_fife_assessor.md`), or the
   Scotland-wide roll via the university's OS/PSGA (Digimap) licence. Keep raw data
   local (OS/Crown licence); commit only aggregated counts.
2. **Clustering radius.** The 150 m radius and the 100–250 m sensitivity range in
   4.1 are proposed values, not results. Minimum cluster size (5) and the scale
   threshold come from your Section 2 definition. Confirm or change the radius
   when you run it, and change "is to be reported" to past tense.
3. **Table 3b ratings.** Every ● must still be defensible from Section 5 stream
   evidence.

### Things found while checking that affect other files
- **ND-NEED covers England and Wales only.** It cannot size Eden Campus or any
  Scottish estate. You need a Scottish consumption source (DESNZ sub-national
  electricity and gas statistics cover Great Britain at local-authority level) or
  must say plainly that Scottish sizing rests on EPC and valuation data.
  (Recorded in DATA_SPINE_ACCESS_VERIFICATION.md, 7 Nov 2026.)
- **FES 2025 pathway names.** The three net-zero pathways are Holistic Transition,
  Electric Engagement, Hydrogen Evolution; the fourth is "Falling Behind" (NOT
  "Full-system Bridge" as earlier guessed). The 38 GW lower bound for 2050 storage
  is the Falling Behind value, which does not reach net zero; say so if a reviewer
  asks. (FES2025_VERIFIED_FIGURES.md corrected, 7 Nov 2026.)
- **2030 FES figures.** The skeleton's "batteries 23–27 GW, LDES 4–6 GW by 2030"
  do not match a trade-body summary of FES 2025 (REA members' brief: batteries
  20.5–25.2 GW, LDES 3–5.3 GW by 2030). Neither is verified against the FES
  Data Workbook, so no 2030 figure is stated. Section 1 uses the same numbers.
- **ND-NEED edition.** The 2026 edition is now on GOV.UK (covers 2012–2024).
  Cite the latest at submission.
- **Table numbering.** "Table 3b" probably needs its own number, which shifts
  Tables 4 and 5 in Sections 5 and 6.

### Read before submission (existence checked, content not read in full)
Your own worklist rule is not to cite anything you have not read. These are the
citations where the sentence leans on a reading of an abstract or summary:
- [1] Steadman et al. — "organised around premises and buildings rather than
  estates" is a paraphrase of their premises-to-buildings point.
- [2] Timmerman et al. — abstract states no models tailored to industrial-park
  energy systems were found.
- [17] Grünewald & Torriti — used for half-hourly non-domestic demand profiles;
  check it supports "daytime, weekday-weighted" for offices specifically.
- [18] BEES — used for offices being electricity-dominant; pull the exact share
  from the overarching report if you want a number.
- [29], [30] — retail-park literature cited only to show it is a separate body of
  work. Check the author order on [30] and the issue number on [29].
- [33], [34] — the T5 sentence was softened from "removing the split-incentive
  barrier entirely". [33] is a US study of lease terms and electricity use.
- [22] — the 75 million m² and 15 GW figures come from press coverage of the
  report; confirm against the report itself.

### Reference details to tidy in EndNote
- [9] Live register address used (the earlier "dev." staging address was replaced).
- [4] Confirm the document title on GOV.UK; the file is named
  "2025-08-28_NDR_SCat_codes".
- [12] Add the direct link from the ENA resource library.
- [23] Eden Campus "locate here" page address added.
- [31] The NatWest page only confirms Gogarburn as the headquarters. Press
  reports put the campus at about 100 acres, opened 2005; no area is stated in
  the text because no primary source was found for it.

### Unchanged from the earlier notes
- **Cross-link Section 7.** The Eden Campus modelling numbers must be the
  corrected, reconciled figures (annual demand 2,401 MWh not 1,816; the "+32%
  peak" is tariff-dependent). NOTE: Eden Campus is biomass-heated (confirmed:
  biomass energy centre heating 48 buildings + 2,500 student rooms), so the
  modelling paper's gas-boiler assumption needs an explicit caveat, and the
  review and model must be consistent on the heat source.
- **Consistency with Section 2.** This section assumes the operational definition
  (≥5 separately occupied units; ≥10,000 m² GIA or ≥2 ha; shared infrastructure;
  single or coordinated management). If that changes, the T1–T5 boundaries and
  the clustering parameters here change with it.
