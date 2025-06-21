"""Aggregation helpers for analyzing sentiment statistics."""

import pandas as pd
from typing import Iterable, Dict


def by_set(df: pd.DataFrame) -> pd.DataFrame:
    """Return average sentiment metrics grouped by set."""
    return df.groupby("set_code").mean()


def by_color(df: pd.DataFrame) -> pd.DataFrame:
    """Return average sentiment metrics grouped by color identity."""
    return df.groupby("color_identity").mean()


if __name__ == "__main__":
    # Example usage placeholder
    pass
