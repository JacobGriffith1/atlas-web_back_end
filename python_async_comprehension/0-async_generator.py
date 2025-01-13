#!/usr/bin/env python3
'''
## 0. Async Generator
Write a coroutine called ```async_generator``` that takes no arguments.

The coroutine will loop 10 times, each time asynchronously waiting 1 second,
then yielding a random number between 0 and 10. Use the ```random``` module.
'''
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]: # type: ignore
    '''
    Function creates a generator that yields a 
    random number between 0 and 10
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
