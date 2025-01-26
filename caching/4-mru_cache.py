#!/usr/bin/env python3
'''
MRU caching module
'''
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    '''
    MRU caching class, inherits from BaseCaching
    '''
    def __init__(self):
        '''
        Initialize method
        '''
        super().__init__()
        self.keys = []

    def put(self, key, item):
        '''
        Method puts a new k/v pair in cache
        '''
        if (key and item):
            self.cache_data[key] = item
            if key in self.keys:
                self.keys.remove(key)
                self.keys.append(key)
            else:
                self.keys.append(key)
            if len(self.keys) > self.MAX_ITEMS:
                index = self.MAX_ITEMS - 1
                dis = self.keys.pop(index)
                del self.cache_data[dis]
                print('DISCARD: {}'.format(dis))

    def get(self, key):
        '''
        Method returns value linked to key
        '''
        if key and key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data[key]
        return None
