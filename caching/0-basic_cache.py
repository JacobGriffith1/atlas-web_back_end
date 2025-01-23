#!/usr/bin/env python3
'''
Basic caching module
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''
    Basic caching class, inherits from BaseCaching
    '''
    def put(self, key, item):
        '''
        Method puts a new k/v pair 
        '''
        if (key and item):
            self.cache_data[key] = item
    
    def get(self, key):
        '''
        Method returns value linked to key
        '''
        if key:
            for k in self.cache_data.keys():
                if k == key:
                    return self.cache_data.get(key)
        return None
