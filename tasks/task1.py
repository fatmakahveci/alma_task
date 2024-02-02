"""Task 1 - Data Loading

- Write a Python script to read the contents of the CSV file that contains
the movies and load the movie data into an appropriate data structure.
(`utils.py - load_movies()`)
- Display the total number of movies in the CSV file.
"""

from utils import load_movies


def run() -> None:
    """Task 1 - Main execution"""

    movies = load_movies()
    print(f"Total number of the movies: {movies.shape[0]}\n")
