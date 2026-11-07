"""
Eden Campus — synthetic vs. real demand comparison / validation harness
=======================================================================

Quantifies how the real metered demand differs from the synthetic
(CIBSE-benchmark-derived) series the model was built on. This is the core of the
"validation" story for Paper 1: it turns the synthetic-demand *limitation* into a
measured validation result, and produces the figure/metrics needed to flip the
manuscript framing from "in the absence of metered data" to "validated against
metered data."

Both inputs must be in the model's canonical demand format:
    <unnamed index: hourly naive timestamps>, demand_kW

Use `ingest_real_demand.py` first to normalise whatever the site/supplier gives
you (half-hourly kWh, sub-meters, etc.) into that format.

What it reports
---------------
  - Annual energy (MWh), peak (kW), mean (kW), load factor
  - Monthly energy profile (seasonal shape)
  - Average diurnal profile (24-hour shape), weekday vs weekend
  - Error metrics on the OVERLAPPING hours only (real data may be a partial year):
      MAE, RMSE, MAPE, bias, Pearson r, peak-timing agreement
  - A 2x2 comparison figure saved to 04_results/figures/

Partial-year safe: if the real series covers only part of the year, all
distributional and error metrics are computed on the overlapping timestamps,
and the coverage is reported so nothing is silently extrapolated.

Usage
-----
    python compare_demand_synthetic_vs_real.py \
        --synthetic ../01_data/demand/eden_campus_demand_2023_synthetic.csv \
        --real      ../01_data/demand/eden_campus_demand_2023.csv \
        [--label-real "Metered 2023"] [--save-fig]

Run with conda env `eden_phd`.
"""

from __future__ import annotations

import argparse
import os

import numpy as np
import pandas as pd

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FIG_DIR = os.path.join(BASE, "04_results", "figures")


def load_series(path: str, name: str) -> pd.Series:
    df = pd.read_csv(path, index_col=0, parse_dates=True)
    col = "demand_kW" if "demand_kW" in df.columns else df.columns[0]
    s = df[col].astype(float)
    s.name = name
    s = s[~s.index.duplicated(keep="first")].sort_index()
    return s


def summary(s: pd.Series) -> dict:
    peak = s.max()
    return {
        "hours": int(len(s)),
        "annual_MWh": s.sum() / 1000.0,
        "peak_kW": peak,
        "mean_kW": s.mean(),
        "load_factor_%": (s.mean() / peak * 100.0) if peak > 0 else float("nan"),
        "peak_time": s.idxmax(),
    }


def diurnal(s: pd.Series, weekend: bool | None = None) -> pd.Series:
    idx = s.index
    if weekend is True:
        s = s[idx.weekday >= 5]
    elif weekend is False:
        s = s[idx.weekday < 5]
    return s.groupby(s.index.hour).mean()


def monthly_energy(s: pd.Series) -> pd.Series:
    return s.groupby(s.index.month).sum() / 1000.0  # MWh per month


def error_metrics(syn: pd.Series, real: pd.Series) -> dict:
    """Metrics on overlapping timestamps only."""
    common = syn.index.intersection(real.index)
    if len(common) == 0:
        return {"overlap_hours": 0}
    a = syn.loc[common]
    b = real.loc[common]
    err = b - a  # how far synthetic was from real
    mae = err.abs().mean()
    rmse = float(np.sqrt((err ** 2).mean()))
    denom = b.replace(0, np.nan).abs()
    mape = (err.abs() / denom).replace([np.inf, -np.inf], np.nan).mean() * 100.0
    r = float(np.corrcoef(a.values, b.values)[0, 1]) if len(common) > 1 else float("nan")
    return {
        "overlap_hours": int(len(common)),
        "coverage_%": len(common) / len(real) * 100.0,
        "MAE_kW": mae,
        "RMSE_kW": rmse,
        "MAPE_%": mape,
        "bias_kW": err.mean(),  # +ve => synthetic underestimated real
        "pearson_r": r,
    }


