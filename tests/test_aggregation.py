import pytest
import pandas as pd
import sys
from pathlib import Path

# Ensure the src package is importable when running this file directly
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.aggregation import by_set, by_color


def test_by_set_groups_average():
    df = pd.DataFrame({
        "set_code": ["A", "A", "B"],
        "textblob_polarity": [0.1, 0.3, 0.5],
    })
    result = by_set(df)
    result = result.sort_index()
    assert list(result.index) == ["A", "B"]
    assert result.loc["A", "textblob_polarity"] == pytest.approx(0.2)


def test_by_color_groups_average():
    df = pd.DataFrame({
        "color_identity": ["U", "U", "R"],
        "vader_compound": [0.2, 0.4, 0.6],
    })
    result = by_color(df)
    result = result.sort_index()
    assert list(result.index) == ["R", "U"]
    assert result.loc["U", "vader_compound"] == pytest.approx(0.3)
