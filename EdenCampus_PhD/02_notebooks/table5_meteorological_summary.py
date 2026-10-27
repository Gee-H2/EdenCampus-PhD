"""
Table 5 — Annual meteorological summary for Eden Campus (2020-2023).

Recomputes the plane-of-array (POA) irradiance, mean ambient temperature,
and peak irradiance for each weather year, then writes the summary table to
05_papers/paper1/ as both .xlsx and .csv.

This script is the provenance record for Table 5 in the Paper 1 manuscript
("Multi-Vector Digital Twin Framework for Decarbonising Business Parks"). It
replaces a former scratch notebook whose Table 5 values were hard-coded; here
the values are derived from the committed source data and are reproducible.

Single source of truth
-----------------------
Weather data is read through the committed weather CSVs
`01_data/weather/eden_campus_<year>.csv` — the same files `data_prep.py`
uses for the model's PV profile. POA is computed with the identical
`poa_direct + poa_sky_diffuse + poa_ground_diffuse` definition, so Table 5
is consistent with the PV inputs used everywhere else in the project.

Verified 2026-10-27: computed POA (966 / 965 / 1002 / 982 kWh/m^2) matches
the manuscript values. (Note: the mean peak irradiance is computed here as the
true arithmetic mean of the four annual peaks = 894 W/m^2; an earlier
hand-entered table used 895.)

Run with the project environment (conda env `eden_phd`):
    python table5_meteorological_summary.py
"""

from __future__ import annotations

import os

import pandas as pd

YEARS = [2020, 2021, 2022, 2023]

# Project root resolved relative to this file: .../EdenCampus_PhD
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WEATHER_DIR = os.path.join(BASE, "01_data", "weather")
OUT_DIR = os.path.join(BASE, "05_papers", "paper1")


def _load_weather(year: int) -> pd.DataFrame:
    """Load a committed weather CSV with total POA, matching data_prep.py.

    Column header is on line 1 with hourly data immediately after (no preamble);
    columns: time, poa_direct, poa_sky_diffuse, poa_ground_diffuse,
    solar_elevation, temp_air, wind_speed, Int.
    """
    path = os.path.join(WEATHER_DIR, f"eden_campus_{year}.csv")
    w = pd.read_csv(path, index_col=0, parse_dates=True)
    if w.index.tz is not None:
        w.index = w.index.tz_localize(None)
    w["poa_total"] = w["poa_direct"] + w["poa_sky_diffuse"] + w["poa_ground_diffuse"]
    return w


def annual_meteorology(year: int) -> dict:
    """Compute POA irradiance, mean temperature and peak irradiance for a year."""
    w = _load_weather(year)
    # Hourly W/m^2 summed over the year -> kWh/m^2/year
    annual_poa_kwh = w["poa_total"].sum() / 1000.0
    return {
        "Weather Year": str(year),
        "Annual POA Irradiance (kWh/m²)": round(annual_poa_kwh),
        "Mean Ambient Temperature (°C)": round(w["temp_air"].mean(), 1),
        "Peak Irradiance (W/m²)": round(w["poa_total"].max()),
    }


def build_table() -> pd.DataFrame:
    rows = [annual_meteorology(y) for y in YEARS]
    table = pd.DataFrame(rows)

    # Append a mean row across the four years (true arithmetic means)
    mean_row = {
        "Weather Year": "Mean",
        "Annual POA Irradiance (kWh/m²)": round(
            table["Annual POA Irradiance (kWh/m²)"].mean()
        ),
        "Mean Ambient Temperature (°C)": round(
            table["Mean Ambient Temperature (°C)"].mean(), 1
        ),
        "Peak Irradiance (W/m²)": round(table["Peak Irradiance (W/m²)"].mean()),
    }
    return pd.concat([table, pd.DataFrame([mean_row])], ignore_index=True)


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    table5 = build_table()

    xlsx_path = os.path.join(OUT_DIR, "Table5_meteorological_summary.xlsx")
    csv_path = os.path.join(OUT_DIR, "Table5_meteorological_summary.csv")
    table5.to_excel(xlsx_path, index=False)
    table5.to_csv(csv_path, index=False)

    print("Table 5 — Annual meteorological summary (recomputed from committed CSVs)")
    print("=" * 70)
    print(table5.to_string(index=False))
    print()
    print(f"Saved: {xlsx_path}")
    print(f"Saved: {csv_path}")
    print()
    print("LaTeX (paste into manuscript if needed):")
    print(
        table5.to_latex(
            index=False,
            float_format="%.1f",
            caption="Annual meteorological summary for Eden Campus, 2020-2023.",
            label="tab:meteo_summary",
        )
    )


if __name__ == "__main__":
    main()
