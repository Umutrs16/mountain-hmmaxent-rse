from __future__ import annotations
import numpy as np
import pandas as pd


def rarefy_presence_indices(y, n: int, seed: int):
    """Return indices retaining exactly n presences while leaving backgrounds untouched."""
    y = np.asarray(y)
    pos = np.flatnonzero(y == 1)
    neg = np.flatnonzero(y == 0)
    if len(pos) < n:
        raise ValueError(f"Requested n={n}, only {len(pos)} presences available")
    rng = np.random.default_rng(seed)
    keep_pos = rng.choice(pos, size=n, replace=False)
    return np.concatenate([keep_pos, neg])


def aggregate_seed_results(df: pd.DataFrame, group=("species", "n"), value="cbi"):
    return df.groupby(list(group), as_index=False)[value].mean()
