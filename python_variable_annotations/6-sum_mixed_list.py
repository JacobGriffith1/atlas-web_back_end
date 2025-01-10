#!/usr/bin/env python3
'''
## 6. Complex Types - Mixed List
Write a type-annotated function ```sum_mixed_list```
which takes a list ```mxd_lst``` of integers and floats
and returns their sum as a float.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Type-annotated function that takes a mixed list of floats and
    integers and returns their sum as a float

    @mxd_lst: Mixed list
    Return: The sum of the mixed list as a float
    '''
    sum = 0
    for n in mxd_lst:
        sum += n

    return sum
