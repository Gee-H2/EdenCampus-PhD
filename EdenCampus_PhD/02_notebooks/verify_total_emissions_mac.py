"""
Verify total-emissions MAC on the symmetric-heat model.

The issue: fix_symmetric_heat.py measured CO2 as (solar used x 0.233) — i.e. only
grid electricity displaced BY SOLAR. Once every scenario serves heat, that metric
ignores (a) the heat pump's extra grid electricity and (b) the gas-boiler
emissions it displaces. For a fair cross-scenario abatement comparison we need
TOTAL system emissions:

    total_CO2 = grid_import_MWh * grid_factor  +  boiler_gas_MWh * gas_factor

Then abatement vs S0 = total_CO2(S0) - total_CO2(scenario), and
MAC = (cost_scenario - cost_S0) / abatement.

Grid factor: 0.233 tCO2/MWh (committed model value, kept for comparability).
Gas factor: 0.183 tCO2/MWh (DESNZ natural gas, kWh gross CV ~0.183 kgCO2/kWh).
Boiler thermal output = gas input (efficiency folded into the 0.110 GBP/kWh cost
in the committed model, which has no explicit boiler efficiency -> treat boiler
heat as gas burnt 1:1 unless an efficiency is set). We report both the grid-only
and grid+gas accounting so the difference is explicit.

Run: /opt/homebrew/anaconda3/envs/eden_phd/bin/python verify_total_emissions_mac.py
"""
from __future__ import annotations
import os, warnings
import pandas as pd
warnings.filterwarnings("ignore")
try: pd.options.future.infer_string = False
except Exception: pass
import pypsa
from data_prep import load_inputs
from capacity_charge import add_capacity_charge

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CAP = 120.0
GRID_F = 0.233   # tCO2/MWh electricity (committed)
GAS_F  = 0.183   # tCO2/MWh gas (DESNZ natural gas, gross CV)

SCEN = [
    ("S0", False, False, False, False),
    ("S1", True,  False, False, False),
    ("S2", False, True,  False, True),
    ("S3", False, False, True,  False),
    ("S4", True,  True,  True,  True),
]

def build(pv, elec, thermal, ti, b, p, h, hp):
    n = pypsa.Network(); n.set_snapshots(ti)
    n.add("Carrier","AC",co2_emissions=GRID_F)
    n.add("Carrier","hydrogen"); n.add("Carrier","heat")
    n.add("Bus","Electricity Bus",carrier="AC")
    if h: n.add("Bus","Hydrogen Bus",carrier="hydrogen")
    n.add("Bus","Heat Bus",carrier="heat")   # symmetric: heat in all
    n.add("Generator","Solar PV",bus="Electricity Bus",p_nom=1000,p_max_pu=pv,marginal_cost=0)
    n.add("Generator","Grid Import",bus="Electricity Bus",p_nom=2000,marginal_cost=0.280)
    n.add("Generator","Grid Export",bus="Electricity Bus",p_nom=500,p_max_pu=0,p_min_pu=-1,marginal_cost=-0.050)
    if b: n.add("StorageUnit","BESS",bus="Electricity Bus",p_nom=500,max_hours=4,
                efficiency_store=0.95,efficiency_dispatch=0.95,standing_loss=0.0002,cyclic_state_of_charge=True)
    if h:
        n.add("Link","Electrolyser",bus0="Electricity Bus",bus1="Hydrogen Bus",p_nom=200,efficiency=0.70,marginal_cost=0.001)
        n.add("Link","Fuel Cell",bus0="Hydrogen Bus",bus1="Electricity Bus",p_nom=100,efficiency=0.50,marginal_cost=0.002)
        n.add("Store","Hydrogen Tank",bus="Hydrogen Bus",e_nom=5000,e_cyclic=True,standing_loss=0.0001)
    n.add("Load","Electrical Demand",bus="Electricity Bus",p_set=elec)
    n.add("Generator","Backup Boiler",bus="Heat Bus",p_nom=800,marginal_cost=0.110)
    n.add("Load","Thermal Demand",bus="Heat Bus",p_set=thermal)
    if hp: n.add("Link","Heat Pump",bus0="Electricity Bus",bus1="Heat Bus",p_nom=300,efficiency=3.0,marginal_cost=0.0005)
    if p:  n.add("StorageUnit","PCM TES",bus="Heat Bus",p_nom=200,max_hours=8,
                 efficiency_store=0.95,efficiency_dispatch=0.92,standing_loss=0.001,cyclic_state_of_charge=True)
    n.optimize.create_model()
    add_capacity_charge(n, CAP, import_generator="Grid Import")
    n.optimize.solve_model(solver_name="highs")

    grid_mwh   = n.generators_t.p["Grid Import"].sum()/1000
    boiler_mwh = n.generators_t.p["Backup Boiler"].sum()/1000
    pv_gen     = n.generators_t.p["Solar PV"].sum()/1000
    exp        = n.generators_t.p["Grid Export"].abs().sum()/1000
    total_co2  = grid_mwh*GRID_F + boiler_mwh*GAS_F
    solar_only_co2_saved = (pv_gen - exp)*GRID_F  # old metric
    return dict(cost_k=round(n.objective/1000,1), grid_mwh=round(grid_mwh,1),
                boiler_mwh=round(boiler_mwh,1), total_co2=round(total_co2,1),
                old_metric=round(solar_only_co2_saved,1))

