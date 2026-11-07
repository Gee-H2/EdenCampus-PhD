"""
Generate manuscript Tables 3 and 4 directly from the authoritative model output.

This is the single source of truth for the numeric tables in the Paper 1
manuscript ("Multi-Vector Digital Twin Framework for Decarbonising Business
Parks"). It reads the committed full-year scenario results and emits:

    04_results/tables/manuscript_table3_annual_kpis.csv
    04_results/tables/manuscript_table4_20yr_projection.csv
    (and a LaTeX block for each, printed to stdout)

Rationale
---------
Historically the manuscript tables were hand-transcribed from model runs, which
caused repeated drift (a 1000x cost-unit bug, stale energy-only costs in prose,
and a grid-import column populated from a pre-correction run all survived in the
.docx at various points). Generating the tables from the one authoritative file
makes every published number reproducible: re-run this script and diff.

Source of truth
---------------
`04_results/tables/full_year_scenario_comparison.xlsx`, sheet "Annual KPIs".
Costs are on the study's primary tariff basis (capacity/demand charge
£120/kW/yr). Table 4 savings are defined as S0 cost minus scenario cost; the
20-year columns are the annual figures x 20 (operational projection, no
discounting, matching the manuscript's stated basis).

Run with the project environment (conda env `eden_phd`):
    python generate_manuscript_tables.py
"""

from __future__ import annotations

import os

import pandas as pd

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(
    BASE, "04_results", "tables", "full_year_scenario_comparison.xlsx"
)
OUT_DIR = os.path.join(BASE, "04_results", "tables")

PROJECTION_YEARS = 20
S0_LABEL = "S0: PV Only"


def _load_annual() -> pd.DataFrame:
    df = pd.read_excel(SRC, sheet_name="Annual KPIs")
    return df.set_index("Scenario")


def build_table3(annual: pd.DataFrame) -> pd.DataFrame:
    """Annual KPIs across scenarios (manuscript Table 3)."""
    t3 = pd.DataFrame(
        {
            "PV Generation (MWh)": annual["Annual PV (MWh)"].round(1),
            "Grid Import (MWh)": annual["Annual Grid Import (MWh)"].round(1),
            "Solar Fraction (%)": annual["Solar Fraction (%)"].round(1),
            "CO\u2082 Saved (t/yr)": annual["CO2 Saved (tonnes/yr)"].round(1),
            "Annual Cost (\u00a3k)": annual["Annual Cost (\u00a3k)"].round(1),
        }
    )
    return t3


def build_table4(annual: pd.DataFrame) -> pd.DataFrame:
    """Twenty-year operational projection vs S0 baseline (manuscript Table 4)."""
    cost = annual["Annual Cost (\u00a3k)"]
    co2 = annual["CO2 Saved (tonnes/yr)"]
    s0_cost = cost.loc[S0_LABEL]

    annual_saving = (s0_cost - cost).round(1)  # +ve = cheaper than S0
    twenty_yr_saving = (annual_saving * PROJECTION_YEARS).round(1)
    twenty_yr_co2 = (co2 * PROJECTION_YEARS).round(0).astype(int)

    t4 = pd.DataFrame(
        {
            "20-yr CO\u2082 Saved (tonnes)": twenty_yr_co2,
            "Annual Saving (\u00a3k/yr)": annual_saving,
            "20-yr Saving (\u00a3k)": twenty_yr_saving,
        }
    )
    # S0 is the baseline: savings are undefined (shown as em dash in manuscript)
    t4.loc[S0_LABEL, ["Annual Saving (\u00a3k/yr)", "20-yr Saving (\u00a3k)"]] = pd.NA
    return t4


def _fmt_signed(v) -> str:
    if pd.isna(v):
        return "\u2014"  # em dash
    return f"{v:+,.1f}"


def main() -> None:
    annual = _load_annual()
    t3 = build_table3(annual)
    t4 = build_table4(annual)

    t3_path = os.path.join(OUT_DIR, "manuscript_table3_annual_kpis.csv")
    t4_path = os.path.join(OUT_DIR, "manuscript_table4_20yr_projection.csv")
    t3.to_csv(t3_path)
    t4.to_csv(t4_path)

    print("Table 3 — Annual KPIs across scenarios (from authoritative model)")
    print("=" * 72)
    print(t3.to_string())
    print(f"\nSaved: {t3_path}\n")

    print("Table 4 — Twenty-year operational projection vs S0 baseline")
    print("=" * 72)
    # pretty-print the signed columns
    t4_disp = t4.copy()
    t4_disp["Annual Saving (\u00a3k/yr)"] = t4["Annual Saving (\u00a3k/yr)"].map(
        _fmt_signed
    )
    t4_disp["20-yr Saving (\u00a3k)"] = t4["20-yr Saving (\u00a3k)"].map(_fmt_signed)
    print(t4_disp.to_string())
    print(f"\nSaved: {t4_path}\n")

    print("=" * 72)
    print("LaTeX — Table 3 (paste into manuscript):\n")
    print(
        t3.to_latex(
            float_format="%.1f",
            caption=(
                "Annual KPIs across scenarios for the Eden Campus case study. "
                "Costs include a \u00a3120/kW/yr capacity (demand) charge "
                "representative of UK commercial DUoS billing, used as this "
                "study's primary tariff basis."
            ),
            label="tab:annual_kpis",
        )
    )

    print("\nLaTeX — Table 4 (paste into manuscript):\n")
    print(
        t4_disp.to_latex(
            caption=(
                "Twenty-year operational projection vs S0 baseline "
                "(no discounting; savings are S0 cost minus scenario cost)."
            ),
            label="tab:20yr_projection",
        )
    )

    # Internal consistency check: Table 4 annual saving must equal S0 - scenario cost
    recomputed = (
        annual["Annual Cost (\u00a3k)"].loc[S0_LABEL]
        - annual["Annual Cost (\u00a3k)"]
    ).round(1)
    ok = (recomputed.drop(S0_LABEL) == t4["Annual Saving (\u00a3k/yr)"].drop(S0_LABEL)).all()
    print("\n" + "=" * 72)
    print(f"Consistency check (T4 saving == S0 cost - scenario cost): {'PASS' if ok else 'FAIL'}")


if __name__ == "__main__":
    main()
