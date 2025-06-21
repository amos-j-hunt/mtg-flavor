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