def main():
    inp = load_inputs(BASE, representative_weeks=False, verbose=False)
    R = {}
    for name,b,p,h,hp in SCEN:
        R[name] = build(inp["pv_profile"], inp["elec_demand"], inp["thermal_demand"],
                        inp["time_index"], b,p,h,hp)
    s0 = R["S0"]
    print(f"{'Scn':4}{'cost£k':>9}{'grid MWh':>10}{'boiler MWh':>11}{'TOTAL tCO2':>12}{'abate vs S0':>12}{'MAC total':>11}{'MAC(old)':>10}")
    for s,v in R.items():
        abate = s0["total_co2"] - v["total_co2"]
        dcost = (v["cost_k"]-s0["cost_k"])*1000
        mac = dcost/abate if abate else float('nan')
        old_abate = v["old_metric"] - s0["old_metric"]
        mac_old = dcost/old_abate if old_abate else float('nan')
        print(f"{s:4}{v['cost_k']:>9.1f}{v['grid_mwh']:>10.1f}{v['boiler_mwh']:>11.1f}{v['total_co2']:>12.1f}{abate:>12.1f}{mac:>11.0f}{mac_old:>10.0f}")
    print("\nMost CO2 abated vs S0 (total accounting):",
          max([s for s in R if s!='S0'], key=lambda s: s0['total_co2']-R[s]['total_co2']))
    print("Cheapest:", min(R, key=lambda s: R[s]['cost_k']))

if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------
# RESULT (7 Nov 2026), symmetric-heat model, capacity-charge basis:
#
#   Scn  cost£k  TOTAL tCO2  abate vs S0  MAC(total)  MAC(old/solar-only)
#   S0   729.0     697.5        0.0          —            —
#   S1   658.1     664.6       32.9       -2155        -1809
#   S2   683.3     508.0      189.5        -241        -2582
#   S3   705.6     682.7       14.8       -1581         -551
#   S4   628.1     541.0      156.5        -645        -1660
#
# KEY CORRECTION: the solar-only CO2 metric in fix_symmetric_heat.py is the WRONG
# denominator for cross-scenario abatement once all scenarios serve heat. On TOTAL
# emissions (grid elec + boiler gas):
#   * S2 abates the MOST CO2 (189.5 t) — heat pump displaces ~1,654 MWh of boiler gas
#   * S4 is CHEAPEST (£628k) and abates 156.5 t
#   * all four remain cost-negative vs S0
#   => The deck claim "full hybrid delivers the most abatement" was WRONG.
#      Correct: S4 cheapest, S2 greatest CO2 cut.
#
# FACTOR SENSITIVITY: absolute MAC depends on the gas factor assumed (0.183
# tCO2/MWh here) and boiler efficiency (treated 1:1). A different gas/efficiency
# assumption shifts the magnitudes (e.g. S2 between ~ -205 and -241) but not the
# ordering or the all-negative conclusion. State the factor explicitly in the paper.
