"""
Demand-sensitivity stress test — robustness of Paper 1 conclusions
==================================================================

Purpose (viva defence): quantify whether the paper's headline conclusions
survive if the real metered demand differs from the synthetic CIBSE-derived
profile. The real series could plausibly land anywhere within roughly +/-30% of
the synthetic annual energy and peak. This script re-runs the full S0-S4
scenario comparison at a range of demand scale factors and checks whether the
key findings still hold at each level.

Conclusions tested
------------------
C1. S1 (PV+BESS) is the operationally optimal (lowest-cost) configuration.
C2. The scenario cost ranking is stable (who beats whom does not reorder).
C3. Peak-reduction behaviour holds: S1 and S4 deliver large peak reductions;
    S2 and S3 deliver little.

Method
------
Reuses the committed model exactly: data_prep.load_inputs (full year, committed
data), the same PyPSA components and £/kWh marginal costs as
`Scenario comparison.ipynb`, and capacity_charge.add_capacity_charge on the
study's primary tariff basis. Only the electrical demand series is multiplied by
a scale factor; everything else is held constant.

Run with conda env `eden_phd`:
    python stress_test_demand_sensitivity.py
"""

from __future__ import annotations

import os
import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
try:
    pd.options.future.infer_string = False
except Exception:
    pass

import pypsa  # noqa: E402

from data_prep import load_inputs  # noqa: E402
from capacity_charge import add_capacity_charge  # noqa: E402

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GRID_CAPACITY_CHARGE = 120.0  # £/kW/yr — study's primary tariff basis
SCALE_FACTORS = [0.7, 0.85, 1.0, 1.15, 1.3]

SCENARIOS = [
    ("S0: PV Only", False, False, False, False),
    ("S1: PV + BESS", True, False, False, False),
    ("S2: PV + PCM TES", False, True, False, True),
    ("S3: PV + H2 LDES", False, False, True, False),
    ("S4: Full Hybrid", True, True, True, True),
]


def build_and_run(name, pv, elec, thermal, time_index,
                  use_bess, use_pcm, use_h2, use_heatpump):
    n = pypsa.Network()
    n.set_snapshots(time_index)
    n.add("Carrier", "AC", co2_emissions=0.233)
    n.add("Carrier", "hydrogen", co2_emissions=0.0)
    n.add("Carrier", "heat", co2_emissions=0.0)
    n.add("Bus", "Electricity Bus", carrier="AC")
    if use_h2:
        n.add("Bus", "Hydrogen Bus", carrier="hydrogen")
    if use_pcm or use_heatpump:
        n.add("Bus", "Heat Bus", carrier="heat")

    n.add("Generator", "Solar PV", bus="Electricity Bus", carrier="AC",
          p_nom=1000, p_max_pu=pv, marginal_cost=0)
    n.add("Generator", "Grid Import", bus="Electricity Bus", carrier="AC",
          p_nom=2000, marginal_cost=0.280)
    n.add("Generator", "Grid Export", bus="Electricity Bus", carrier="AC",
          p_nom=500, p_max_pu=0, p_min_pu=-1, marginal_cost=-0.050)
    if use_bess:
        n.add("StorageUnit", "BESS", bus="Electricity Bus", carrier="AC",
              p_nom=500, max_hours=4, efficiency_store=0.95,
              efficiency_dispatch=0.95, standing_loss=0.0002,
              cyclic_state_of_charge=True)
    if use_h2:
        n.add("Link", "Electrolyser", bus0="Electricity Bus", bus1="Hydrogen Bus",
              p_nom=200, efficiency=0.70, marginal_cost=0.001)
        n.add("Link", "Fuel Cell", bus0="Hydrogen Bus", bus1="Electricity Bus",
              p_nom=100, efficiency=0.50, marginal_cost=0.002)
        n.add("Store", "Hydrogen Tank", bus="Hydrogen Bus", carrier="hydrogen",
              e_nom=5000, e_cyclic=True, standing_loss=0.0001)
    n.add("Load", "Electrical Demand", bus="Electricity Bus", carrier="AC",
          p_set=elec)
    if use_pcm or use_heatpump:
        n.add("Generator", "Backup Boiler", bus="Heat Bus", carrier="heat",
              p_nom=600, marginal_cost=0.110)
        n.add("Load", "Thermal Demand", bus="Heat Bus", carrier="heat",
              p_set=thermal)
        if use_heatpump:
            n.add("Link", "Heat Pump", bus0="Electricity Bus", bus1="Heat Bus",
                  p_nom=300, efficiency=3.0, marginal_cost=0.0005)
        if use_pcm:
            n.add("StorageUnit", "PCM TES", bus="Heat Bus", carrier="heat",
                  p_nom=200, max_hours=8, efficiency_store=0.95,
                  efficiency_dispatch=0.92, standing_loss=0.001,
                  cyclic_state_of_charge=True)

    n.optimize.create_model()
    add_capacity_charge(n, GRID_CAPACITY_CHARGE, import_generator="Grid Import")
    n.optimize.solve_model(solver_name="highs")

    grid_import = n.generators_t.p["Grid Import"]
    peak_base = elec.max()
    peak_with = grid_import.max()
    return {
        "cost_k": round(n.objective / 1000, 1),
        "peak_red_%": round((peak_base - peak_with) / peak_base * 100, 1),
    }


