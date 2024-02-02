"""Task 5 - Chart Creation

- Implement a function to create a chart visually representing movie score distribution. You can
choose any appropriate chart type (e.g., bar chart, histogram).
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from utils import load_movies


def draw_plot(movies: pd.DataFrame) -> None:
    """Draw a plot to display the distribution of IMDB Scores.

    Args:
        movies (pd.DataFrame): A DataFrame containing the movies data.
    """
    plt.figure(figsize=(12, 6))
    sns.histplot(data=movies, x="IMDB Score", bins=40, kde=False)

    plt.title("Distribution of IMDb Scores with Counts")

    plt.xlim(0, 10)
    plt.xlabel("Score")
    plt.ylim(0, plt.ylim()[1])
    plt.ylabel("Count")

    plt.show()  # savefig() can be used to save the figure.


def run():
    """Task 5 - Main execution"""

    movies = load_movies()
    draw_plot(movies)
    print("The plot shows the rating distribution.")
    print("Data distribution will look like a normal distribution if there is enough data.")
