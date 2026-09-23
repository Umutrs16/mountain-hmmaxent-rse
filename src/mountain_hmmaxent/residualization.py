from __future__ import annotations
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor


def fit_residualizer(X_env, X_embed, method="ridge", random_state=20260829):
    """Fit environmental -> embedding mapping on outer-training rows only."""
    if method == "ridge":
        model = Ridge(alpha=1.0)
    elif method == "rf":
        model = RandomForestRegressor(n_estimators=300, random_state=random_state, n_jobs=-1)
    else:
        raise ValueError("method must be 'ridge' or 'rf'")
    model.fit(np.asarray(X_env), np.asarray(X_embed))
    return model


def residualize(model, X_env, X_embed):
    return np.asarray(X_embed) - model.predict(np.asarray(X_env))
