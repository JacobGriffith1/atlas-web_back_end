#!/usr/bin/env python3
'''Redis Basic'''
import redis
from uuid import uuid4
from typing import Callable, Optional, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''Decorator counts how many times methods of Cache are called'''
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''Wrapper for count_calls decorator'''
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    '''Decorator stores the history of i/o for a particular function'''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''Wrapper for call_history decorator'''
        inputs = str(args)
        self._redis.rpush(method.__qualname__ + ':inputs', inputs)

        outputs = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ':outputs', outputs)
        return outputs
    return wrapper

def replay(func: Callable):
    '''Function displays the history of a particular function's calls'''
    r = redis.Redis()
    func_name = func.__qualname__
    n_calls = r.get(func_name)
    try:
        n_calls = n_calls.decode('utf-8')
    except Exception:
        n_calls = 0
    print(f'{func_name} was called {n_calls} times:')

    inps = r.lrange(func_name + ":inputs", 0, -1)
    outs = r.lrange(func_name + ":outputs", 0, -1)

    for i, o in zip(inps, outs):
        try:
            i = i.decode('utf-8')
        except Exception:
            i = ""
        try:
            o = o.decode('utf-8')
        except Exception:
            o = ""

        print(f'{func_name}(*{i}) -> {o}')


class Cache:
    '''Caching class'''

    def __init__(self):
        '''Constructor'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Method generates a random key, stores the input data in Redis using
        the random key, and returns the key.
        '''
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        '''
        Method takes a 'key' string argument and an optional 'Callable'
        argument named 'fn'. This callable will be used to convert the data
        back to the desired format
        '''
        val = self._redis.get(key)
        if fn:
            val = fn(val)
        return val

    def get_str(self, key: str) -> str:
        '''Parameterizes a value from redis to str'''
        val = self._redis.get(key)
        return val.decode('utf-8')

    def get_int(self, key: str) -> int:
        '''Parameterizes a value from redis to int'''
        val = self._redis.get(key)
        try:
            val = int(val.decode('utf-8'))
        except Exception:
            val = 0
        return val
