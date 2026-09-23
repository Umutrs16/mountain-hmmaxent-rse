from __future__ import annotations
import numpy as np
import pandas as pd


def species_cluster_bootstrap(df: pd.DataFrame, value_col: str, species_col: str = "species",
                              n_boot: int = 10000, seed: int = 20260829):
    """Bootstrap species as the independent sampling unit."""
    species = pd.unique(df[species_col])
    rng = np.random.default_rng(seed)
    estimates = np.empty(n_boot)
    grouped = {s: df.loc[df[species_col] == s, value_col].mean() for s in species}
    vals = np.array([grouped[s] for s in species], dtype=float)
    for i in range(n_boot):
        estimates[i] = rng.choice(vals, size=len(vals), replace=True).mean()
    return {
        "mean": float(np.nanmean(vals)),
        "ci_low": float(np.nanquantile(estimates, 0.025)),
        "ci_high": float(np.nanquantile(estimates, 0.975)),
    }
