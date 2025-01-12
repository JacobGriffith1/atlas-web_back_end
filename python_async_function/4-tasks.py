#!/usr/bin/env python3
'''
## 4. Tasks
Take the code from ```wait_n```. The code is nearly identical to
```wait_n``` except ```task_wait_random``` is being called.
'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Function that calls wait_random n times asynchronously

    @n: Number of times wait_random is to be called
    @max_delay: Maximum wait time fed to wait_random
    Return: List of wait times as a float
    '''
    timeList = []
    for _ in range(n):
        timeList.append(task_wait_random(max_delay))
    return [await time for time in asyncio.as_completed(timeList)]
