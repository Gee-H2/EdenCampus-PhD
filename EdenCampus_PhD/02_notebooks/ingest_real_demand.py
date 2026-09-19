"""
Eden Campus — real metered demand ingest & validation
======================================================

Use this when you receive real metered electricity (and optionally thermal)
demand from the campus operator / BMS / half-hourly supplier data. It normalises
whatever format you are given into the exact hourly `demand_kW` CSV the model and
`data_prep.py` expect, and validates it before it reaches the model.

Handles common real-world formats:
  - kW readings or kWh-per-interval (converts kWh→kW using interval length)
  - half-hourly (48/day) or hourly (24/day) resolution (resamples to hourly)
  - timezone-aware or naive timestamps
  - a datetime column + a value column with any names (you specify them)

Usage
-----
    python ingest_real_demand.py \
        --input  ~/Downloads/eden_campus_HH_2023.csv \
        --time-col "Timestamp" \
        --value-col "kWh" \
        --unit kwh \
        --output ../01_data/demand/eden_campus_demand_2023.csv

Then re-run the model notebooks — no code changes needed, data_prep.py picks up
the new CSV automatically.
"""

from __future__ import annotations

import argparse
import sys

import numpy as np
import pandas as pd


def load_raw(path: str, time_col: str, value_col: str) -> pd.DataFrame:
    if path.lower().endswith((".xlsx", ".xls")):
        df = pd.read_excel(path)
    else:
        df = pd.read_csv(path)
    if time_col not in df.columns:
        sys.exit(f"ERROR: time column '{time_col}' not found. Columns: {list(df.columns)}")
    if value_col not in df.columns:
        sys.exit(f"ERROR: value column '{value_col}' not found. Columns: {list(df.columns)}")
    df = df[[time_col, value_col]].copy()
    df.columns = ["timestamp", "value"]
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.dropna(subset=["timestamp"])
    if df["timestamp"].dt.tz is not None:
        df["timestamp"] = df["timestamp"].dt.tz_localize(None)
    df = df.set_index("timestamp").sort_index()
    return df


def normalise_to_hourly_kw(df: pd.DataFrame, unit: str) -> pd.Series:
    """Return an hourly kW series regardless of input resolution/unit."""
    # Infer interval length (median gap) in hours
    deltas = df.index.to_series().diff().dropna()
    if deltas.empty:
        sys.exit("ERROR: fewer than 2 timestamps — cannot infer interval.")
    interval_h = deltas.median().total_seconds() / 3600.0

    values = df["value"].astype(float)

    if unit.lower() == "kwh":
        # kWh per interval → average kW over that interval
        kw = values / interval_h
    elif unit.lower() == "kw":
        kw = values
    else:
        sys.exit(f"ERROR: unit must be 'kw' or 'kwh', got '{unit}'.")

    kw = kw.rename("demand_kW")

    # Resample to hourly mean (handles half-hourly → hourly)
    hourly = kw.resample("h").mean()
    return hourly


def validate(hourly: pd.Series) -> list[str]:
    """Return a list of warnings; empty list means clean."""
    warnings = []
    n = len(hourly)
    if n not in (8760, 8784):  # 8784 for leap years
        warnings.append(f"Row count {n} is not a full year (expected 8760 or 8784).")
    gaps = hourly.isna().sum()
    if gaps:
        warnings.append(f"{gaps} missing hourly values (will be interpolated).")
    if (hourly < 0).any():
        warnings.append(f"{(hourly < 0).sum()} negative values found — check sign convention.")
    if hourly.max() > 10000:
        warnings.append(f"Peak {hourly.max():.0f} kW is very high — check units (kW vs W).")
    load_factor = hourly.mean() / hourly.max() if hourly.max() > 0 else 0
    if load_factor < 0.1 or load_factor > 0.95:
        warnings.append(f"Load factor {load_factor*100:.0f}% is unusual — check data.")
    return warnings


def main() -> None:
    ap = argparse.ArgumentParser(description="Ingest real metered demand into model format.")
    ap.add_argument("--input", required=True, help="Path to raw metered CSV/Excel")
    ap.add_argument("--time-col", required=True, help="Name of the timestamp column")
    ap.add_argument("--value-col", required=True, help="Name of the value column")
    ap.add_argument("--unit", required=True, choices=["kw", "kwh"], help="Unit of the value column")
    ap.add_argument("--output", required=True, help="Output CSV path (model format)")
    ap.add_argument("--write", action="store_true", help="Actually write output (otherwise dry-run)")
    args = ap.parse_args()

    df = load_raw(args.input, args.time_col, args.value_col)
    hourly = normalise_to_hourly_kw(df, args.unit)

    # Interpolate small gaps
    hourly = hourly.interpolate(limit=6).ffill().bfill()

    warns = validate(hourly)

    print("=" * 60)
    print("  REAL DEMAND INGEST — SUMMARY")
    print("=" * 60)
    print(f"  Input file:     {args.input}")
    print(f"  Rows (hourly):  {len(hourly)}")
    print(f"  Date range:     {hourly.index[0]} -> {hourly.index[-1]}")
    print(f"  Peak:           {hourly.max():.1f} kW")
    print(f"  Mean:           {hourly.mean():.1f} kW")
    print(f"  Annual total:   {hourly.sum()/1000:.1f} MWh")
    print(f"  Load factor:    {hourly.mean()/hourly.max()*100:.1f} %")
    print("=" * 60)
    if warns:
        print("  VALIDATION WARNINGS:")
        for w in warns:
            print(f"    - {w}")
    else:
        print("  Validation: clean ✓")
    print("=" * 60)

    out = hourly.to_frame()
    out.index.name = ""
    if args.write:
        out.to_csv(args.output)
        print(f"  Written to {args.output}")
        print("  Re-run the model notebooks — data_prep.py will use this automatically.")
    else:
        print("  DRY RUN — re-run with --write to save. Review the summary above first.")


if __name__ == "__main__":
    main()
