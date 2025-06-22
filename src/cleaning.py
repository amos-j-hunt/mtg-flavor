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

        # Normalize color identity field for downstream analysis. MTGJSON uses
        # the camelCase key ``colorIdentity`` with a list value of individual
        # color letters (e.g. ``["U", "R"]``).  The rest of this project expects
        # a snake_case ``color_identity`` column containing a simple string like
        # ``"UR"``. Handle both possibilities so the pipeline works regardless of
        # which form the data provides.
        if "color_identity" not in cleaned and "colorIdentity" in cleaned:
            ci = cleaned.get("colorIdentity")
            if isinstance(ci, list):
                cleaned["color_identity"] = "".join(ci)
            elif ci is not None:
                cleaned["color_identity"] = str(ci)
        elif "color_identity" in cleaned and isinstance(cleaned["color_identity"], list):
            cleaned["color_identity"] = "".join(cleaned["color_identity"])

        cleaned_cards.append(cleaned)

    return cleaned_cards


if __name__ == "__main__":
    # Example usage placeholder
    pass
