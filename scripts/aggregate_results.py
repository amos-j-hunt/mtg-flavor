from pathlib import Path
import sys

# Ensure src package is importable when running this script directly
repo_root = Path(__file__).resolve().parents[1]
sys.path.append(str(repo_root))

import pandas as pd

from src.aggregation import by_set, by_color


def main() -> None:
    scores_path = Path("data/processed/sentiment_scores.csv")
    if not scores_path.is_file():
        raise FileNotFoundError(
            f"Expected scores file at {scores_path}. Run score_flavor_texts.py first"
        )

    df = pd.read_csv(scores_path)

    metrics = [
        "textblob_polarity",
        "vader_compound",
        "vader_pos",
        "vader_neg",
        "vader_neu",
    ]

    df_by_set = by_set(df[["set_code"] + metrics])
    df_by_color = by_color(df[["color_identity"] + metrics])

    print("Average sentiment by set:\n", df_by_set.head(), sep="")
    print("\nAverage sentiment by color:\n", df_by_color.head(), sep="")


if __name__ == "__main__":
    main()
