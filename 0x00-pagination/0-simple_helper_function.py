#!/usr/bin/env python3
"""
a function named index_range that takes two
int args page and page_size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for the given page and page size.
    Returns: Tuple: A tuple containing the start index
    and the end index
    """
    end_indx = page * page_size
    start_indx = end_indx - page_size

    return (start_indx, end_indx)