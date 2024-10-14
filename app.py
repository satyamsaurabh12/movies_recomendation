from http.client import responses
import requests
import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]]['title'])  # Corrected attribute access
    return recommended_movies

# Load the data
movies_dict = pickle.load(open("movies_dict.pkl", 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl", 'rb'))

# Streamlit UI
st.title("Movies Recommender System")

selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:", movies['title'].values)  # Corrected prompt text

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for movie in recommendations:
        st.write(movie)
