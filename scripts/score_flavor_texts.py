from pathlib import Path
import sys

# Ensure src package is importable when running this script directly
repo_root = Path(__file__).resolve().parents[1]
sys.path.append(str(repo_root))

import pandas as pd
import nltk

from src.acquisition import load_and_clean_cards
from src.sentiment import score_texts


def main() -> None:
    # Ensure VADER lexicon is available
    nltk.download("vader_lexicon")

    cards_path = Path("data/raw/AllPrintings.json")
    cards = load_and_clean_cards(cards_path)

    texts = [card["flavorText"] for card in cards]
    scores = score_texts(texts)

    df_cards = pd.DataFrame(cards)
    df_scores = pd.DataFrame(scores)
    result = pd.concat([df_cards.reset_index(drop=True), df_scores], axis=1)

    out_path = Path("data/processed/sentiment_scores.csv")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(out_path, index=False)
    print(f"Wrote sentiment scores to {out_path}")


if __name__ == "__main__":
    main()
