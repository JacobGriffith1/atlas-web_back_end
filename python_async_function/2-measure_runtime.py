#!/usr/bin/env python3
'''
## 2. Measure the Runtime
From the previous file, import ```wait_n``` into ```2-measure_runtime.py```.

Create a ```measure_time``` function with integers ```n``` and
```max_delay``` as arguments that measures the total execution time
for ```wait_n(n, max_delay)```, and returns ```total_time / n```.
Your function should return a float.

Use the ```time``` module to measure an approximate elapsed time.
'''
import asyncio, time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Function that measures the execution time off wait_n

    @n: Number of times to execute wait_random
    @max_delay: Maximum wait time fed to wait_random
    Return: Total execution time divided by n, as a float
    '''
    startTime = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    totalTime = time.perf_counter() - startTime
    return totalTime / n
