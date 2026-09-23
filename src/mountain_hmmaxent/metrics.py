from __future__ import annotations
import numpy as np


def continuous_boyce_index(presence_scores, background_scores, n_bins=20):
    """Approximate continuous Boyce index using moving suitability bins.

    This implementation is intended for reproducibility checks. Publication analyses should
    use the exact frozen implementation recorded in the public release.
    """
    p = np.asarray(presence_scores, float)
    b = np.asarray(background_scores, float)
    lo, hi = np.nanmin(b), np.nanmax(b)
    if not np.isfinite(lo + hi) or hi <= lo:
        return np.nan
    centers = np.linspace(lo, hi, n_bins)
    width = (hi - lo) / max(n_bins - 1, 1)
    ratios, cs = [], []
    for c in centers:
        a, z = c - width, c + width
        npres = np.sum((p >= a) & (p <= z))
        navail = np.sum((b >= a) & (b <= z))
        if navail > 0:
            ratios.append((npres / max(len(p), 1)) / (navail / max(len(b), 1)))
            cs.append(c)
    if len(ratios) < 3:
        return np.nan
    return float(np.corrcoef(np.argsort(np.argsort(cs)), np.argsort(np.argsort(ratios)))[0, 1])
