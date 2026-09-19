# Section 6 — Market and Regulatory Access Map

**Paper 1 (RSER)** · Target: ~2,800 words · Outputs: Table 5 (service × route ×
typology fit), Fig. 2 (access matrix). Purpose (skeleton): move from literature to
the live market stack — GB in depth, with a Northern Ireland comparator.

> Conventions: `[REF]` = citation; `[VERIFY]` = confirm regulatory detail against
> the primary source (Ofgem/NESO/ENA code or decision) before submission.
> Regulatory facts move quickly — date-stamp each claim.

---

## 6.1 Framing: implicit and explicit value

Business-park flexibility can be rewarded through two channels, which this section
treats separately: **implicit value** (avoided charges) and **explicit value**
(paid services). The distinction matters because the two have different
participation requirements and fit the park typology (Section 4) differently.

**Implicit value — avoided charges.** Without entering any market, an estate can
reduce its bill by shifting load away from high-charge periods:
- **DUoS red-band avoidance** — shifting demand out of the distribution
  red time-band reduces distribution-use-of-system charges [REF/VERIFY: DUoS
  banded charging under DCP228 / current arrangements];
- **Post-TCR banded residual charges** — Ofgem's Targeted Charging Review moved
  residual network charges to fixed bands, changing what estates can and cannot
  avoid [VERIFY: TCR fixed-charge banding, effective dates];
- **Market-wide Half-Hourly Settlement (MHHS)** — the migration to MHHS changes
  the settlement baseline and improves the visibility on which flexibility is
  rewarded [VERIFY: MHHS migration timeline].

**Explicit value — paid services.** An estate (or its aggregator) can be paid to
provide flexibility through defined products (6.2–6.4).

## 6.2 DSO and local flexibility markets

Under the ENA Open Networks programme, DNOs procure local flexibility through a
standard product suite — **Sustain, Secure, Dynamic, and Restore** — via
platforms [REF/VERIFY: ENA Open Networks product definitions]. For the Fife/Eden
Campus exemplar these are procured by **SSEN** (the relevant DNO for the North of
Scotland licence area — *not* SPEN, which covers Central and Southern Scotland;
see DATA_SPINE_ACCESS_VERIFICATION.md) [VERIFY]. Local markets are the most
natural entry point for estate flexibility because they are distribution-connected
and location-specific.

## 6.3 National markets: Balancing Mechanism, DFS, Capacity Market, frequency

- **Balancing Mechanism (BM).** Estate flexibility can access the BM via a
  **Virtual Lead Party (VLP)** under **BSC modification P344**, with wholesale
  market access extended under **P415** [VERIFY: P344 VLP role; P415 scope and
  status]. This is the principal route by which aggregated behind-the-meter
  flexibility reaches national balancing.
- **Demand Flexibility Service (DFS).** NESO's DFS, originally a winter-only
  service, has been approved by Ofgem to operate **year-round** [REF: NESO/Ofgem
  DFS year-round approval, 2025]. DFS is a low-barrier entry product well suited to
  commercial estates.
- **Capacity Market (CM).** Demand-side response can participate in the CM,
  providing capacity payments for guaranteed demand reduction at stress events
  [VERIFY: CM DSR participation rules].
- **Frequency response.** The dynamic frequency products (Dynamic Containment,
  Dynamic Moderation, Dynamic Regulation — DC/DM/DR) are accessible to fast assets
  such as batteries [VERIFY: current NESO frequency product definitions].
- **LDES cap-and-floor.** The long-duration electricity storage cap-and-floor
  regime is host context rather than a park-scale product, but is relevant where an
  estate hosts longer-duration storage [VERIFY: Ofgem/DESNZ LDES cap-and-floor,
  2025 windows].

## 6.4 The reform layer

Several reforms in train reshape access and must be reflected:
- **MHHS migration** — changes settlement and flexibility visibility [VERIFY];
- **REMA** — the Review of Electricity Market Arrangements confirmed **reformed
  national pricing** in July 2025, with zonal pricing rejected [VERIFY: DESNZ REMA
  decision, July 2025]. This is materially relevant: had zonal pricing been
  adopted, locational signals for estate flexibility would differ sharply;
- **Heat-network zoning** — under the **Energy Act 2023** (England) and the **Heat
  Networks (Scotland) Act 2021**, heat-network zoning affects estates with thermal
  assets [VERIFY: confirm both instruments and their zoning provisions].

## 6.5 Northern Ireland comparator

NI operates a distinct stack: the **Single Electricity Market (SEM)** with
**Demand Side Units (DSUs)** as the DSR participation vehicle, the **DS3** system
services transitioning to **FASS**, distribution by **NIE Networks**, and an
**EU ETS** carbon context distinct from the UK ETS [VERIFY: each NI mechanism].
The comparator shows that participation vehicles for estate flexibility are
jurisdiction-specific, reinforcing that a UK-wide account must treat NI separately.

## 6.6 Barriers to estate participation

Across both channels, recurring barriers limit business-park participation:
- **Multi-MPAN aggregation friction** — an estate spans many meter points; 
  aggregating them for a single flexibility offer is administratively hard [REF];
- **Landlord–tenant split incentives** — the party able to contract (landlord)
  often does not hold the supply relationship (tenant) [REF];
- **Private-wire limits** — regulatory constraints on private networks limit
  behind-the-boundary trading [VERIFY];
- **Pre-MHHS data visibility** — without half-hourly data, flexibility is hard to
  baseline and reward [REF].

These barriers fall unevenly across the typology: coordinated estates (T3, T5)
face them least; fragmented multi-tenant estates (T1, T2) most.

## 6.7 Service × route × typology fit (Table 5, Fig. 2)

**Table 5 — Flexibility service × market route × typology fit** *(to complete)*

| Service | Route | Best-fit type(s) | Key barrier |
|---|---|---|---|
| Peak-charge avoidance | Implicit (DUoS) | All (esp. T3/T5) | Data visibility (pre-MHHS) |
| Local flexibility | DSO products (SSEN etc.) | T2, T3 | Multi-MPAN aggregation |
| Balancing / wholesale | BM via VLP (P344/P415) | T3, T5 | Aggregation, metering |
| Demand reduction | DFS (year-round) | T1, T3 | Low barrier — good entry |
| Capacity | Capacity Market DSR | T2, T3 | Firmness of commitment |
| Frequency | DC/DM/DR | Battery-hosting estates | Asset speed/size |

Figure 2 will render this as an access matrix (typology rows × route columns,
shaded by fit).

---

## Notes for the researcher (not for submission)

- **Every regulatory claim needs a date-stamped source.** This field changes fast;
  a reviewer will check P415 status, REMA July-2025 decision, DFS year-round, LDES
  windows, and TCR/MHHS timelines. Confirm each against the Ofgem/NESO/DESNZ
  primary source before submission.
- **SSEN not SPEN** for the Fife exemplar — already corrected in Section 4; keep
  consistent here and check whether GB-wide coverage means naming multiple DNOs.
- Table 5 fit ratings must be justified from Section 4.3 capability + these routes.
- ~1,500 words scaffolded; expand each product with participation detail and
  evidence to reach ~2,800.
