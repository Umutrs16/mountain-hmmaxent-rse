from __future__ import annotations
import pandas as pd


def lomro_splits(df: pd.DataFrame, range_col: str = "range_id"):
    """Yield train/test indices for leave-one-mountain-range-out validation."""
    for rid in pd.unique(df[range_col].dropna()):
        test = df.index[df[range_col] == rid].to_numpy()
        train = df.index[df[range_col] != rid].to_numpy()
        if len(train) and len(test):
            yield rid, train, test


def group_block_splits(df: pd.DataFrame, block_col: str = "block_id"):
    """Yield geographic block hold-outs."""
    for bid in pd.unique(df[block_col].dropna()):
        test = df.index[df[block_col] == bid].to_numpy()
        train = df.index[df[block_col] != bid].to_numpy()
        if len(train) and len(test):
            yield bid, train, test
