#!/usr/bin/env python3
'''Redis Basic'''
import redis
from uuid import uuid4
from typing import Union


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
