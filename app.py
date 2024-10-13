from flask import Flask, render_template, request, jsonify
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import nltk
from nltk.corpus import stopwords
import json

nltk.download('stopwords')

app = Flask(__name__)

# Load dataset
newsgroups = fetch_20newsgroups(subset='all')
documents = newsgroups.data
stop_words = list(set(stopwords.words('english')))

# Create a Term-Document Matrix using TF-IDF
vectorizer = TfidfVectorizer(stop_words=stop_words)
X = vectorizer.fit_transform(documents)

# Perform SVD (LSA)
n_components = 100  # Number of dimensions to reduce to
svd = TruncatedSVD(n_components=n_components)
X_reduced = svd.fit_transform(X)

# Inverse transform to approximate original space (optional if you need to visualize components)
terms = vectorizer.get_feature_names_out()

def preprocess_query(query):
    """
    Preprocess the user query (e.g., remove stop words, transform using vectorizer).
    """
    query_tfidf = vectorizer.transform([query])
    query_reduced = svd.transform(query_tfidf)
    return query_reduced

def search_engine(query):
    """
    Function to search for top 5 similar documents given a query.
    Input: query (str)
    Output: documents (list), similarities (list), indices (list)
    """
    query_reduced = preprocess_query(query)
    # Compute cosine similarity between the query and all documents
    similarities = cosine_similarity(query_reduced, X_reduced)
    
    # Get the top 5 most similar documents
    top_n = 5
    indices = np.argsort(similarities[0])[::-1][:top_n]
    top_docs = [documents[i] for i in indices]
    top_similarities = [similarities[0][i] for i in indices]
    
    return top_docs, top_similarities, indices.tolist()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    documents, similarities, indices = search_engine(query)
    return jsonify({'documents': documents, 'similarities': similarities, 'indices': indices})

if __name__ == '__main__':
    app.run(debug=True)
