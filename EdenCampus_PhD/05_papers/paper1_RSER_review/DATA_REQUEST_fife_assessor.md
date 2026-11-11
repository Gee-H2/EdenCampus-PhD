# Data-request email — Fife / Scotland valuation roll (for business-park clustering)

**Purpose:** obtain a non-domestic valuation-roll extract so `cluster_business_parks.py`
can be run on real data and produce actual estate counts for RSER Section 4.
**For a first real run you only need Fife** (contains Eden Campus); Scotland-wide
can follow.

---

## Who to send it to

- **Fife:** the **Tayside Valuation Joint Board / Fife Assessor** — use the FOI /
  publication-scheme contact on the SAA Fife page (saa.gov.uk → Fife → Freedom of
  Information). Each Assessor has its own FOI inbox.
- **Scotland-wide:** you would repeat this to each regional Assessor, OR pursue
  the OS/PSGA-licence route via the university library (see notes), OR ask the
  Scottish Government statistics team how they obtain the full roll.
- **Fastest first step:** ask your supervisors (John M. Andresen / Omid Shahrokhi
  / Sudhagar Pitchaimuthu) and the University of St Andrews Eden Campus team for a
  direct introduction — this is already an "ask" on the progress-review deck.

---

## Draft email (copy, fill the [brackets], send)

> **Subject:** Data request — non-domestic valuation roll extract (PhD research, Heriot-Watt)
>
> Dear Assessor,
>
> I am a PhD researcher at Heriot-Watt University (Centre for Doctoral Training in
> Green Industrial Futures), studying the role of UK business parks in the
> electricity system. My work includes an empirical characterisation of
> business/industrial estates in Scotland, using the non-domestic valuation roll
> to identify clusters of commercial premises.
>
> Please could you provide an extract of the current non-domestic **valuation roll
> for [Fife / your board area]**, in a machine-readable format (CSV or Excel), with
> the following fields for each entry:
>
> - unique property reference number
> - full property address and **postcode**
> - **Special Category / property class code** (the classification used in the roll)
> - rateable value
> - (if available) floor area / gross internal area
>
> The data will be used solely for academic research — spatial clustering to
> identify business parks — and will be reported only in aggregate (counts and
> summary statistics). I will not republish individual records, and I will comply
> with any licensing or data-protection conditions you specify (including any
> Ordnance Survey / PSGA licence terms relating to address or location data).
>
> If a formal request route (FOI, or a data-sharing agreement) is required, I am
> happy to follow it. I can also provide a supporting note from my supervisors or
> the University if helpful.
>
> Thank you for your time.
>
> Kind regards,
> [Your name]
> [PhD researcher, CDT-GIF, Heriot-Watt University]
> [email] · [phone]

---

## Why these exact fields
`cluster_business_parks.py` needs, per hereditament: a **category code** (to keep
only business-park-compatible uses), and a **location** (postcode → coordinates via
the ONS Postcode Directory / OS Code-Point Open, or supplied eastings/northings).
Floor area (GIA) is optional but lets the scale screen use ≥10,000 m² GIA instead of
the bounding-box ≥2 ha fallback.

## Licensing caution (important before any commit)
Valuation-roll / address data is typically under **Crown copyright + Ordnance
Survey licence** (the Scottish Government statistics cite OS Licence 100024655).
You can use it to produce counts, but you likely **cannot redistribute the raw
records** in a public GitHub repo. **Keep the raw extract local; commit only the
aggregated outputs** (counts per type, sensitivity table).

## After the data arrives
1. Geocode postcodes to British National Grid eastings/northings if not supplied.
2. Rename columns to `scat, easting, northing[, gia_m2]`.
3. Confirm the business-park SCat/class list in `cluster_business_parks.py`
   (the default set is a placeholder).
4. Run: `python cluster_business_parks.py --input fife_roll_geocoded.csv`
5. Replace Table 3's `[DATA]` column with the real counts; change the Section 4.1
   sensitivity wording from "is to be reported" to past tense.
