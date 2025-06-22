import sys
from pathlib import Path

# Ensure the src package is importable when running this file directly
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.cleaning import normalize, clean_flavor_texts, clean_cards


def test_normalize_strips_whitespace():
    assert normalize("  foo\nbar  ") == "foo bar"


def test_clean_flavor_texts_list():
    texts = ["hello\nworld", "foo"]
    assert clean_flavor_texts(texts) == ["hello world", "foo"]


def test_clean_cards_filters_and_cleans():
    cards = [
        {"name": "Name\nOne", "setName": "Set\nOne", "flavorText": "hi\nthere"},
        {"name": "Name Two"},
    ]
    cleaned = clean_cards(cards)
    assert len(cleaned) == 1
    c = cleaned[0]
    assert c["name"] == "Name One"
    assert c["setName"] == "Set One"
    assert c["flavorText"] == "hi there"
