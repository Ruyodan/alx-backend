#!/usr/bin/env python3
"""Module conatining class with a LIFO(Last In First Out) caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Class defining methods th@ assign to dict & return data from it"""

    def __init__(self):
        """Function to initialise class intances"""

        super().__init__()
        self.last_item = ""

    def put(self, key, item):
        """Function that assigns data to dictionary(cache)"""

        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.last_item))
                self.cache_data.pop(self.last_item)
            self.last_item = key

    def get(self, key):
        """Function that returns value from dictionary(cache)"""

        if key is None or self.cache_data.get(key) is None:
            return None

        if key in self.cache_data:
            return self.cache_data[key]
