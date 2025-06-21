"""Text cleaning functions for flavor text analysis."""

import re
from typing import Iterable


def normalize(text: str) -> str:
    """Basic normalization: strip whitespace and remove newlines."""
    return re.sub(r"\s+", " ", text.strip())


def clean_flavor_texts(texts: Iterable[str]) -> list:
    """Return a list of normalized flavor text strings."""
    return [normalize(t) for t in texts]


if __name__ == "__main__":
    # Example usage placeholder
    pass
