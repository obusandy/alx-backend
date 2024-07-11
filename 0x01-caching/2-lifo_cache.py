#!/usr/bin/env python3
"""
Below is a class LIFOCache that
inherits from BaseCaching and is a caching system
self.cache_data - dictionary from the parent class BaseCaching
"""
BaseCaching = __import__('base_caching').BaseCaching
class LIFOCache(BaseCaching):
    """
    LIFOCache class
    Lat in First out eviction
    """
    recntkey = None

    def __init__(self):
        """
        Initialize the LIFOCache instance
        """
        super().__init__()

    def put(self, key, item):
        """
        add to the dictionary self.cache_data the item value for the key
        If key or item is None, this method does nothing
        Args:
            key (str): The key under which the item should be stored.
            item : The item to be stored in the cache
        """
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                del self.cache_data[self.recntkey]
                print(f'DISCARD: {self.recntkey}')

            self.recntkey = key
    def get(self, key):
        """
        Returns: the value in self.cache_data linked to key.
        If key is None or if the key doesnt exist in self.cache_data,
        return None.
        """
        return self.cache_data.get(key)