def run_at_scale(inp, scale):
    pv = inp["pv_profile"]
    elec = inp["elec_demand"] * scale
    thermal = inp["thermal_demand"]  # thermal held fixed (separate vector)
    ti = inp["time_index"]
    rows = {}
    for name, b, p, h, hp in SCENARIOS:
        rows[name] = build_and_run(name, pv, elec, thermal, ti, b, p, h, hp)
    return rows


def check_conclusions(rows) -> dict:
    costs = {k: v["cost_k"] for k, v in rows.items()}
    peaks = {k: v["peak_red_%"] for k, v in rows.items()}
    ranking = sorted(costs, key=costs.get)  # cheapest first
    c1 = ranking[0] == "S1: PV + BESS"
    # C3: S1 & S4 should have high peak reduction (>20%), S2 & S3 low (<20%)
    c3 = (peaks["S1: PV + BESS"] > 20 and peaks["S4: Full Hybrid"] > 20
          and peaks["S2: PV + PCM TES"] < 20 and peaks["S3: PV + H2 LDES"] < 20)
    return {
        "cheapest": ranking[0],
        "ranking": " < ".join(s.split(":")[0] for s in ranking),
        "C1_S1_optimal": c1,
        "C3_peak_pattern": c3,
        "costs": costs,
        "peaks": peaks,
    }


def main() -> None:
    print("Loading committed inputs (full year)...")
    inp = load_inputs(BASE, representative_weeks=False, verbose=False)
    base_mwh = inp["elec_demand"].sum() / 1000
    base_peak = inp["elec_demand"].max()
    print(f"Synthetic baseline: {base_mwh:.1f} MWh/yr, peak {base_peak:.0f} kW\n")

    rankings = []
    all_c1 = all_c3 = True
    for sf in SCALE_FACTORS:
        res = run_at_scale(inp, sf)
        chk = check_conclusions(res)
        all_c1 &= chk["C1_S1_optimal"]
        all_c3 &= chk["C3_peak_pattern"]
        rankings.append((sf, chk))
        print(f"=== demand x{sf:.2f}  ({base_mwh*sf:.0f} MWh/yr, peak {base_peak*sf:.0f} kW) ===")
        print(f"  cost ranking (cheapest->dearest): {chk['ranking']}")
        print(f"  cheapest = {chk['cheapest']}  | C1 (S1 optimal): {'PASS' if chk['C1_S1_optimal'] else 'FAIL'}"
              f"  | C3 (peak pattern): {'PASS' if chk['C3_peak_pattern'] else 'FAIL'}")
        print(f"    costs £k: " + ", ".join(f"{k.split(':')[0]}={v}" for k, v in chk["costs"].items()))
        print(f"    peak red %: " + ", ".join(f"{k.split(':')[0]}={v}" for k, v in chk["peaks"].items()))
        print()

    print("=" * 64)
    print("  ROBUSTNESS VERDICT across demand scale 0.70x - 1.30x")
    print("=" * 64)
    print(f"  C1  S1 is cost-optimal at every scale:      {'YES' if all_c1 else 'NO'}")
    print(f"  C3  Peak-reduction pattern holds:           {'YES' if all_c3 else 'NO'}")
    print("  C2  Cost ranking stable:")
    uniq = {chk["ranking"] for _, chk in rankings}
    if len(uniq) == 1:
        print(f"      YES — identical ordering at all scales: {uniq.pop()}")
    else:
        print(f"      PARTIAL — {len(uniq)} distinct orderings observed:")
        for r in uniq:
            print(f"        {r}")
    print("=" * 64)


if __name__ == "__main__":
    main()
