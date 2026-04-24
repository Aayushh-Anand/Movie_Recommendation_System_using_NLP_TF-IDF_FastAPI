# =========================
# 🎬 REELIQ - COMPLETE FINAL APP
# =========================

import streamlit as st
import requests
import base64

API_BASE = "http://127.0.0.1:8000"
TMDB_IMG = "https://image.tmdb.org/t/p/w500"

st.set_page_config(
    layout="wide",
    page_title="Reeliq",
    initial_sidebar_state="expanded"
)

# =========================
# SESSION STATE
# =========================
if "category" not in st.session_state:
    st.session_state.category = "popular"

if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

# =========================
# LOAD LOGO (BASE64)
# =========================
def get_base64_image(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

logo_base64 = get_base64_image("images/Reeliq LOGO.png")

# =========================
# 🎨 CSS (FINAL)
# =========================
st.markdown("""
<style>

/* FULL WIDTH */
.block-container {
    max-width: 100% !important;
    padding: 70px 24px 24px 24px !important;
}

/* GLOBAL */
html, body {
    background-color: #020617;
    color: #E5E7EB;
    font-family: system-ui, -apple-system, sans-serif;
}

header, footer {visibility:hidden;}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    min-width: 220px !important;
    max-width: 220px !important;
    padding: 0 !important;
    background: #020617;
    border-right: 1px solid #1E293B;
}

section[data-testid="stSidebar"] > div {
    padding: 0 !important;
}

/* SIDEBAR BUTTON */
.stButton > button {
    width: 100%;
    text-align: left;
    padding: 6px 10px !important;
    margin: 0 !important;
    background: transparent;
    color: #E5E7EB;
    border: none;
    border-radius: 6px;
}

/* HOVER */
.stButton > button:hover {
    background: linear-gradient(90deg,#FF3C5F,#8B5CF6,#3B82F6);
}

/* ACTIVE */
.active-btn {
    background: linear-gradient(90deg,#FF3C5F,#8B5CF6,#3B82F6) !important;
    color: white !important;
    font-weight: 600 !important;
}

/* HEADER */
.top-header {
    position: fixed;
    top: 0;
    left: 220px;
    right: 0;
    height: 60px;
    background: #020617;
    border-bottom: 1px solid #1E293B;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 20px;
    z-index: 999;
}

/* HEADER LEFT */
.header-left {
    display: flex;
    align-items: center;
    gap: 8px;
}

.logo {
    height: 34px;
}

.app-title {
    font-size: 20px;
    font-weight: 600;
}

/* SEARCH */
.search-container {
    width: 320px;
}

/* MOVIE CARD */
.movie-card {
    background:#0B1220;
    border-radius:12px;
    padding:8px;
    border:1px solid #1E293B;
    transition:0.3s;
}

.movie-card:hover {
    transform: scale(1.05);
    box-shadow: 0px 10px 25px rgba(139,92,246,0.4);
}

.movie-title {
    font-size:14px;
    font-weight:600;
}

.movie-rating {
    font-size:12px;
    color:#94A3B8;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
with st.sidebar:

    st.markdown("### 🎬 Categories")

    categories = [
        ("Home", "popular"),
        ("Trending", "trending"),
        ("Popular", "popular"),
        ("Top Rated", "top_rated")
    ]

    for i, (name, value) in enumerate(categories):
        if st.button(name, key=f"cat_{i}"):
            st.session_state.category = value
            st.session_state.selected_movie = None

        if st.session_state.category == value:
            st.markdown(f"""
            <style>
            div[data-testid="stSidebar"] button:nth-of-type({i+1}) {{
                background: linear-gradient(90deg,#FF3C5F,#8B5CF6,#3B82F6) !important;
                color: white !important;
                font-weight: 600 !important;
            }}
            </style>
            """, unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown(f"""
<div class="top-header">
    <div class="header-left">
        <img src="data:image/png;base64,{logo_base64}" class="logo"/>
        <div class="app-title">Reeliq</div>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# SEARCH
# =========================
st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
query = st.text_input("", placeholder="Search movies...")

# =========================
# API FUNCTIONS
# =========================
def fetch_home(category):
    try:
        return requests.get(f"{API_BASE}/home", params={"category": category}).json()
    except:
        return []

def search_movies(query):
    try:
        return requests.get(f"{API_BASE}/tmdb/search", params={"query": query}).json().get("results", [])
    except:
        return []

def get_bundle(query):
    try:
        return requests.get(f"{API_BASE}/movie/search", params={"query": query}).json()
    except:
        return None

# =========================
# FETCH MOVIES
# =========================
movies = search_movies(query) if query else fetch_home(st.session_state.category)

# =========================
# MOVIE GRID
# =========================
def movie_card(movie, idx):
    title = movie.get("title", "")
    tmdb_id = movie.get("tmdb_id", movie.get("id", idx))
    poster = movie.get("poster_url") or f"https://image.tmdb.org/t/p/w500{movie.get('poster_path')}"
    rating = movie.get("vote_average", "")

    st.markdown(f"""
    <div class="movie-card">
        <img src="{poster}" style="width:100%; border-radius:10px;">
        <div class="movie-title">{title}</div>
        <div class="movie-rating">⭐ {rating}</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("View", key=f"{tmdb_id}_{idx}"):
        st.session_state.selected_movie = title

cols = 5
counter = 0

for i in range(0, len(movies), cols):
    row = movies[i:i+cols]
    columns = st.columns(cols)

    for col, movie in zip(columns, row):
        with col:
            movie_card(movie, counter)
            counter += 1

# =========================
# MOVIE DETAILS
# =========================
if st.session_state.selected_movie:
    st.markdown("---")
    st.markdown("## 🎬 Movie Details")

    data = get_bundle(st.session_state.selected_movie)

    if data:
        movie = data["movie_details"]

        col1, col2 = st.columns([1,2])

        with col1:
            st.image(movie.get("poster_url"))

        with col2:
            st.markdown(f"### {movie.get('title')}")
            st.write(movie.get("overview"))

            genres = [g["name"] for g in movie.get("genres", [])]
            st.markdown(f"Genres: {', '.join(genres)}")
            st.markdown(f"Release: {movie.get('release_date')}")

        st.markdown("### 🤖 Recommended")

        tfidf = [i["tmdb"] for i in data.get("tfidf_recommendations", []) if i.get("tmdb")]

        for i in range(0, len(tfidf), cols):
            row = tfidf[i:i+cols]
            columns = st.columns(cols)
            for col, m in zip(columns, row):
                with col:
                    st.image(m.get("poster_url"))

        st.markdown("### 🎭 Similar Movies")

        genre = data.get("genre_recommendations", [])

        for i in range(0, len(genre), cols):
            row = genre[i:i+cols]
            columns = st.columns(cols)
            for col, m in zip(columns, row):
                with col:
                    st.image(m.get("poster_url"))