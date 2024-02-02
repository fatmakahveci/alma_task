"""Task 4 - Additional Complexity

- Extend the program to allow users to rate movies. Implement a function to overwrite the score
of a specific movie.
- Create a function to recommend a movie based on the user's preferred genre and the highest
score in that genre.
"""

import logging

import pandas as pd

import constants as C
from utils import load_movies, read_csv_file


def update_movie_rate_by_imdb_id(
    imdb_id: int,
    rate: float,
) -> pd.Series:
    """Overwrite the score of a specific movie.

    Args:
        imdb_id (int): The IMDb ID of the movie.
        rate (float): The IMDb score of the movie.

    Returns:
        pd.Series: The updated movie details.
    """
    movies = read_csv_file(C.FILE)  # to avoid being affected by intermediate changes
    movie = movies[movies["imdbId"] == int(imdb_id)]

    if movie.empty:
        logging.info("Movie with the ID ({imdb_id}) could not be found.")
        return pd.Series()

    movies.loc[movies["imdbId"] == int(imdb_id), "IMDB Score"] = rate
    updated_movie = movies[movies["imdbId"] == imdb_id]

    movies.to_csv(C.FILE, index=False)

    return updated_movie


def recommend_a_movie_by_genre_and_highest_rate_in_genre(genre: str) -> pd.Series:
    """Return the movie, of which genre is given, with the highest rate.

    Args:
        genre (str): The genre of the movie to be recommended.

    Returns:
        pd.Series: The recommended movie details. (If not, return pd.Series).
    """
    movies = load_movies()
    exploded_movies = movies.explode("Genre")
    genre_movies = exploded_movies[exploded_movies["Genre"] == genre]

    if genre_movies.empty:
        logging.info("There is no movie to recommend with %s genre.", genre)
        return pd.Series()

    movie = genre_movies.loc[genre_movies["IMDB Score"].idxmax()]

    return movie


def run():
    """Task 4 - Main execution"""

    updated_movie = update_movie_rate_by_imdb_id(C.IMDB_ID, C.RATE)
    print(f"Movie is updated as:\n\n{updated_movie}\n")

    print("-----\n")

    recommended_movie = recommend_a_movie_by_genre_and_highest_rate_in_genre(C.GENRE)
    print(f"Recommended movie:\n\n{recommended_movie}\n")
