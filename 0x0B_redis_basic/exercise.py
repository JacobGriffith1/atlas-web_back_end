#!/usr/bin/env python3
'''Redis Basic'''
import redis
from uuid import uuid4
from typing import Callable, Optional, Union


class Cache:
    '''Caching class'''

    def __init__(self):
        '''Constructor'''
        self._redis = redis.Redis()
        self._redis.flushdb()

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
