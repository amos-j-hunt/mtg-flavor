"""Data acquisition utilities."""

from pathlib import Path
import json
from typing import List, Dict

from .cleaning import clean_cards


def load_cards(json_file: Path) -> List[Dict]:
    """Load card data from a JSON file and filter entries with flavor text."""
    with open(json_file, "r", encoding="utf-8") as fh:
        cards = json.load(fh)
    return [card for card in cards if card.get("flavorText")]


def load_and_clean_cards(json_file: Path) -> List[Dict]:
    """Load cards then apply cleaning routine to relevant fields."""
    cards = load_cards(json_file)
    return clean_cards(cards)


if __name__ == "__main__":
    # Example usage placeholder
    pass
