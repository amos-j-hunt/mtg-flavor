"""Sentiment scoring utilities using TextBlob and VADER."""

from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from typing import Iterable, Dict

# Initialize VADER analyzer lazily
_vader = None


def vader() -> SentimentIntensityAnalyzer:
    """Return a singleton VADER analyzer."""
    global _vader
    if _vader is None:
        nltk.download("vader_lexicon", quiet=True)
        _vader = SentimentIntensityAnalyzer()
    return _vader


def score_text(text: str) -> Dict[str, float]:
    """Return sentiment scores for a single string."""
    blob = TextBlob(text)
    tb_polarity = blob.sentiment.polarity
    vader_scores = vader().polarity_scores(text)
    return {
        "textblob_polarity": tb_polarity,
        "vader_compound": vader_scores["compound"],
        "vader_pos": vader_scores["pos"],
        "vader_neg": vader_scores["neg"],
        "vader_neu": vader_scores["neu"],
    }


def score_texts(texts: Iterable[str]) -> list:
    """Score a list of texts and return a list of score dictionaries."""
    return [score_text(t) for t in texts]


if __name__ == "__main__":
    # Example usage placeholder
    pass
