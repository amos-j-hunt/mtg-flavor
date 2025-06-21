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

## Setup

1. Create a Python environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Download the MTGJSON `AllPrintings.json` dataset from [https://mtgjson.com](https://mtgjson.com) and place it in `data/raw/AllPrintings.json`.

## Running the pipeline

Execute `main.py` to run the workflow end-to-end:
```bash
python main.py
```
The script will:
- load and clean card data
- score flavor text sentiment
- save results to `data/processed/sentiment_scores.csv`
- aggregate sentiment by color and save to `data/processed/average_sentiment_by_color.csv`
- create a chart in `reports/figures/average_polarity_by_color.png`

## Viewing outputs

Check the `data/processed` directory for CSV files containing sentiment scores and aggregates. Generated figures are stored under `reports/figures`.

## Running tests

Execute the unit test suite with `pytest`:
```bash
pytest
```
