#!/usr/bin/env python3
'''
Basic caching module
'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''
    FIFO caching class, inherits from BaseCaching
    '''
    def __init__(self):
        '''
        Inititalize method
        '''
        super().__init__()
        self.keys = []

    def put(self, key, item):
        '''
        Method puts a new k/v pair in cache
        '''
        if (key and item):
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.keys) > self.MAX_ITEMS:
                dis = self.keys.pop(0)
                del self.cache_data[dis]
                print('DISCARD: {}'.format(dis))

    def get(self, key):
        '''
        Method returns value linked to key
        '''
        if key:
            for k in self.cache_data.keys():
                if k == key:
                    return self.cache_data.get(key)
        return None
