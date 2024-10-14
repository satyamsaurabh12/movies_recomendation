# Movie Recommendation System 🎬🎥

This project is a **Movie Recommendation System** built using Python, Streamlit, and machine learning. The system recommends movies based on a similarity score between movies.

## Features
- **Content-based Filtering**: Recommends movies similar to the user's input.
- **Interactive Interface**: Built with Streamlit for a user-friendly experience.
- **Pre-trained Model**: Utilizes a pre-trained model for fast recommendations.

## How It Works
1. Users input a movie title.
2. The system retrieves similar movies using cosine similarity from a preprocessed dataset.
3. Recommendations are displayed with key details about the movies.

## Files Included
- **app.py**: The main application file for the Streamlit app.
- **movies.pkl**: Pickle file containing movie data.
- **similarity.pkl**: Precomputed similarity matrix.
- **movies_dict.pkl**: Dictionary file of movies.

## Installation
To run this project locally:
1. Clone the repository:
   ```bash
   git clone https://github.com/satyamsaurabh12/movies_recomendation.git
