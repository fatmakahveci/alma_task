"""Movie Manager System main function"""

import logging
from os import path

import constants as C
from tasks import task1, task2, task3, task4, task5
from utils import parse_arguments

if __name__ == "__main__":
    args = parse_arguments()

    logging.basicConfig(
        filename=path.join(C.PATH, "movies.log"),
        level=logging.INFO,
        encoding="utf-8",
        format="%(asctime)s %(levelname)s %(message)s",
    )
    logging.info("------------------------------------------------------------")
    logging.info("The program is running with the following arguments: %s", args)

    print("\n-Task #1-----------------------------------------------------------\n")
    task1.run()  # Data Loading
    logging.info("Task 1 is completed.")

    print("-Task #2-----------------------------------------------------------\n")
    task2.run()  # Advanced Manipulation
    logging.info("Task 2 is completed.")

    print("-Task #3-----------------------------------------------------------\n")
    task3.run()  # Data Operations
    logging.info("Task 3 is completed.")

    print("-Task #4-----------------------------------------------------------\n")
    task4.run()  # Additional Complexity
    logging.info("Task 4 is completed.")

    print("-Task #5-----------------------------------------------------------\n")
    task5.run()  # Chart Creation
    logging.info("Task 5 is completed.")
    print("-------------------------------------------------------------------\n")

    logging.info("------------------------------------------------------------")
