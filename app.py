import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# -------------------------------
# Load datasets
# -------------------------------
movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")

# Merge datasets on title
movies = movies.merge(credits, on='title')

# -------------------------------
# Utility Functions
# -------------------------------

# Convert list of dicts to string
def convert(obj):
    try:
        L = []
        for i in ast.literal_eval(obj):
            L.append(i['name'])
        return " ".join(L)
    except:
        return ""

# Extract director from crew
def get_director(obj):
    try:
        for i in ast.literal_eval(obj):
            if i['job'] == 'Director':
                return i['name']
        return ""
    except:
        return ""

# -------------------------------
# Preprocess Function
# -------------------------------
def preprocess(df):
    df = df[['title', 'genres', 'keywords', 'overview', 'cast', 'crew']]
    df.dropna(inplace=True)

    df['genres'] = df['genres'].apply(convert)
    df['keywords'] = df['keywords'].apply(convert)
    df['cast'] = df['cast'].apply(convert)
    df['director'] = df['crew'].apply(get_director)

    df['tags'] = df['overview'] + " " + df['genres'] + " " + df['keywords'] + " " + df['cast'] + " " + df['director']
    return df[['title', 'tags']]

# -------------------------------
# Preprocess Data
# -------------------------------
movies = preprocess(movies)

# Vectorize tags
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

# Similarity matrix
similarity = cosine_similarity(vectors)

# -------------------------------
# Recommendation Function
# -------------------------------
def recommend(movie):
    movie = movie.strip().lower()
    all_titles = [m.lower() for m in movies['title'].values]
    
    if movie not in all_titles:
        return ["Movie not found. Try a different title."]

    idx = all_titles.index(movie)
    distances = list(enumerate(similarity[idx]))
    distances = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]

    return [movies.iloc[i[0]].title for i in distances]

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="Movie Recommender", page_icon="🎬")

st.title("🎬 Movie Recommender System")
st.write("Get top 5 movie recommendations based on content similarity!")

selected_movie = st.selectbox("Select a movie title", movies['title'].sort_values().values)

if st.button("Recommend"):
    st.subheader("Top 5 Recommendations:")
    for movie in recommend(selected_movie):
        st.write("👉", movie)
