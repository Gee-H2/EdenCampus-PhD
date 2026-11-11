"""
Business-park identification by spatial clustering of valuation data.

Implements the method described in RSER review Section 4.1: estates are
delineated by density-based spatial clustering (DBSCAN) of geocoded
non-domestic hereditaments in business-park-compatible categories, then
screened against the operational definition from Section 2.

STATUS: the pipeline is complete and tested on synthetic sample data. It will
produce REAL estate counts only when run on the real valuation data (not yet in
the repo — see "Where to get the data" below). Do NOT quote any count from the
synthetic self-test as a result.

Method (parameters from Section 2 operational definition + Section 4.1)
----------------------------------------------------------------------
1. Load geocoded hereditaments (easting/northing or lat/lon), each with a
   category code (VOA SCat / Scottish Assessor class).
2. Keep only business-park-compatible categories (offices, workshops/factories/
   warehouses, light industrial). Default SCat set below — EDIT to match the
   definitive list you screen.
3. DBSCAN with eps = 150 m (neighbourhood radius), min_samples = 5
   (criterion 1: >=5 separately occupied units). Points are clustered in a
   metric CRS (British National Grid, EPSG:27700) so eps is in metres.
4. Keep clusters meeting the scale threshold (criterion 2): >=10,000 m2 GIA
   OR site bounding-box area >= 2 ha. (GIA used if a floor-area column exists;
   otherwise the cluster's spatial footprint is the fallback.)
5. Report the count of qualifying estates. (Criteria 3 & 4 — shared
   infrastructure, coordinated management — are a manual screen on the shortlist;
   this script flags candidates, it does not auto-confirm governance.)
6. Sensitivity: repeat for eps in {100, 150, 200, 250} m and report the range.

Where to get the data (England & Wales is downloadable; Scotland/NI are not bulk)
---------------------------------------------------------------------------------
* England & Wales — VOA rating list, full download (large, ~hundreds of MB):
  https://voaratinglists.blob.core.windows.net/html/rlidata.htm
  (the "rating list" + "summary valuation" files for the 2023 list). These give
  SCat code, address and postcode; postcodes must be geocoded to coordinates
  (e.g. via the ONS Postcode Directory / Code-Point Open).
* Scotland — Scottish Assessors valuation roll: portal only (saa.gov.uk),
  no bulk open download; request an extract from the relevant Assessor, or
  scrape per-authority within terms of use.
* Northern Ireland — LPS Non-Domestic Valuation List (finance-ni.gov.uk).

Expected input (CSV), one row per hereditament
-----------------------------------------------
Required columns (rename yours to these, or pass a mapping):
    scat          : category code (e.g. VOA SCat like '096', '203', '249')
    easting       : British National Grid easting (m)   [OR provide lon]
    northing      : British National Grid northing (m)  [OR provide lat]
Optional:
    gia_m2        : gross internal floor area (m2), for the scale threshold
    uarn / ref    : unique property reference (carried through for the shortlist)
    postcode      : used only if you geocode upstream

Run on real data:
    python cluster_business_parks.py --input voa_ew_geocoded.csv

Run the built-in self-test on synthetic data (proves the pipeline works):
    python cluster_business_parks.py --selftest
"""
from __future__ import annotations

import argparse
import sys

import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN

# Business-park-compatible VOA SCat codes — PLACEHOLDER DEFAULT.
# EDIT to the definitive screened list. Examples of relevant families:
#   offices, factories/workshops/warehouses, light industrial units.
DEFAULT_SCAT = {"096", "203", "249", "151", "217"}  # illustrative — confirm!

EPS_SENSITIVITY_M = [100, 150, 200, 250]
MIN_SAMPLES = 5                 # criterion 1: >=5 separately occupied units
SCALE_GIA_M2 = 10_000           # criterion 2a
SCALE_AREA_HA = 2.0             # criterion 2b (bounding-box fallback)


def _footprint_ha(e: np.ndarray, n: np.ndarray) -> float:
    """Bounding-box area of a cluster's points, in hectares."""
    if len(e) < 2:
        return 0.0
    return ((e.max() - e.min()) * (n.max() - n.min())) / 10_000.0


