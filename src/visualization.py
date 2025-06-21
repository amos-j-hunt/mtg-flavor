"""Visualization utilities for sentiment analysis results."""

import matplotlib.pyplot as plt
import pandas as pd


def plot_average_sentiment(df: pd.DataFrame, group: str, metric: str) -> None:
    """Bar plot of the given metric grouped by a column."""
    averages = df.groupby(group)[metric].mean().sort_values()
    averages.plot.barh()
    plt.xlabel(metric)
    plt.tight_layout()


if __name__ == "__main__":
    # Example usage placeholder
    pass
