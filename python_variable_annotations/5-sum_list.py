#!/usr/bin/env python3
'''
## 5. Complex Types - List of Floats
Write a type-annotated function ```sum_list```
which takes a list ```input_list``` of floats as an argument
and returns their sum as a float.
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    Type-annotated function that takes a list of floats
    and returns its sum as a float

    @input_list: List of floats
    Return: The sum of the list as a float
    '''
    sum = 0
    for n in input_list:
        sum += n

    return sum
