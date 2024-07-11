#!/usr/bin/env python3
"""
below is class LFUCache that
inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching
class LFUCache(BaseCaching):
    """
    LRUCache class provides a caching mechanism
    """
    freq_Count = {}

    def __init__(self):
        """
        Initialize the LFUCache
        """
        super().__init__()

    def put(self, key, item):
        """
        add to the dictionary self.cache_data
        the item value for the key
        """
        if key and item:
            self.cache_data[key] = item

            if key in self.freq_Count.keys():
                count = self.freq_Count[key]
                del self.freq_Count[key]
                self.freq_Count[key] = count + 1
            else:
                self.freq_Count[key] = 0

            if len(self.freq_Count) > self.MAX_ITEMS:
                keys = list(self.freq_Count.keys())[:-1]
                values = list(self.freq_Count.values())[:-1]
                reckey = values.index(min(values))
                frst_key = keys[reckey]
                print(f'DISCARD: {frst_key}')
                del self.freq_Count[frst_key]
                del self.cache_data[frst_key]

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data
        returns None.
        """
        itm = self.cache_data.get(key)

        if itm:
            count = self.freq_Count[key]
            del self.freq_Count[key]
            self.freq_Count[key] = count + 1

        return itm
