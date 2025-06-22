from pathlib import Path
import urllib.request
import gzip
import pandas as pd
import matplotlib.pyplot as plt

from src.acquisition import load_and_clean_cards
from src.sentiment import score_texts
from src.aggregation import by_set, by_color
from src.visualization import plot_average_sentiment


def download_all_printings(dest: Path) -> None:
    """Download the AllPrintings dataset if it's missing."""
    url = "https://mtgjson.com/api/v5/AllPrintings.json.gz"
    print(f"{dest} not found. Downloading from {url} ...")
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = dest.with_suffix(".json.gz")
    urllib.request.urlretrieve(url, tmp_path)
    with gzip.open(tmp_path, "rb") as fin, open(dest, "wb") as fout:
        fout.write(fin.read())
    tmp_path.unlink()


def run_pipeline() -> None:
    """Run the full sentiment analysis pipeline."""
    raw_path = Path("data/raw/AllPrintings.json")
    if not raw_path.is_file():
        download_all_printings(raw_path)
    print(f"Loading cards from {raw_path} ...")
    cards = load_and_clean_cards(raw_path)

    texts = [card["flavorText"] for card in cards]
    print("Scoring flavor text ...")
    scores = score_texts(texts)

    df_cards = pd.DataFrame(cards)
    df_scores = pd.DataFrame(scores)
    df = pd.concat([df_cards.reset_index(drop=True), df_scores], axis=1)

    processed_dir = Path("data/processed")
    processed_dir.mkdir(parents=True, exist_ok=True)
    scores_path = processed_dir / "sentiment_scores.csv"
    df.to_csv(scores_path, index=False)
    print(f"Saved scored data to {scores_path}")

    print("Aggregating results ...")
    metrics = [
        "textblob_polarity",
        "vader_compound",
        "vader_pos",
        "vader_neg",
        "vader_neu",
    ]
    df_by_color = by_color(df[["color_identity"] + metrics])
    agg_path = processed_dir / "average_sentiment_by_color.csv"
    df_by_color.to_csv(agg_path)
    print(f"Saved aggregation to {agg_path}")

    print("Generating figure ...")
    fig_path = Path("reports/figures/average_polarity_by_color.png")
    fig_path.parent.mkdir(parents=True, exist_ok=True)
    plot_average_sentiment(df, group="color_identity", metric="textblob_polarity")
    plt.savefig(fig_path)
    plt.close()
    print(f"Saved figure to {fig_path}")


if __name__ == "__main__":
    run_pipeline()
