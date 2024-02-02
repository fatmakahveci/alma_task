"""Tests for movie management"""

import unittest
from io import StringIO

import pandas as pd

import tasks.task2 as task2
import tasks.task3 as task3


class TestTasks(unittest.TestCase):

    def setUp(self):
        self.csv_file = (
            "imdbId,Imdb Link,Title,IMDB Score,Genre,Poster\n"
            '114709,http://www.imdb.com/title/tt114709,Toy Story (1995),8.3,Animation|Adventure|Comedy,"https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg"\n'
            '113497,http://www.imdb.com/title/tt113497,Jumanji (1995),6.9,Action|Adventure|Family,"https://images-na.ssl-images-amazon.com/images/M/MV5BZTk2ZmUwYmEtNTcwZS00YmMyLWFkYjMtNTRmZDA3YWExMjc2XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR10,0,182,268_AL_.jpg"\n'
            '113228,http://www.imdb.com/title/tt113228,Grumpier Old Men (1995),6.6,Comedy|Romance,"https://images-na.ssl-images-amazon.com/images/M/MV5BMjQxM2YyNjMtZjUxYy00OGYyLTg0MmQtNGE2YzNjYmUyZTY1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg"\n'
        )

        self.csv_file_io = StringIO(self.csv_file)
        self.movie_df = pd.read_csv(self.csv_file_io, sep=",")

        self.empty_movie_df = pd.DataFrame()

    def test__when_single_n__find_top_n_movies(self):
        top_movie = task2.find_top_n_movies(self.movie_df, 1)

        self.assertEqual(len(top_movie), 1)
        self.assertEqual(top_movie["Title"].iloc[0], "Toy Story (1995)")
        self.assertEqual(top_movie["IMDB Score"].iloc[0], 8.3)

    def test__when_multiple_n__find_top_n_movies(self):

        top_2_movies = task2.find_top_n_movies(self.movie_df, 2)

        self.assertEqual(len(top_2_movies), 2)
        self.assertEqual(top_2_movies["Title"].iloc[0], "Toy Story (1995)")
        self.assertEqual(top_2_movies["IMDB Score"].iloc[0], 8.3)

        self.assertEqual(top_2_movies["Title"].iloc[1], "Jumanji (1995)")
        self.assertEqual(top_2_movies["IMDB Score"].iloc[1], 6.9)

    def test__when_negative_n__find_top_n_movies(self):

        with self.assertRaises(ValueError):
            self.assertRaises(task2.find_top_n_movies(self.movie_df, -2))

        with self.assertRaises(ValueError):
            self.assertRaises(task2.find_top_n_movies(self.movie_df, 0))

    def test__when_movie_file_is_empty(self):
        with self.assertRaises(ValueError):
            self.assertRaises(task2.calculate_average_score(self.empty_movie_df))

    def test__when_genre_is_not_found(self):
        with self.assertRaises(task3.GenreNotFound):
            self.assertRaises(
                task3.find_movies_by_genre(self.movie_df, genre="Apple"), None
            )


if __name__ == "__main__":
    unittest.main()
