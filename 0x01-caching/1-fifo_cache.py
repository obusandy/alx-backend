#!/usr/bin/env python3
"""
below is a class FIFOCache that
inherits from BaseCaching and is a caching system
Returns: the value in self.cache_data linked to key.
"""
BaseCaching = __import__('base_caching').BaseCaching

class FIFOCache(BaseCaching):
    """
    FIFOCache class
    First in First out
    """
    def __init__(self):
        """
        Initialize the FIFOCache instance
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache with the specified key
        key or item is None, this method should not do anything.
        """
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                frst_key = list(self.cache_data.keys())[0]
                del self.cache_data[frst_key]
                print(f'DISCARD: {frst_key}')

    def get(self, key):
        """
        Returns: the value in self.cache_data linked to key.
        If key is None or if the key doesnt exist in self.cache_data,
        return None.
        """
        return self.cache_data.get(key)
