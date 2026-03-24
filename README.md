# Search Engine

This project is a lightweight text search engine built with **Flask** and classical NLP techniques.

## What it does

The app indexes the **20 Newsgroups** dataset and lets a user submit a search query through a web interface. It then returns the documents that are most similar to the query.

Instead of exact keyword matching alone, the project uses **TF-IDF** and **Latent Semantic Analysis (LSA)** to compare documents in a reduced semantic space.

## Main features

- Web interface for entering a search query
- Document ranking based on cosine similarity
- NLP pipeline using:
  - `TfidfVectorizer`
  - `TruncatedSVD` for LSA
  - cosine similarity for retrieval
- Uses the full **20 Newsgroups** dataset as the document corpus

## Tech stack

- Python
- Flask
- scikit-learn
- NLTK
- HTML / CSS / JavaScript
- Plotly on the frontend

## Files

- `app.py` - Flask server and search pipeline
- `templates/index.html` - Search page UI
- `static/main.js` - Frontend behavior
- `static/style.css` - Styling
- `requirements.txt` - Dependencies
- `Makefile` - Helper commands

## How it works

1. Load the 20 Newsgroups corpus
2. Remove English stopwords
3. Convert documents into TF-IDF vectors
4. Reduce dimensionality with SVD (LSA)
5. Transform the user query into the same semantic space
6. Rank documents by cosine similarity
7. Return the top matching results

## Run locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the Flask app:
   ```bash
   python app.py
   ```
3. Open the local server in your browser and submit a query.

## Why this repo is useful

This is a clear example of a classical information retrieval pipeline and shows how to build a small search product using standard NLP techniques without relying on a large language model.
