from __future__ import annotations
import numpy as np
import pandas as pd


def weighted_spearman(a, b):
    """Rank-correlation helper; weights are handled outside because scipy Spearman is unweighted."""
    return pd.Series(a).corr(pd.Series(b), method="spearman")


def hotspot_mask(values, q=0.90):
    values = np.asarray(values, dtype=float)
    return values >= np.nanquantile(values, q)


def jaccard(mask_a, mask_b):
    a = np.asarray(mask_a, dtype=bool); b = np.asarray(mask_b, dtype=bool)
    u = np.logical_or(a, b).sum()
    return float(np.logical_and(a, b).sum() / u) if u else np.nan


def area_weighted_overlap(hotspot, protected, area_weight):
    h = np.asarray(hotspot, bool); p = np.asarray(protected, bool); w = np.asarray(area_weight, float)
    denom = w[h].sum()
    return float(w[h & p].sum() / denom) if denom > 0 else np.nan


def stratified_null(df, hotspot_col, protected_col, weight_col, strata_cols,
                    n_null=9999, seed=20260829):
    """Monte Carlo null preserving hotspot count within supplied strata."""
    rng = np.random.default_rng(seed)
    obs = area_weighted_overlap(df[hotspot_col], df[protected_col], df[weight_col])
    sims = np.empty(n_null)
    groups = list(df.groupby(strata_cols, dropna=False))
    target_n = {k: int(g[hotspot_col].sum()) for k, g in groups}
    for i in range(n_null):
        draw = np.zeros(len(df), dtype=bool)
        for k, g in groups:
            n = target_n[k]
            if n <= 0: continue
            idx = g.index.to_numpy()
            n = min(n, len(idx))
            draw[rng.choice(idx, size=n, replace=False)] = True
        sims[i] = area_weighted_overlap(draw, df[protected_col], df[weight_col])
    p = (1 + np.sum(sims >= obs)) / (n_null + 1)
    return obs, sims, float(p)
