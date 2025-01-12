#!/usr/bin/env python3
'''
## 1. Let's Execute Multiple Coroutines at the Same Time with Async
Import ```wait_random``` from the previous python file that you've written
and write an async routine called ```wait_n``` that takes in 2 int arguments
(in this order): ```n``` and ```max_delay```. You will spawn
```wait_random``` ```n``` times with the specified ```max_delay```.

```wait_n``` should return the list of all the delays (float values).
The list of the delays should be in ascending order without using
```sort()``` because of concurrency.
'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Function that calls wait_random n times asynchronously

    @n: Number of times wait_random will be called
    @max_delay: Maximum delay for wait_random
    Return: List of wait times as float values
    '''
    taskList = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    timeList = []
    for task in asyncio.as_completed(taskList):
        time: float = await task
        timeList.append(time)
    return timeList
