"""Aggregation helpers for analyzing sentiment statistics."""

import pandas as pd
from typing import Iterable, Dict, List


def by_set(df: pd.DataFrame) -> pd.DataFrame:
    """Return average sentiment metrics grouped by set."""
    return df.groupby("set_code").mean()


def by_color(df: pd.DataFrame) -> pd.DataFrame:
    """Return average sentiment metrics grouped by color identity."""
    return df.groupby("color_identity").mean()


def by_colors(df: pd.DataFrame) -> pd.DataFrame:
    """Return average sentiment metrics grouped by individual card color.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing a ``colors`` column with lists of color letters.
        Empty lists indicate colorless cards, represented with ``"C"`` in the
        result.
    """

    if "colors" not in df.columns:
        raise KeyError("DataFrame must include a 'colors' column")

    expanded = df.copy()
    expanded["color"] = expanded["colors"].apply(lambda c: c if c else ["C"])
    expanded = expanded.explode("color")

    numeric_cols = expanded.select_dtypes(include="number").columns
    return expanded.groupby("color")[numeric_cols].mean()


if __name__ == "__main__":
    # Example usage placeholder
    pass
