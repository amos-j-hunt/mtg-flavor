# MTG Flavor Text Sentiment Analysis

This project analyzes sentiment in Magic: The Gathering card flavor text. The
workflow is split into several stages:

1. **Data acquisition** (`src/acquisition.py`)
2. **Cleaning & normalization** (`src/cleaning.py` – see `clean_cards`)
3. **Sentiment scoring** (`src/sentiment.py`)
4. **Aggregation** (`src/aggregation.py` – see `scripts/aggregate_results.py`)
5. **Visualization** (`src/visualization.py`)

The repository is organized as follows:

```
mtg-flavor/
├── data/             # Raw and processed card data
│   ├── raw/
│   └── processed/
├── src/              # Analysis modules
├── notebooks/        # Optional Jupyter notebooks
├── reports/
│   └── figures/      # Generated charts
└── requirements.txt  # Python dependencies
```

See `mtg_flavor_text_sentiment_analysis.md` for the full project outline.
