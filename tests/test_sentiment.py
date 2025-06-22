import sys
from pathlib import Path

# Ensure the src package is importable when running this file directly
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.sentiment import score_text, score_texts


def test_score_text_returns_scores():
    result = score_text("I love this game!")
    assert "textblob_polarity" in result
    assert "vader_compound" in result
    assert isinstance(result["textblob_polarity"], float)


def test_score_texts_multiple():
    texts = ["good", "bad"]
    scores = score_texts(texts)
    assert isinstance(scores, list)
    assert len(scores) == 2
    assert set(scores[0]) == set(scores[1])


def test_score_text_includes_nrc():
    result = score_text("This card is amazing!")
    assert "nrc_top_emotion" in result
    assert isinstance(result["nrc_top_emotion"], str)
