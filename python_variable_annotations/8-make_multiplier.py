#!/usr/bin/env python3
'''
## 8. Complex Types - Functions
Write a type-annotated function ```make_multiplier``` that takes
a float ```multiplier``` as an argument and returns a function
that multiplies a float by ```multiplier```.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Type-annotated function that takes a float as an argument and
    returns a function that multiplies a float by the previous float

    @multiplier: float that will be returned in the function
    Return: Function that multiplies a float by the multiplier
    '''
    def multiply(n: float) -> float:
        '''
        Function that multiplies a number by the multiplier and
        returns a float

        @n: Number to be multiplied
        Return: The product of the two floats as a float
        '''
        return n * multiplier
    
    return multiply
