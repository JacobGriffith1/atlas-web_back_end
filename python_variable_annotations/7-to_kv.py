#!/usr/bin/env python3
'''
## 7. Complex Types - String and Int/Float to Tuple
Write a type-annotated function ```to_kv``` that takes
a string ```k``` and an int OR float ```v``` as arguments
and returns a tuple. The first element of the tuple is the
string ```k```. The second element is the square of the
int/float ```v``` and should be annotated as a float.
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Type-annotated function that takes a string and an int or float
    and returns a tuple

    @k: The string that will be returned in the tuple (key)
    @v: An int or float that will be squared (value)
    Return: Tuple with k as the first element and square of v as
    the second element as a float
    '''
    kv = (k, v * v)
    return kv
