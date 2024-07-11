#!/usr/bin/env python3
"""
Below is a class MRUCache that
inherits from BaseCaching and is a caching system
Returns: the value in self.cache_data linked to key.
else None
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class\ Most Recently Used
    eviction policy.
    """
    leastrusd = []

    def __init__(self):
        """
        Initialize the MRUCache
        """
        super().__init__()

    def put(self, key, item):
        """
        add to the dict self.cache_data the item value for the key.
        Args:
            key (str): The key under which the item should be stored.
            item: The item to be stored in the cache.
        """
        if key and item:
            self.cache_data[key] = item

            if key in self.leastrusd:
                self.leastrusd.append(key)
                self.leastrusd.remove(key)
            else:
                self.leastrusd.append(key)

            if len(self.leastrusd) > self.MAX_ITEMS:
                del self.cache_data[self.leastrusd[-2]]
                print(f'DISCARD: {self.leastrusd[-2]}')
                self.leastrusd.pop(-2)

    def get(self, key):
        """
        Returns: the value in self.cache_data linked to key.
        If key is None or if the key doesnt exist in self.cache_data
        returns None.
        """
        item = self.cache_data.get(key)

        if item:
            self.leastrusd.append(key)
            self.leastrusd.remove(key)

        return item
