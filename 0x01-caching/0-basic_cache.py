#!/usr/bin/env python3
"""
Below is a class BasicCache
that inherits from BaseCaching and is a caching system
Returns:  value in self.cache_data linked to key.
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class provides a simple caching mechanism
    this is where items are stored ina dict
    """
    def __init__(self):
        """
        Initialize the BasicCache instance
        """
        super().__init__()

    def put(self, key, item):
        """
        dictionary from the parent class
        Args:
            key (str): The key under which the item should be stored.
            item (any): The item to be stored in the cache.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by its key.
        Returns: The item stored under the key
        or none if dont exist
        """
        return self.cache_data.get(key)
