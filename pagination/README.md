# Pagination
Project for Atlas School

## Learning Objectives
At the end of this project, understand:
- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Tasks

## 0. Simple Helper Function
Write a function named ```index_range``` that takes two integer arguments ```page``` and ```page_size```.
The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.
Page numbers are 1-indexed, i.e. the first page is page 1.

## 1. Simple Pagination
Copy ```index_range``` from the previous task and the following class into your code
```
import csv
import math
from typing import List


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
            pass
```
Implement a method named ```get_page``` that takes two integer arguments ```page``` with default value 1 and ```page_size``` with default value 10.
- You have to use this [CSV file](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250126%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20250126T012737Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5eac7a961802408ab00ad868b278c35dc604088aa612583c45dae2c6aee9a6c9) (same as the one presented at the top of the project)
- Use ```assert``` to verify that both arguments are integers greater than 0.
- Use ```index_range``` to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset (i.e. the correct list of rows).
- If the input arguments are out of range for the dataset, and empty list should be returned.

## 2. Hypermedia Pagination
Replicate code from the previous task.
Implement a ```get_hyper``` method that takes the same arguments (and defaults) as ```get_page``` and returns a dictionary containing the following key-value pairs:
- ```page_size```: The length of the returned dataset page
- ```page```: The current page number
- ```data```: The dataset page (equivalent to return from previous task)
- ```next_page```: Number of the next page, ```None``` if no next page
- ```prev_page```: Number of the previous page, ```None``` if no previous page
- ```total_pages```: The total number of pages in the dataset as an integer
Make sure to reuse ```get_page``` in your implementation.
You can use the ```math``` module if necessary.

## 3. Deletion-Resilient Hypermedia Pagination
The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.
Start ```3-hypermedia_del_pagination.py``` with this code:
```
#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


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
            pass
```
Implement a ```get_hyper_index``` method with two integer arguments: ```index``` with a ```None``` default value and ```page_size``` with default value of 10.
- The method should return a dictionary with the following key-value pairs:
    - ```index```: The current start index of the return page. That is the index of the first item in the current page. For example if requesting page 3 with ```page_size``` 20, and no data was removed from the dataset, the current index should be 60.
    - ```next_index```: The next index to query with. That should be the index of the first item after the last item on the current page.
    - ```page_size```: The current page size
    - ```data```: The actual page of the dataset
**Requirements/Behavior**:
- Use ```assert``` to verify that ```index``` is in a valid range.
- If the user queries index 0, ```page_size``` 10, they will get rows indexed 0 to 9 included.
- If they request the next index (10) with ```page_size``` 10, but rows 3, 6 and 7 were deleted, the user should still recieve rows indexed 10 to 19 included.