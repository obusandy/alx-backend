#!/usr/bin/env python3
"""

"""
import csv
from typing import List, Tuple


class Server:
    """
    The above Server class to paginate a dataset from a CSV file.
    Attributes:
    DATA_FILE (str): The path to the CSV file containing the dataset.
    __dataset (List[List]): A cached list
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
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

    def index_range(self, page: int, page_size: int) -> Tuple[int]:
        start_indx = (page - 1) * page_size
        end_indx = page * page_size

        return (start_indx, end_indx)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a paginated section of the dataset starting from the specified indx.
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        index_range = self.index_range(page, page_size)
        start_indx, end_indx = index_range[0], index_range[1]

        dataset = self.dataset()
        try:
            datast = [dataset[indx] for indx in range(start_indx, end_indx)]
        except IndexError:
            datast = []

        return datast

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        a get_hyper method that takes the same args (and defaults) as get_page and
        Returns: a dict containing the following key-value pairs
        """
        datast = self.get_page(page, page_size)
        dataset = self.dataset()
        total_pages = ((len(dataset) - 1) // page_size) + 1
        # get the index to start and end at
        respns = {
            "page_size": len(datast),
            "page": page,
            "data": datast,
            "next_page": None if (page >= total_pages) else page + 1,
            "prev_page": None if (page - 1 == 0) else page - 1,
            "total_pages": total_pages
        }

        return respns