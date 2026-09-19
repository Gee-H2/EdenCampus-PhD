"""
Eden Campus Digital Twin — reproducible data preparation
========================================================

Single source of truth for all model inputs. Both `PyPSA Model.ipynb`
(representative weeks) and `Full Year Model.ipynb` (8760 h) import from here so
that demand and PV profiles are IDENTICAL across notebooks and reproducible from
committed data files only (no live PVGIS download).

Usage from a notebook
----------------------
    from data_prep import load_inputs
    inp = load_inputs(base)               # full year (8760 h)
    inp_weeks = load_inputs(base, representative_weeks=True)  # 4×168 h

Returns a dict with:
    elec_demand   : pd.Series (kW)   — electrical demand
    thermal_demand: pd.Series (kW)   — thermal demand
    pv_profile    : pd.Series (p.u.) — PV per-unit of 1000 kW capacity
    time_index    : pd.DatetimeIndex — the snapshot index

Design decisions (documented for the manuscript)
------------------------------------------------
1. Electrical demand is loaded from the committed CSV
   `01_data/demand/eden_campus_demand_2023.csv`, which is the single
   authoritative demand series. Its annual total and peak are computed here and
   printed so the manuscript figures can be taken directly from this file rather
   than hard-coded.

2. PV is derived from the committed weather CSV
   `01_data/weather/eden_campus_2023.csv` (PVGIS 2023, already downloaded and
   committed). No live network call — the model is fully reproducible offline.

3. Thermal demand: there is no measured thermal series. It is derived as a
   transparent, documented function of the electrical demand's seasonal shape
   (heating-dominated, winter-peaking). This is clearly a MODELLED thermal
   profile and must be described as such in the manuscript — not as metered data.
"""

from __future__ import annotations

import os

import numpy as np
import pandas as pd


# PV system constants (match Table 1)
_PV_CAPACITY_KW = 1000.0
_PV_TEMP_COEFF = -0.004  # per °C, relative to 25 °C


def _load_pv_profile(base: str) -> pd.Series:
    """Per-unit PV profile (0–1) from the committed 2023 weather CSV."""
    path = os.path.join(base, "01_data/weather/eden_campus_2023.csv")
    w = pd.read_csv(path, index_col=0, parse_dates=True)
    if w.index.tz is not None:
        w.index = w.index.tz_localize(None)
    w.index = w.index.round("h")
    w = w[~w.index.duplicated(keep="first")]

    poa_total = w["poa_direct"] + w["poa_sky_diffuse"] + w["poa_ground_diffuse"]
    pv_kw = (
        _PV_CAPACITY_KW
        * (poa_total / 1000.0)
        * (1 + _PV_TEMP_COEFF * (w["temp_air"] - 25))
    ).clip(lower=0)
    pv_pu = (pv_kw / _PV_CAPACITY_KW).clip(0, 1)
    pv_pu.name = "pv_pu"
    return pv_pu


def load_pv_profile_for_year(base: str, year: int, time_index=None) -> pd.Series:
    """
    Public helper: per-unit PV profile (0–1) for a given committed weather year.

    Used by the sensitivity analysis (weather years 2020–2023). Loads the
    committed CSV `01_data/weather/eden_campus_<year>.csv` — no live PVGIS.
    If `time_index` is given, the profile is reindexed onto it.
    """
    path = os.path.join(base, f"01_data/weather/eden_campus_{year}.csv")
    w = pd.read_csv(path, index_col=0, parse_dates=True)
    if w.index.tz is not None:
        w.index = w.index.tz_localize(None)
    w.index = w.index.round("h")
    w = w[~w.index.duplicated(keep="first")]
    poa_total = w["poa_direct"] + w["poa_sky_diffuse"] + w["poa_ground_diffuse"]
    pv_kw = (
        _PV_CAPACITY_KW
        * (poa_total / 1000.0)
        * (1 + _PV_TEMP_COEFF * (w["temp_air"] - 25))
    ).clip(lower=0)
    pv_pu = (pv_kw / _PV_CAPACITY_KW).clip(0, 1)
    if time_index is not None:
        pv_pu = pv_pu.reindex(time_index).fillna(0)
    pv_pu.name = "pv_pu"
    return pv_pu


def _load_elec_demand(base: str) -> pd.Series:
    """Electrical demand (kW) from the committed authoritative CSV."""
    path = os.path.join(base, "01_data/demand/eden_campus_demand_2023.csv")
    d = pd.read_csv(path, index_col=0, parse_dates=True)
    s = d["demand_kW"].copy()
    s.name = "elec_demand_kW"
    return s


