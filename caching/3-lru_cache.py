#!/usr/bin/env python3
'''
LRU caching module
'''
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''
    LRU caching class, inherits from BaseCaching
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
            if key in self.keys:
                self.keys.remove(key)
                self.keys.append(key)
            else:
                self.keys.append(key)
            if len(self.keys) > self.MAX_ITEMS:
                dis = self.keys.pop(0)
                del self.cache_data[dis]
                print('DISCARD: {}'.format(dis))

    def get(self, key):
        '''
        Method returns value linked to key
        '''
        if key and key in self.keys:
            self.keys.remove(key)
            self.keys.apppend(key)
            return self.cache_data(key)
        return None
