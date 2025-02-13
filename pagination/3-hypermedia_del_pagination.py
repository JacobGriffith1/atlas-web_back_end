#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''
        Method returns a dict of data from the index up to page_size
        '''
        assert type(index) is int and index >= 0
        assert type(page_size) is int and page_size > 0
        assert index < len(self.dataset())
        hyperDict = {}
        if (index + page_size) > len(self.dataset()):
            next_index = None
        else:
            next_index = index + page_size
        page_list = []
        data = self.dataset()
        for i in range(index, index + page_size):
            page_list.append(data[i])
        hyperDict["index"] = index
        hyperDict["next_index"] = next_index
        hyperDict["page_size"] = page_size
        hyperDict["data"] = page_list
        return hyperDict
