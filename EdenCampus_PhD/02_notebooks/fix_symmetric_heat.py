"""
Symmetric-heat re-run — fixes the unequal thermal boundary across scenarios.

PROBLEM (found 7 Nov 2026): in `Scenario comparison.ipynb` the heat bus, thermal
demand load, and backup boiler are added ONLY when use_pcm or use_heatpump is
true — i.e. only in S2 and S4. S0, S1, S3 therefore carry NO heat bill, while
S2/S4 carry the entire 1,728 MWh/yr thermal demand. The cross-scenario cost
comparison is not like-for-like.

FIX: give EVERY scenario the same thermal demand, served by the backup boiler
wherever there is no heat pump. Electrical components are unchanged. This makes
all five scenarios serve the identical electrical + thermal load, so costs are
comparable.

This script (a) reproduces the committed asymmetric costs as a control, then
(b) runs the symmetric version, and prints both cost rankings and the MAC.
All component parameters match the committed model exactly (£/kWh costs,
capacity-charge basis £120/kW/yr).

Run: /opt/homebrew/anaconda3/envs/eden_phd/bin/python fix_symmetric_heat.py
"""
from __future__ import annotations
import os, warnings
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")
try: pd.options.future.infer_string = False
except Exception: pass
import pypsa
from data_prep import load_inputs
from capacity_charge import add_capacity_charge

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CAP_CHARGE = 120.0
CO2 = 0.233  # keep committed factor for comparability; CO2-factor fix is separate

SCEN = [
    ("S0: PV Only",      False, False, False, False),
    ("S1: PV + BESS",    True,  False, False, False),
    ("S2: PV + PCM TES", False, True,  False, True),
    ("S3: PV + H2 LDES", False, False, True,  False),
    ("S4: Full Hybrid",  True,  True,  True,  True),
]


def build(name, pv, elec, thermal, ti, use_bess, use_pcm, use_h2, use_hp,
          symmetric_heat: bool):
    n = pypsa.Network(); n.set_snapshots(ti)
    n.add("Carrier", "AC", co2_emissions=CO2)
    n.add("Carrier", "hydrogen", co2_emissions=0.0)
    n.add("Carrier", "heat", co2_emissions=0.0)
    n.add("Bus", "Electricity Bus", carrier="AC")
    if use_h2: n.add("Bus", "Hydrogen Bus", carrier="hydrogen")

    # Heat bus exists if the scenario has heat tech OR we're enforcing symmetry
    heat_bus = use_pcm or use_hp or symmetric_heat
    if heat_bus: n.add("Bus", "Heat Bus", carrier="heat")

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
    n.add("Load", "Electrical Demand", bus="Electricity Bus", carrier="AC", p_set=elec)

    if heat_bus:
        # Boiler sized to meet thermal peak (756 kW) so boiler-only scenarios
        # (S0/S1/S3 under symmetric heat) are feasible. The committed model used
        # 600 kW, which only worked because S2/S4 also had a 300 kW heat pump.
        boiler_p = 800 if symmetric_heat else 600
        n.add("Generator", "Backup Boiler", bus="Heat Bus", carrier="heat",
              p_nom=boiler_p, marginal_cost=0.110)
        n.add("Load", "Thermal Demand", bus="Heat Bus", carrier="heat", p_set=thermal)
        if use_hp:
            n.add("Link", "Heat Pump", bus0="Electricity Bus", bus1="Heat Bus",
                  p_nom=300, efficiency=3.0, marginal_cost=0.0005)
        if use_pcm:
            n.add("StorageUnit", "PCM TES", bus="Heat Bus", carrier="heat",
                  p_nom=200, max_hours=8, efficiency_store=0.95,
                  efficiency_dispatch=0.92, standing_loss=0.001,
                  cyclic_state_of_charge=True)

    n.optimize.create_model()
    add_capacity_charge(n, CAP_CHARGE, import_generator="Grid Import")
    n.optimize.solve_model(solver_name="highs")

    gi = n.generators_t.p["Grid Import"]
    pv_gen = n.generators_t.p["Solar PV"]
    exp = n.generators_t.p["Grid Export"].abs()
    pv_consumed = pv_gen.sum() - exp.sum()
    co2_saved = pv_consumed * CO2 / 1000
    # boiler gas emissions not in objective CO2; report grid-displacement CO2 as before
    return {
        "cost_k": round(n.objective / 1000, 1),
        "co2_t": round(co2_saved, 1),
        "peak_red_%": round((elec.max() - gi.max()) / elec.max() * 100, 1),
        "export_MWh": round(exp.sum() / 1000, 1),
    }


def run(symmetric: bool, inp):
    rows = {}
    for name, b, p, h, hp in SCEN:
        rows[name] = build(name, inp["pv_profile"], inp["elec_demand"],
                           inp["thermal_demand"], inp["time_index"],
                           b, p, h, hp, symmetric)
    return rows


def report(title, rows):
    print(f"\n{title}")
    print("-" * len(title))
    print(f"{'Scenario':18} {'cost £k':>9} {'CO2 t/yr':>9} {'peak red%':>9} {'export MWh':>10}")
    for s, v in rows.items():
        print(f"{s:18} {v['cost_k']:>9.1f} {v['co2_t']:>9.1f} {v['peak_red_%']:>9.1f} {v['export_MWh']:>10.1f}")
    rank = sorted(rows, key=lambda s: rows[s]["cost_k"])
    print("  cheapest -> dearest:", " < ".join(s.split(':')[0] for s in rank))
    s0 = rows["S0: PV Only"]["cost_k"]
    print("  savings vs S0 (£k/yr):",
          ", ".join(f"{s.split(':')[0]}={s0-rows[s]['cost_k']:+.1f}" for s in rows))
    return rank


def main():
    inp = load_inputs(BASE, representative_weeks=False, verbose=False)
    print("Thermal demand annual:", round(inp["thermal_demand"].sum()/1000,1), "MWh/yr")

    asym = run(False, inp)
    r1 = report("A) COMMITTED (asymmetric heat — heat only in S2/S4)", asym)

    sym = run(True, inp)
    r2 = report("B) FIXED (symmetric heat — all scenarios serve thermal demand)", sym)

    # MAC on the fixed version
    print("\nMAC vs S0 (fixed, symmetric heat):")
    s0c = sym["S0: PV Only"]["cost_k"]; s0co2 = sym["S0: PV Only"]["co2_t"]
    for s in sym:
        dcost = (sym[s]["cost_k"] - s0c) * 1000
        dco2 = sym[s]["co2_t"] - s0co2
        mac = dcost/dco2 if dco2 else float('nan')
        print(f"  {s.split(':')[0]:4}: Δcost {dcost/1000:+7.1f}k  Δco2 {dco2:+6.1f}t  MAC {mac:+9.1f} £/tCO2")

    print("\nVERDICT:")
    print(f"  Committed cheapest: {r1[0]}  |  Fixed cheapest: {r2[0]}")
    print(f"  Ranking changed: {'YES' if r1 != r2 else 'NO'}")


if __name__ == "__main__":
    main()
