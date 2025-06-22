# MTG "Flavor Text" Sentiment Analysis

## Project Goal  
Leverage natural language processing (NLP) techniques to analyze and visualize sentiment patterns in Magic: The Gathering (MTG) flavor text data, identifying trends across sets, card colors, and potentially card types.

---

## Functional Requirements

### 1. Data Acquisition
- **1.1** Source the full set of MTG card data, ideally via MTGJSON or Scryfall bulk data.
- **1.2** Extract the `flavorText` field for all cards where it exists.
- **1.3** Extract associated metadata, including:
  - Card name  
  - Set name and set code  
  - Card color(s)  
  - Card type(s)  
  - Release date (if available)

### 2. Data Cleaning & Preparation
- **2.1** Filter out cards with missing or empty flavor text.
- **2.2** Normalize text for analysis (e.g., remove quotes, whitespace, HTML entities).
- **2.3** Encode categorical features as needed for visualization (e.g., color combinations as grouped categories).

### 3. Sentiment Analysis
- **3.1** Apply at least one sentiment analysis tool:
  - TextBlob (polarity, subjectivity)  
  - VADER (compound, positive, negative, neutral)
- **3.2** Score each flavor text according to chosen tools.
- **3.3** Apply NRCLex to classify emotional tone for each flavor text.

### 4. Aggregation and Comparison
- **4.1** Group sentiment scores by:
  - Set  
  - Color identity  
  - (Optionally) Card type
- **4.2** Calculate average and variance of sentiment scores for each group.

### 5. Visualization
- **5.1** Create plots/charts to show:
  - Average sentiment by color (e.g., pie chart or bar graph)  
  - Sentiment trends over time by set release  
  - Most “positive,” “negative,” or “funny” sets or colors  
  - Optional: Word clouds of common terms in highly negative or positive cards
- **5.2** Use libraries such as Matplotlib, Seaborn, or Plotly for visualizations.

---

## Non-Functional Requirements

### 6. Performance & Usability
- **6.1** Analysis must be executable within a reasonable time on a personal computer.
- **6.2** Output visualizations and summaries should be clear and human-readable.

### 7. Tooling & Stack
- **7.1** Python is the preferred programming language.
- **7.2** Use libraries such as:
  - Pandas for data manipulation  
  - TextBlob or NLTK/VADER for sentiment  
  - Matplotlib/Seaborn/Plotly for visualization
- **7.3** Optional: Jupyter Notebook for exploration and presentation

---

## Stretch Goals
- **8.1** Apply unsupervised clustering (e.g., KMeans or PCA) on sentiment/linguistic features to discover emergent themes.
- **8.2** Implement a small web app or interactive dashboard (e.g., using Streamlit or Dash).
- **8.3** Compare flavor text sentiment to mechanical card effects (e.g., dark flavor on cards that kill creatures).

---

## Why This Project Is Valuable
- Demonstrates ability to apply NLP tools to unstructured data.
- Explores real-world application of sentiment analysis outside traditional business/text review settings.
- Provides insights into the tone and storytelling evolution of Magic: The Gathering.
- Combines technical skills in data engineering, NLP, and visualization.
