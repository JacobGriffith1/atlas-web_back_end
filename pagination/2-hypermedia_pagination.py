#!/usr/bin/env python3
'''
Module that returns the list of results from a page
'''
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Helper function for pagination

    @page: The page number
    @page_size: The amount of results per page
    Return: A tuple of the start and end indexes of the page
    '''
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        Get results per page
        '''
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        pageList = []
        results = self.dataset()
        indexes = index_range(page, page_size)
        try:
            for i in range(indexes[0], indexes[1]):
                pageList.append(results[i])
        except IndexError:
            pass
        return pageList

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''
        Get results per page & return a dictionary
        '''
        hyperDict = {}
        trueData = self.get_page(page, page_size)
        truePageSize =  len(trueData)
        trueTotalPages = math.ceil(len(self.dataset()) / page_size)
        if page < trueTotalPages:
            nextPage = page + 1
        else:
            nextPage = None

        if page != 1:
            prevPage = page - 1
        else:
            prevPage = None
        hyperDict["page_size"] = truePageSize
        hyperDict["page"] = page
        hyperDict["data"] = trueData
        hyperDict["next_page"] = nextPage
        hyperDict["prev_page"] = prevPage
        hyperDict["total_pages"] = trueTotalPages
        return hyperDict