def cluster_estates(df: pd.DataFrame, eps_m: float,
                    scat_set: set[str] | None = None) -> dict:
    """Run one DBSCAN pass; return counts + the qualifying-cluster table."""
    scat_set = scat_set or DEFAULT_SCAT
    sub = df[df["scat"].astype(str).isin(scat_set)].copy()
    if sub.empty:
        return {"eps_m": eps_m, "candidate_clusters": 0, "qualifying_estates": 0,
                "clusters": pd.DataFrame()}

    coords = sub[["easting", "northing"]].to_numpy(dtype=float)
    labels = DBSCAN(eps=eps_m, min_samples=MIN_SAMPLES).fit_predict(coords)
    sub["cluster"] = labels

    rows = []
    for cid, grp in sub[sub["cluster"] >= 0].groupby("cluster"):
        e = grp["easting"].to_numpy(float)
        n = grp["northing"].to_numpy(float)
        gia = grp["gia_m2"].sum() if "gia_m2" in grp else np.nan
        area_ha = _footprint_ha(e, n)
        meets_scale = (gia >= SCALE_GIA_M2) if pd.notna(gia) else (area_ha >= SCALE_AREA_HA)
        rows.append({"cluster": cid, "n_units": len(grp),
                     "gia_m2": gia, "footprint_ha": round(area_ha, 2),
                     "meets_scale": bool(meets_scale)})
    clusters = pd.DataFrame(rows)
    qualifying = int(clusters["meets_scale"].sum()) if not clusters.empty else 0
    return {"eps_m": eps_m, "candidate_clusters": len(clusters),
            "qualifying_estates": qualifying, "clusters": clusters}


def run_with_sensitivity(df: pd.DataFrame, scat_set: set[str] | None = None) -> pd.DataFrame:
    out = []
    for eps in EPS_SENSITIVITY_M:
        r = cluster_estates(df, eps, scat_set)
        out.append({"eps_m": eps,
                    "candidate_clusters": r["candidate_clusters"],
                    "qualifying_estates": r["qualifying_estates"]})
    return pd.DataFrame(out)


def _make_synthetic(seed: int = 42) -> pd.DataFrame:
    """Synthetic hereditaments: 3 dense 'parks' + scattered noise. SELF-TEST ONLY."""
    rng = np.random.default_rng(seed)
    parts = []
    # three genuine estates of 6-12 units within ~80 m of a centre
    for cx, cy, k in [(325000, 673000, 8), (326500, 672000, 11), (324000, 674500, 6)]:
        parts.append(pd.DataFrame({
            "scat": "096",
            "easting": rng.normal(cx, 40, k),
            "northing": rng.normal(cy, 40, k),
            "gia_m2": rng.uniform(1500, 3000, k),
        }))
    # scattered singletons (noise — should NOT form estates)
    parts.append(pd.DataFrame({
        "scat": "096",
        "easting": rng.uniform(320000, 330000, 40),
        "northing": rng.uniform(670000, 676000, 40),
        "gia_m2": rng.uniform(200, 800, 40),
    }))
    # some out-of-scope categories (should be filtered out)
    parts.append(pd.DataFrame({
        "scat": "999", "easting": rng.uniform(320000, 330000, 20),
        "northing": rng.uniform(670000, 676000, 20), "gia_m2": rng.uniform(100, 500, 20),
    }))
    return pd.concat(parts, ignore_index=True)


def main() -> None:
    ap = argparse.ArgumentParser(description="Cluster valuation data into business parks.")
    ap.add_argument("--input", help="CSV of geocoded hereditaments (see header).")
    ap.add_argument("--selftest", action="store_true",
                    help="Run on synthetic data to prove the pipeline works.")
    args = ap.parse_args()

    if args.selftest:
        print("SELF-TEST on SYNTHETIC data — these counts are NOT a result.\n")
        df = _make_synthetic()
    elif args.input:
        df = pd.read_csv(args.input)
        missing = {"scat", "easting", "northing"} - set(df.columns)
        if missing:
            sys.exit(f"ERROR: input missing required columns: {missing}")
        print(f"Loaded {len(df):,} hereditaments from {args.input}\n")
    else:
        sys.exit("Provide --input <csv> for real data, or --selftest to demo.")

    print(f"Parameters: eps={EPS_SENSITIVITY_M} m, min_samples={MIN_SAMPLES}, "
          f"scale >= {SCALE_GIA_M2:,} m2 GIA or {SCALE_AREA_HA} ha")
    print(f"SCat filter: {sorted(DEFAULT_SCAT)}  (EDIT to the screened list)\n")

    base = cluster_estates(df, eps_m=150.0)
    print("=== Primary run (eps = 150 m) ===")
    print(f"  candidate clusters (>=5 units): {base['candidate_clusters']}")
    print(f"  qualifying estates (meet scale): {base['qualifying_estates']}")
    if not base["clusters"].empty:
        print(base["clusters"].to_string(index=False))

    print("\n=== Sensitivity across radius ===")
    print(run_with_sensitivity(df).to_string(index=False))

    if args.selftest:
        print("\nExpected self-test result: 3 qualifying estates at every radius "
              "(the 3 planted parks); scattered singletons and out-of-scope "
              "categories are correctly excluded.")


if __name__ == "__main__":
    main()
