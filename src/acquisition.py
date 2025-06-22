"""Data acquisition utilities."""

from pathlib import Path
import json
from typing import List, Dict, Iterable

from .cleaning import clean_cards


def _extract_cards(data: object) -> Iterable[Dict]:
    """Yield card dictionaries from a parsed MTGJSON structure."""
    if isinstance(data, list):
        # Already a flat list of cards
        yield from data
    elif isinstance(data, dict):
        # MTGJSON `AllPrintings` format
        if "data" in data and isinstance(data["data"], dict):
            for set_data in data["data"].values():
                if isinstance(set_data, dict) and "cards" in set_data:
                    for card in set_data["cards"]:
                        if not isinstance(card, dict):
                            continue
                        card_copy = dict(card)
                        if "set_code" not in card_copy and "code" in set_data:
                            card_copy["set_code"] = set_data.get("code")
                        if "setName" not in card_copy and "name" in set_data:
                            card_copy["setName"] = set_data.get("name")
                        yield card_copy
        elif "cards" in data and isinstance(data["cards"], list):
            # Single set structure
            for card in data["cards"]:
                if isinstance(card, dict):
                    yield card


def load_cards(json_file: Path) -> List[Dict]:
    """Load card data from a JSON file and filter entries with flavor text."""
    with open(json_file, "r", encoding="utf-8") as fh:
        parsed = json.load(fh)

    cards = [card for card in _extract_cards(parsed) if card.get("flavorText")]
    return cards


def load_and_clean_cards(json_file: Path) -> List[Dict]:
    """Load cards then apply cleaning routine to relevant fields."""
    cards = load_cards(json_file)
    return clean_cards(cards)


if __name__ == "__main__":
    # Example usage placeholder
    pass
