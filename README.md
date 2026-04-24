#🎬 Movie Recommendation System (NLP + TF-IDF + FastAPI)

This project is a content-based Movie Recommendation System that leverages Natural Language Processing (NLP) and TF-IDF vectorization to suggest movies based on user preferences. It analyzes textual metadata such as genres, overview, keywords, and tags to compute similarity between movies and deliver intelligent recommendations.

The backend is built using FastAPI, providing a high-performance and scalable REST API for serving recommendations in real-time.

#🚀 Features
🔍 Content-Based Filtering using NLP techniques
📊 TF-IDF Vectorization for feature extraction
🤝 Cosine Similarity to find similar movies
⚡ FastAPI Backend for fast and efficient API responses
🎯 Accurate Recommendations based on movie metadata
📁 Clean and modular project structure

#🧠 How It Works
Movie data (genres, overview, keywords, etc.) is preprocessed
Text data is combined and cleaned using NLP techniques
TF-IDF is applied to convert text into numerical vectors
Cosine similarity is calculated between movie vectors
Based on user input, the system returns the most similar movies

#🛠️ Tech Stack
Python
FastAPI
Scikit-learn
Pandas & NumPy
NLP (Text Processing)
TF-IDF Vectorizer
