#!/usr/bin/env python3
"""pagination o.
using the prev. code
index_range
"""
import csv
import math
from typing import List, Tuple

def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    It includes a Server class for handling pagination.
    Calculate the start and end index for a given page and page size.

    Args:
    - page (int): The current page no (1).
    - page_size (int): The no of items(10)
    """
    start_indx = (page - 1) * page_size
    end_indx = page * page_size

    return (start_indx, end_indx)

class Server:
    """
    Server class to paginate a dataset from a CSV file.
    Attributes:
    DATA_FILE (str): The path to the CSV file containing the dataset.
    __dataset (List[List]): A cached list
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset from the CSV file
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as fl:
                reader = csv.reader(fl)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of the dataset
        Args:
        - page (int): The current page no (default is 1).
        - page_size (int): The no (10)
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        paginate_range = index_range(page, page_size)
        start, end = paginate_range[0], paginate_range[1]
        dataset = self.dataset()

        try:
            data = [dataset[indx] for indx in range(start, end)]
        except IndexError:
            data = []

        return data