def _derive_thermal_demand(elec_demand: pd.Series) -> pd.Series:
    """
    Modelled thermal demand (kW), derived from the electrical demand index.

    NOTE: This is a MODELLED heating-dominated profile, not metered data.
    It is winter-peaking (space-heating dominated) with a daytime occupancy
    shape. Describe it as a modelled profile in the manuscript.
    """
    idx = elec_demand.index
    rng = np.random.default_rng(42)  # reproducible

    seasonal_thermal = {
        1: 1.8, 2: 1.6, 3: 1.3, 4: 0.8, 5: 0.4, 6: 0.2,
        7: 0.2, 8: 0.2, 9: 0.5, 10: 0.9, 11: 1.4, 12: 1.7,
    }
    hourly_thermal = {
        0: 0.3, 1: 0.2, 2: 0.2, 3: 0.2, 4: 0.2, 5: 0.3,
        6: 0.5, 7: 0.8, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0,
        12: 0.9, 13: 0.95, 14: 1.0, 15: 1.0, 16: 0.9, 17: 0.8,
        18: 0.6, 19: 0.5, 20: 0.4, 21: 0.35, 22: 0.3, 23: 0.3,
    }
    peak_thermal, base_thermal = 400.0, 80.0

    vals = []
    for ts in idx:
        sf = seasonal_thermal[ts.month]
        wf = 0.25 if ts.weekday() >= 5 else 1.0
        hf = hourly_thermal[ts.hour]
        base = (base_thermal + (peak_thermal - base_thermal) * hf) * sf * wf
        vals.append(max(base * rng.uniform(0.95, 1.05), 0.0))

    s = pd.Series(vals, index=idx, name="thermal_demand_kW")
    return s


def _representative_weeks_index(year: int = 2023) -> pd.DatetimeIndex:
    """Four 168-hour seasonal weeks (winter, spring, summer, autumn)."""
    winter = pd.date_range(f"{year}-01-09", periods=168, freq="h")
    spring = pd.date_range(f"{year}-04-10", periods=168, freq="h")
    summer = pd.date_range(f"{year}-07-10", periods=168, freq="h")
    autumn = pd.date_range(f"{year}-10-09", periods=168, freq="h")
    return winter.append(spring).append(summer).append(autumn)


def load_inputs(base: str, representative_weeks: bool = False, verbose: bool = True) -> dict:
    """
    Load all model inputs from committed data files.

    Parameters
    ----------
    base : str
        Path to the EdenCampus_PhD directory.
    representative_weeks : bool
        If True, subset to the four 168-hour seasonal weeks. If False (default),
        return the full 8760-hour year.
    """
    elec = _load_elec_demand(base)
    pv = _load_pv_profile(base).reindex(elec.index).fillna(0)
    thermal = _derive_thermal_demand(elec)

    if representative_weeks:
        idx = _representative_weeks_index(elec.index[0].year)
        elec = elec.reindex(idx).ffill().bfill()
        pv = pv.reindex(idx).fillna(0)
        thermal = thermal.reindex(idx).ffill().bfill()
        time_index = idx
    else:
        time_index = elec.index

    if verbose:
        print("Eden Campus inputs loaded from committed data files")
        print("=" * 55)
        print(f"  Snapshots:            {len(time_index)} h"
              f" ({'representative weeks' if representative_weeks else 'full year'})")
        print(f"  Elec demand peak:     {elec.max():.1f} kW")
        print(f"  Elec demand annual:   {elec.sum() / 1000:.1f} MWh"
              f" ({'subset' if representative_weeks else 'full year'})")
        print(f"  Thermal demand peak:  {thermal.max():.1f} kW (MODELLED)")
        print(f"  PV peak:              {pv.max() * 100:.1f} % of {int(_PV_CAPACITY_KW)} kW")
        print(f"  PV annual (1 MW):     {(pv * _PV_CAPACITY_KW).sum() / 1000:.1f} MWh")
        print("=" * 55)

    return {
        "elec_demand": elec,
        "thermal_demand": thermal,
        "pv_profile": pv,
        "time_index": time_index,
    }


if __name__ == "__main__":
    # Self-test against the committed data
    base = os.path.expanduser("~/Documents/GitHub/EdenCampus-PhD/EdenCampus_PhD")
    if not os.path.isdir(base):
        base = os.path.join(os.path.dirname(__file__), "..")
    print("\n--- FULL YEAR ---")
    load_inputs(base, representative_weeks=False)
    print("\n--- REPRESENTATIVE WEEKS ---")
    load_inputs(base, representative_weeks=True)
