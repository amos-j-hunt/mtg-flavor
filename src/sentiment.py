"""Sentiment scoring utilities using TextBlob, VADER and NRCLex."""

from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from typing import Iterable, Dict
from nrclex import NRCLex

# Initialize VADER analyzer lazily
_vader = None


def vader() -> SentimentIntensityAnalyzer:
    """Return a singleton VADER analyzer."""
    global _vader
    if _vader is None:
        nltk.download("vader_lexicon", quiet=True)
        _vader = SentimentIntensityAnalyzer()
    return _vader


def _nrc_scores(text: str) -> Dict[str, float | str]:
    """Return emotion scores using the NRC affect lexicon."""
    emotions = NRCLex(text)
    freq = emotions.affect_frequencies
    categories = [
        "anger",
        "anticipation",
        "disgust",
        "fear",
        "joy",
        "negative",
        "positive",
        "sadness",
        "surprise",
        "trust",
    ]
    scores = {f"nrc_{c}": float(freq.get(c, 0.0)) for c in categories}
    top_emotion = (
        max(categories, key=lambda c: scores[f"nrc_{c}"])
        if any(scores.values())
        else "neutral"
    )
    scores["nrc_top_emotion"] = top_emotion
    return scores


def score_text(text: str) -> Dict[str, float | str]:
    """Return sentiment and tone scores for a single string."""
    blob = TextBlob(text)
    tb_polarity = blob.sentiment.polarity
    vader_scores = vader().polarity_scores(text)
    scores = {
        "textblob_polarity": tb_polarity,
        "vader_compound": vader_scores["compound"],
        "vader_pos": vader_scores["pos"],
        "vader_neg": vader_scores["neg"],
        "vader_neu": vader_scores["neu"],
    }
    scores.update(_nrc_scores(text))
    return scores


def score_texts(texts: Iterable[str]) -> list:
    """Score a list of texts and return a list of score dictionaries."""
    return [score_text(t) for t in texts]


if __name__ == "__main__":
    # Example usage placeholder
    pass
