#!/usr/bin/env python3
'''
## 1. Basic Annotations - Concat
Write a type-annotated function ```concat```
that takes a string ```str1``` and a string ```str2```
as arguments and returns a concatenated string.
'''


def concat(str1: str, str2: str) -> str:
    '''
    Type-annotated function that takes two strings
    and returns them as a concatenated string

    @str1: First string
    @str2: Second string
    Return: Concatenated string composed of variable strings
    '''
    return str1 + str2
