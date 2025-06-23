# 🎬 Movie Recommender System

A beginner-friendly content-based movie recommendation system built using:

- Python 🐍
- pandas 🐼
- scikit-learn 🔍
- Streamlit 🌐

## 🚀 Features

- Choose a movie from dropdown
- Get top 5 content-based recommendations
- Based on genres, keywords, cast, and director
- Simple and clean UI with Streamlit

## 📁 Dataset Used

This project uses:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

👉 Download both files from [Kaggle - TMDB 5000 Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## ⚙️ How to Run

1. Clone the repo or download ZIP
2. Make sure Python is installed (>=3.8)
3. Install dependencies:

```bash
pip install pandas scikit-learn streamlit
```

4. Run the app:

```bash
streamlit run app.py
```

## 🧠 How it Works

- Data is preprocessed to extract genres, cast, keywords, and director.
- Tags are created from all content.
- CountVectorizer + Cosine Similarity used to find closest matches.

## 🙌 Made With ❤️ by Deep Darji
