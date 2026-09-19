# Section 3 — Scopus Search Strings (seven streams)

**Paper 1 (RSER):** *From passive estates to flexible generator energy systems*
**Database:** Scopus (primary). Syntax: `TITLE-ABS-KEY( ... )`, `*` truncation,
`{ }` for exact phrase, `W/n` for proximity. Adapt to WoS (`TS=(...)`) and
IEEE Xplore separately.

> **HONEST CAVEATS — read before running:**
> - These are *starting* strings. Search design is iterative: run each, check the
>   hit count, and tune breadth. A stream returning >2000 or <15 hits almost
>   certainly needs adjustment.
> - The proximity operator `W/n` (within n words) is Scopus-specific and powerful
>   but changes recall a lot — I've used it where it sharpens precision; loosen to
>   `AND` if recall is too low.
> - Every string AND's an **estate/scale block (A)** with a **stream-specific
>   block (B)**, so results are scoped to the business-park question, not the whole
>   literature. Confirm that scoping is what you want per stream — for some (D3, D4)
>   you may deliberately want to relax block A to catch transferable work.
> - Apply the common limits AFTER the string: `AND PUBYEAR > 2009 AND PUBYEAR < 2027`
>   (1 Jan 2010 – 31 Aug 2026 window) and language/doc-type filters via the Scopus UI.
> - **Record the exact string, date run, and hit count for each** — PRISMA-S
>   requires verbatim reporting (Section 3.3).

---

## Reusable concept blocks

**Block A — estate / business-park / campus scale** (used, with variation, across streams):
```
( "business park*" OR "science park*" OR "innovation campus" OR "commercial park*"
  OR "industrial estate*" OR "industrial park*" OR "logistics park*" OR "retail park*"
  OR "office park*" OR "enterprise zone*" OR "commercial estate*" OR "multi-tenant"
  OR "mixed-use estate*" OR campus OR "commercial building*" OR "non-domestic building*" )
```

**Block F — flexibility / market** (used where the stream is about market participation):
```
( flexib* OR "demand response" OR "demand-side" OR "demand side management"
  OR "ancillary service*" OR "balancing market*" OR "capacity market"
  OR "local flexibility market*" OR "grid service*" OR aggregat* OR "peak shav*"
  OR "load shift*" OR "distribution system operator" OR DSO )
```

---

## D1 — Commercial demand response
```
TITLE-ABS-KEY(
  ( "demand response" OR "demand-side response" OR "demand side management"
    OR "load shift*" OR "peak shav*" OR "load flexib*" )
  AND ( "commercial building*" OR "non-domestic building*" OR "office building*"
        OR "commercial sector" OR "tertiary sector" OR "business park*"
        OR "commercial estate*" )
)
AND PUBYEAR > 2009 AND PUBYEAR < 2027
```
*Tune: if too broad, add `AND (electric* OR grid OR tariff*)`. If too narrow, drop
"non-domestic".*

## D2 — Campus and estate microgrids
```
TITLE-ABS-KEY(
  ( microgrid* OR "micro-grid*" OR "energy hub*" OR "local energy system*"
    OR "multi-energy system*" )
  AND ( campus OR "business park*" OR "science park*" OR "industrial estate*"
        OR "innovation campus" OR "commercial estate*" OR "university" )
  AND ( solar OR "photovoltaic*" OR PV OR "battery*" OR storage OR renewable* )
)
AND PUBYEAR > 2009 AND PUBYEAR < 2027
```
*Tune: "university" broadens recall a lot (many campus-microgrid papers are
university sites) — keep it, but expect to screen out purely academic-campus
studies that don't transfer.*

## D3 — Energy communities
```
TITLE-ABS-KEY(
  ( "energy community" OR "energy communities" OR "renewable energy community"
    OR "citizen energy" OR "community energy" OR "collective self-consumption"
    OR "energy cooperative*" )
  AND ( governance OR "business model*" OR participation OR "cost sharing"
        OR flexib* OR market* OR commercial OR estate* OR "non-residential" )
)
AND PUBYEAR > 2009 AND PUBYEAR < 2027
```
*Note: block A deliberately relaxed — most energy-community work is residential;
you WANT to catch it to argue the commercial-estate gap. Expect a large hit count;
screen for commercial applicability.*

## D4 — Eco-industrial parks and industrial symbiosis
```
TITLE-ABS-KEY(
  ( "eco-industrial park*" OR "industrial symbiosis" OR "industrial ecology"
    OR "by-product synerg*" OR "resource exchange" )
  AND ( energy OR "energy sharing" OR "energy exchange" OR electric* OR heat
        OR flexib* OR "demand response" )
)
AND PUBYEAR > 2009 AND PUBYEAR < 2027
```
*Tune: this stream is well-defined; if hits are high, restrict the energy block to
`("energy sharing" OR "energy exchange" OR electric* OR flexib*)`.*

## D5 — District-scale sector coupling
```
TITLE-ABS-KEY(
  ( "sector coupling" OR "sector-coupling" OR "multi-vector*" OR "multi-energy*"
    OR "integrated energy system*" OR "power-to-heat" OR "electrification of heat" )
  AND ( district* OR estate* OR campus OR "business park*" OR "urban energy"
        OR "local energy" OR "commercial" )
)
AND PUBYEAR > 2009 AND PUBYEAR < 2027
```
*Tune: "district" pulls in district-heating and city-scale work — that's the gap
you're documenting (estate scale under-represented), so keep it and screen.*

## D6 — DSO transition and local flexibility markets
```
TITLE-ABS-KEY(
  ( "distribution system operator" OR DSO OR "local flexibility market*"
    OR "local energy market*" OR "flexibility procurement" OR "flexibility service*"
    OR "active distribution network*" )
  AND ( flexib* OR aggregat* OR "demand response" OR "distributed energy resource*"
        OR DER OR participat* OR procure* )
)
AND PUBYEAR > 2009 AND PUBYEAR < 2027
```
*Tune: likely a large GB/EU literature. Consider `AND (UK OR "United Kingdom"
OR GB OR Ofgem OR "Great Britain")` for a UK-focused subset, run both.*

## D7 — Digital twins for estates
```
TITLE-ABS-KEY(
  ( "digital twin*" )
  AND ( building* OR campus OR estate* OR "business park*" OR district*
        OR "energy system*" OR microgrid* )
  AND ( energy OR electric* OR "demand" OR flexib* OR optimi* OR dispatch )
)
AND PUBYEAR > 2009 AND PUBYEAR < 2027
```
*Tune: "digital twin" is exploding in the literature; expect high hits. Tighten
with `W/5`: `"digital twin*" W/5 (energy OR building* OR grid)` if needed.*

---

## Post-search filters (apply in Scopus UI, record in PRISMA-S)
- Document types: Article, Review, Conference Paper (decide and state)
- Language: English
- Subject areas: Energy, Engineering, Environmental Science (optional, state if used)

## What to record for Table 2 / Figure 1 (PRISMA)
For each stream: the verbatim string, the date run, hits before filters, hits after
filters. These populate Table 2 and the PRISMA identification box.

---

## Notes for the researcher (not for submission)
- Run each string, note the count, and **come back with the counts** — if any are
  wildly off (thousands, or single digits), we tune together before you screen.
- The grey-literature corpus (Ofgem, NESO, ENA, DESNZ, SSEN, SONI, Piclo) is
  searched separately by hand per PRISMA-S — not via Scopus.
- Consider a pilot run on D4 or D7 first (most self-contained) to calibrate your
  screening effort before the big streams (D3, D6).
