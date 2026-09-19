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
| 4 | **ND-NEED (non-domestic)** | ✅ Public | gov.uk ND-NEED 2024/2025; geographical annex | Metered non-domestic consumption 2012–2022(23), by building type/size + geography. Strong for sizing. |
| 5 | **DNO Embedded Capacity Registers** | ✅ Public | Each DNO portal + National ECR on Northern Powergrid OpenDataSoft (combined) | ≥50 kW connected/accepted generation+storage, monthly. Downloadable CSV. Excellent. |
| 6 | **DESNZ Heat Networks Planning DB / HNDU pipeline** | ✅ Public (partial) | gov.uk HNDU pipeline | Overview of current/planned networks. The full "Planning Database" may be less granular than skeleton implies — verify scope. |
| 7 | **Non-domestic EPC registers** | ✅ Public | (Eng&Wales, Scotland, NI each have open EPC registers) | Bulk download available for Eng&Wales; Scotland via SEPR; NI separate. Fabric/intensity data. |
| 8 | **SSEN DFES (Fife) — NOT SPEN** | ✅ Public | SSEN DFES 2024 North of Scotland technical report | **CORRECTION: Fife is in SSEN (SHEPD) licence area, not SPEN. See below.** |
| 9 | **SONI Tomorrow's Energy Scenarios** | ✅ Public | SONI TES (NI system operator) | Workbook available. NI comparator viable. |

**Bottom line:** all nine sources are genuinely public and accessible. The data
spine is real and buildable. One factual correction is required (item 8).

---

## CORRECTION REQUIRED — Fife DNO is SSEN, not SPEN

The skeleton and the first Section-4 draft state "SPEN Distribution Future Energy
Scenarios (Fife)." This is a **geographical error.**

Verified against the ENA "Who's my network operator?" distributor-ID table:
- **Distributor ID 17 — Northern Scotland — Scottish & Southern Electricity
  Networks (SSEN / SHEPD)**
- Distributor ID 18 — Southern Scotland — SP Energy Networks (SPEN)

SPEN covers *Central and Southern* Scotland. **Fife (KY postcodes, including
St Andrews and Eden Campus) sits in SSEN's Northern Scotland (SHEPD) licence
area.** The correct sub-national scenario source for Fife is therefore the
**SSEN Distribution Future Energy Scenarios (North of Scotland)**, not SPEN DFES.

**Action:** replace "SPEN DFES (Fife)" with "SSEN DFES (North of Scotland,
covering Fife)" in Section 4.1 and anywhere else it appears (Section 6 also
references SPEN as the DSO procuring flexibility for the exemplar — that too
should be checked, since the exemplar is in SSEN territory).

*[CHECK: confirm the St Andrews / Eden Campus postcode is KY16 and that KY16 is
SSEN — the distributor-ID table is licence-area level; a postcode lookup on the
ENA tool will confirm definitively.]*

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
