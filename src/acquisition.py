"""Data acquisition utilities."""

from pathlib import Path
import json


def load_cards(json_file: Path) -> list:
    """Load card data from a JSON file and filter entries with flavor text."""
    with open(json_file, "r", encoding="utf-8") as fh:
        cards = json.load(fh)
    return [card for card in cards if card.get("flavorText")]


if __name__ == "__main__":
    # Example usage placeholder
    pass
