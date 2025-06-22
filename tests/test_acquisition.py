from pathlib import Path
import sys

# Ensure the src package is importable when running this file directly
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.acquisition import load_cards, load_and_clean_cards


def test_load_cards_filters_flavor(tmp_path: Path):
    sample = Path(__file__).parent / "test_data" / "sample_cards.json"
    cards = load_cards(sample)
    # should only include entry with non-empty flavorText
    assert len(cards) == 1
    assert cards[0]["name"] == "Card One"


def test_load_and_clean_cards_normalizes(tmp_path: Path):
    sample = Path(__file__).parent / "test_data" / "sample_cards.json"
    cards = load_and_clean_cards(sample)
    # expect only one card cleaned and newline removed
    assert len(cards) == 1
    assert cards[0]["flavorText"] == "Line one Line two"
    assert cards[0]["name"] == "Card One"
    assert cards[0]["setName"] == "Set A"
