"""Task 3 - Data Operations

- Implement a function to filter and display movies based on a specified genre.
- Create a function to find and display all unique genres in the movie data.
"""

import logging
from typing import List

import numpy as np
import pandas as pd

import constants as C
from utils import load_movies

class GenreNotFound(Exception):
    """Indicates that no movies were found with the given genre."""
    pass

def find_movies_by_genre(movies: pd.DataFrame, genre: str) -> pd.DataFrame:
    """Filter and display movies based on given genre.

    Args:
        movies (pd.DataFrame): A DataFrame containing the movies data.
        genre (str): Genre to filter by.

    Returns:
        movies (pd.DataFrame): A DataFrame containing the movies data filtered by their genre.
    """
    movies_by_genre = movies[movies["Genre"].apply(lambda genres: genre in genres)]

    if movies_by_genre.empty:
        error_msg = f"No movies were found with the given '{genre}' genre"
        logging.info(error_msg)
        raise GenreNotFound(error_msg)

    return movies_by_genre


def find_unique_genres(movies: pd.DataFrame) -> List[str]:
    """Find and display all unique genres in the movie data.

    Args:
        movies (pd.DataFrame): A DataFrame containing the movies data.

    Returns:
        List[str]: A list of unique Movie genres in movies.
    """
    exploded_df = movies.explode("Genre")

    uniq_genres = list(exploded_df["Genre"].unique())

    if "" in uniq_genres:
        uniq_genres.remove("")  # Clean empty genres.

    return uniq_genres


def run():
    """Task 3 - Main execution"""

    movies = load_movies()
    print(
        f"Movies selected by {C.GENRE} genre:\n{find_movies_by_genre(movies, C.GENRE)}\n"
    )

    print("-----\n")

    print(f"Unique genres: {', '.join(find_unique_genres(movies))}.\n")
