import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import constants
from utils import configure_dataset, load_movies, parse_arguments


class DatasetSelectionTests(unittest.TestCase):
    def test_cli_selects_the_requested_file_and_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            dataset = Path(directory) / "custom.csv"
            dataset.write_text("Title,IMDB Score,Genre\nSelected,8.5,Drama\n", encoding="utf-8")
            args = parse_arguments(["--dir", directory, "--file", "custom.csv"])
            with patch.object(constants, "PATH", "unused"), patch.object(constants, "FILE", "unused"):
                configure_dataset(args)
                self.assertEqual(Path(constants.FILE), dataset.resolve())
                self.assertEqual(load_movies().iloc[0]["Title"], "Selected")

    def test_missing_dataset_has_a_clear_cli_error(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(SystemExit) as error:
                parse_arguments(["--dir", directory, "--file", "missing.csv"])
            self.assertEqual(error.exception.code, 2)

    def test_filename_cannot_override_directory(self):
        with self.assertRaises(SystemExit):
            parse_arguments(["--dir", ".", "--file", "../movies.csv"])
