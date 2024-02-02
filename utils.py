"""Utility functions"""

import argparse

import pandas as pd

import constants as C


def clean_data(movies: pd.DataFrame) -> pd.DataFrame:
    """_summary_

    Args:
        movies (pd.DataFrame): A DataFrame containing the movies data.

    Returns:
        pd.DataFrame: _description_
    """
    movies["IMDB Score"] = movies["IMDB Score"].fillna(0.0)  # Data cleaning

    # If Genre is empty, fill in the default 0.0 value.
    movies["Genre"] = movies["Genre"].fillna("")

    # Create list of genres separated by `|`.
    movies["Genre"] = movies["Genre"].str.split("|")

    return movies


def read_csv_file(file_name: str, header: int = 0) -> pd.DataFrame:
    """Get file name with path and return a DataFrame containing the movies data.

    Args:
        file_name: The name of the file with the path to read the data.
    Returns:
        pd.DataFrame: A DataFrame containing the movies data.
    """
    return pd.read_csv(file_name, sep=",", header=header, encoding=C.DEFAULT_ENCODING)


def load_movies() -> pd.DataFrame:
    """Read movies data from csv file and return as a data frame after preprocessing.

    Returns:
        movies (pd.DataFrame): A DataFrame containing the movies data.
    """
    movies = pd.read_csv(C.FILE, sep=",", header=0, encoding=C.DEFAULT_ENCODING)

    return clean_data(movies)


def parse_arguments():
    """Command-line argument parsing.

    Returns:
        args: A list of arguments.
    """
    parser = argparse.ArgumentParser(add_help=True)

    parser.add_argument(
        "--dir",
        "-d",
        type=str,
        help="Enter the file path.",
        required=True,
    )

    parser.add_argument(
        "--file",
        "-f",
        type=str,
        help="Enter the file name.",
        required=True,
    )

    return parser.parse_args()