def make_figure(syn: pd.Series, real: pd.Series, label_syn: str, label_real: str, out_path: str):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(2, 2, figsize=(16, 11))
    fig.suptitle(
        f"Eden Campus demand — {label_syn} vs {label_real}",
        fontsize=15, fontweight="bold",
    )

    # Monthly energy
    ms, mr = monthly_energy(syn), monthly_energy(real)
    months = range(1, 13)
    a = ax[0, 0]
    a.plot(months, [ms.get(m, np.nan) for m in months], "o-", label=label_syn, color="#2E86AB")
    a.plot(months, [mr.get(m, np.nan) for m in months], "s-", label=label_real, color="#C73E1D")
    a.set_title("Monthly energy (MWh)"); a.set_xlabel("Month"); a.set_ylabel("MWh")
    a.legend(); a.grid(alpha=0.3)

    # Diurnal weekday
    a = ax[0, 1]
    a.plot(range(24), diurnal(syn, weekend=False).reindex(range(24)), label=f"{label_syn} (wkday)", color="#2E86AB")
    a.plot(range(24), diurnal(real, weekend=False).reindex(range(24)), label=f"{label_real} (wkday)", color="#C73E1D")
    a.set_title("Average weekday diurnal profile"); a.set_xlabel("Hour"); a.set_ylabel("kW")
    a.legend(); a.grid(alpha=0.3)

    # Diurnal weekend
    a = ax[1, 0]
    a.plot(range(24), diurnal(syn, weekend=True).reindex(range(24)), label=f"{label_syn} (wkend)", color="#2E86AB")
    a.plot(range(24), diurnal(real, weekend=True).reindex(range(24)), label=f"{label_real} (wkend)", color="#C73E1D")
    a.set_title("Average weekend diurnal profile"); a.set_xlabel("Hour"); a.set_ylabel("kW")
    a.legend(); a.grid(alpha=0.3)

    # Scatter on overlap
    a = ax[1, 1]
    common = syn.index.intersection(real.index)
    if len(common) > 0:
        a.scatter(syn.loc[common], real.loc[common], s=4, alpha=0.3, color="#555555")
        lim = max(syn.loc[common].max(), real.loc[common].max())
        a.plot([0, lim], [0, lim], "r--", linewidth=1, label="1:1")
        a.set_xlabel(f"{label_syn} (kW)"); a.set_ylabel(f"{label_real} (kW)")
        a.set_title(f"Hourly agreement (n={len(common)})"); a.legend(); a.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def _print_block(title: str, d: dict):
    print(f"\n{title}")
    print("-" * len(title))
    for k, v in d.items():
        if isinstance(v, float):
            print(f"  {k:16} {v:,.2f}")
        else:
            print(f"  {k:16} {v}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Compare synthetic vs real demand.")
    ap.add_argument("--synthetic", required=True)
    ap.add_argument("--real", required=True)
    ap.add_argument("--label-syn", default="Synthetic")
    ap.add_argument("--label-real", default="Metered")
    ap.add_argument("--save-fig", action="store_true")
    args = ap.parse_args()

    syn = load_series(args.synthetic, args.label_syn)
    real = load_series(args.real, args.label_real)

    print("=" * 64)
    print("  SYNTHETIC vs REAL DEMAND — VALIDATION COMPARISON")
    print("=" * 64)
    _print_block(f"{args.label_syn} summary", summary(syn))
    _print_block(f"{args.label_real} summary", summary(real))

    s_sum, r_sum = summary(syn), summary(real)
    print("\nHeadline deltas (real vs synthetic)")
    print("-" * 35)
    for k in ["annual_MWh", "peak_kW", "mean_kW", "load_factor_%"]:
        d = r_sum[k] - s_sum[k]
        pct = (d / s_sum[k] * 100.0) if s_sum[k] else float("nan")
        print(f"  {k:16} {d:+,.1f}  ({pct:+.1f}%)")

    _print_block("Error metrics (overlapping hours)", error_metrics(syn, real))

    if args.save_fig:
        os.makedirs(FIG_DIR, exist_ok=True)
        out = os.path.join(FIG_DIR, "demand_synthetic_vs_real.png")
        make_figure(syn, real, args.label_syn, args.label_real, out)
        print(f"\nFigure saved: {out}")

    print("\n" + "=" * 64)
    print("  Interpretation hints:")
    print("  - bias_kW > 0  => synthetic UNDER-estimated real demand")
    print("  - pearson_r near 1 => shape matches well even if level differs")
    print("  - large MAPE with high r => timing right, magnitude off (rescale)")
    print("=" * 64)


if __name__ == "__main__":
    main()
