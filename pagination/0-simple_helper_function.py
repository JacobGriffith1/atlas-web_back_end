#!/usr/bin/env python3
'''
Module for a pagination helper function
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Helper function for pagination

    @page: The page number
    @page_size: The amount of results per page
    Return: A tuple of the starting and end indexes for that page
    '''
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
