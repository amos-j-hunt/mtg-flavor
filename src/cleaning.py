"""Text cleaning functions for flavor text analysis."""

import re
from typing import Iterable, List, Dict


def normalize(text: str) -> str:
    """Basic normalization: strip whitespace and remove newlines."""
    return re.sub(r"\s+", " ", text.strip())


def clean_flavor_texts(texts: Iterable[str]) -> list:
    """Return a list of normalized flavor text strings."""
    return [normalize(t) for t in texts]


def clean_cards(cards: Iterable[Dict]) -> List[Dict]:
    """Filter out cards missing flavor text and normalize relevant fields."""
    filtered = [c for c in cards if c.get("flavorText")]
    cleaned_texts = clean_flavor_texts(c["flavorText"] for c in filtered)

    cleaned_cards: List[Dict] = []
    for card, cleaned_text in zip(filtered, cleaned_texts):
        cleaned = dict(card)
        cleaned["flavorText"] = cleaned_text
        if "name" in cleaned:
            cleaned["name"] = normalize(cleaned["name"])
        if "setName" in cleaned:
            cleaned["setName"] = normalize(cleaned["setName"])
        cleaned_cards.append(cleaned)

    return cleaned_cards


if __name__ == "__main__":
    # Example usage placeholder
    pass
