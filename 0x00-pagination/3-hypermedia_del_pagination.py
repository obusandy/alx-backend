#!/usr/bin/env python3
"""
A module for paginating and indexing a
dataset from a CSV file.
"""

import csv
import math
from typing import List, Dict


class Server:
    """
    Server class to paginate a dtbs of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the DataServer instance with empty
        dataset and indexed dataset
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset from the CSV file
         Returns:
        - List[List]: A list of rows from the CSV file
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Load and cache the indexed dataset if it hasn't been loaded yet.
        Returns:
        - Dict[int, List]: A dictionary
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                indx: dataset[indx] for indx in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> dict:
        """
         Get a paginated section of the dataset starting from the specified indx
          Args:
        - start_index (int): The starting index for the pagination
        (default is 0).
        - page_size (int): The number of items per page
        """
        assert type(index) == int and index <= len(self.dataset())

        dataset = self.indexed_dataset()

        data = []
        crrnt_indx = 0
        for key, value in dataset.items():
            if key >= index and crrnt_indx < page_size:
                crrnt_indx += 1
                data.append(value)
                continue

            if crrnt_indx == page_size:
                next_index = key
                break

        respns = {
            "index": index if index else 0,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }

        return respns