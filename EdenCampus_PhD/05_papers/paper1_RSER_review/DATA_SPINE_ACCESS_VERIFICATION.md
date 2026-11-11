# Data-Spine Access Verification — Section 4

**Date:** 19 September 2026
**Purpose:** Verify which of the nine Section-4 data-spine datasets are publicly
accessible/queryable, and flag any factual errors in the skeleton. Verified via
web search of official sources (Sept 2026).

---

## Verification results

| # | Dataset | Access | Verified source | Notes for the paper |
|---|---|---|---|---|
| 1 | **VOA rating list / SCAT codes** (Eng & Wales) | ✅ Public | gov.uk Rating Manual (SCAT codes documented, e.g. 301 wholesale warehouses, 289 vehicle repair) | SCAT taxonomy is public; the full rating list is downloadable. Real, usable. |
| 2 | **Scottish Assessors valuation roll** | ✅ Public | saa.gov.uk SA Portal (Fife board page exists) | Searchable Scotland-wide via SA Portal; per-property. Bulk extract may need request. |
| 3 | **LPS NI Valuation List** | ✅ Public | valuationservices.finance-ni.gov.uk | Searchable by postcode/map. NI comparator viable. |
| 4 | **ND-NEED (non-domestic)** | ⚠️ Public — **England & Wales ONLY** | gov.uk ND-NEED (latest 2026 ed., covers 2012–2024) | Metered non-domestic consumption, by building type/size + geography. **Does NOT cover Scotland or NI** — so it cannot size Eden Campus or any Scottish estate. For Scottish/NI sizing use DESNZ sub-national electricity & gas statistics (GB, LA-level) + EPC/valuation, and say so. |
| 5 | **DNO Embedded Capacity Registers** | ✅ Public | Each DNO portal + National ECR on Northern Powergrid OpenDataSoft (combined) | ≥50 kW connected/accepted generation+storage, monthly. Downloadable CSV. Excellent. |
| 6 | **DESNZ Heat Networks Planning DB / HNDU pipeline** | ✅ Public (partial) | gov.uk HNDU pipeline | Overview of current/planned networks. The full "Planning Database" may be less granular than skeleton implies — verify scope. |
| 7 | **Non-domestic EPC registers** | ✅ Public | (Eng&Wales, Scotland, NI each have open EPC registers) | Bulk download available for Eng&Wales; Scotland via SEPR; NI separate. Fabric/intensity data. |
| 8 | **SPEN DFES (Fife) — SP Distribution** | ✅ Public | SPEN DFES, SP Distribution licence area (covers Fife) | **CORRECTED: Fife is in SP Energy Networks (SPD) area, not SSEN. See below.** |
| 9 | **SONI Tomorrow's Energy Scenarios** | ✅ Public | SONI TES (NI system operator) | Workbook available. NI comparator viable. |

**Bottom line:** all nine sources are genuinely public and accessible. The data
spine is real and buildable. One factual correction is required (item 8).

---

## CORRECTION (REVERSED 7 Nov 2026) — Fife DNO is SP Energy Networks (SPD), NOT SSEN

**This file previously asserted the opposite. That earlier assertion was wrong
and is corrected here.** Fife / St Andrews / Eden Campus is in the **SP
Distribution (SPD) licence area — SP Energy Networks (SPEN)**, not SSEN/SHEPD.

Verified against primary sources (7 Nov 2026):
- **SP Energy Networks, *St Andrews primary reinforcement* (DNOA):** states the
  works are in "the **Fife region of SP Distribution (SPD) licence area**."
- **SPEN corporate description:** distribution network operator for "**Central and
  Southern Scotland**" (plus Merseyside/Cheshire/N Wales/N Shropshire) — which
  includes Fife.
- **SSEN** covers "the **north of Scotland** and central southern England" — Fife
  is in neither.
- **SPEN is investing £20m in the Fife network, including a new primary substation
  at Guardbridge, immediately adjacent to Eden Campus** (SPEN news release) — a
  direct, locally relevant confirmation that SPEN is the Fife DNO.

Why the earlier error arose: the ENA distributor-ID table was read as placing Fife
in "Northern Scotland (SHEPD)." That is geographically wrong — Fife is in
east-central Scotland, within SPD. The correct sub-national scenario source for
Fife is **SPEN's DFES**, and the DSO procuring local flexibility for the exemplar
is **SPEN**, not SSEN.

**Action taken:** "SSEN" corrected to "SP Energy Networks (SPEN / SPD)" in
Section 3.3, Section 4.1, and Section 6.2. Any remaining "SSEN" for the Fife
exemplar should be treated as an error.

*(SSEN remains correctly cited only where the review genuinely needs a
north-of-Scotland or GB-wide comparator — check each instance.)*

---

## Access caveats to state honestly in the paper

- **VOA/Assessors/LPS** identify hereditaments but do NOT label "business parks."
  Estate delineation remains a modelled clustering inference (state the method).
- **ND-NEED** is aggregated (by type/size/geography), not per-estate — good for
  bounding demand, not for identifying individual parks.
- **ECRs** cover ≥50 kW resources only; smaller behind-the-meter assets are invisible.
- **Heat Networks DB scope** — verify whether it is a full spatial database or the
  HNDU funding pipeline (narrower). Adjust the claim accordingly.
- **Jurisdictional asymmetry** stands: GB registers are more granular/open than NI;
  keep NI as a structured comparator, not a like-for-like case.
