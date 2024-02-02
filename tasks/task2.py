"""Task 2 - Advanced Manipulation

- Implement a function to calculate and display the average score of all movies in the data
structure.
- Create a function to find and display the top N movies with the highest score
"""

import logging

import pandas as pd

import constants as C
from utils import load_movies


def calculate_average_score(movies: pd.DataFrame) -> float:
    """Calculate and display average score. Assumed that movies without score
    values have 0.0 ratings.

    Args:
        movies (pd.DataFrame): A DataFrame containing the movies data.

    Returns:
        average_score (float): Average score of all movies.
    """

    if movies.empty:
        logging.info(
            "Task2: Average score cannot be calculated because no movies were found."
        )
        print(
            "Task 2: Average score cannot be calculated because no movies were found."
        )
        raise ValueError("Average score cannot be calculated because no movies were found.")

    # If we want to skip 0.0 valued movies, instead of taking as 0.0.
    # movies_with_score = movies[movies["IMDB Score"] != .0]
    # average_score = movies_with_score["IMDB Score"].mean()

    return movies["IMDB Score"].mean()


def find_top_n_movies(movies: pd.DataFrame, n: int) -> pd.DataFrame:
    """Find and display the top N movies with the highest score.

    Args:
        movies (pd.DataFrame): A DataFrame containing the movies data.
        n (int): The number of movies with the highest score to display.

    Returns:
        movies (pd.DataFrame): A DataFrame containing the movies data with
        the highest n score.
    """
    if n < 1:
        raise ValueError(f"n is {n}, but it must be greater than zero.")

    sorted_movies = movies.sort_values(by="IMDB Score", ascending=False)

    return sorted_movies.head(n)


def run():
    """Task 2 - Main execution"""
    movies = load_movies()
    print(f"Average score of all movies given scores: {calculate_average_score(movies):.2f}\n")
    print("---------\n")
    print(f"Top {C.TOP_N} movies:\n\n{find_top_n_movies(movies, C.TOP_N)}\n")
