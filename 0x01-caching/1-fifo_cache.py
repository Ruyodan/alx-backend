#!/usr/bin/env python3
"""Module conatining class with a FIFO(First In First Out) caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Class defining methods th@ assign to dict & return data from it"""

    def __init__(self):
        """Function to initialise class intances"""

        super().__init__()
        self.data = {}
        self.push_in = 0
        self.pop_out = 0

    def pop(self):
        """Function to pop data out of dictionary(cache)"""

        self.pop_out += 1
        key = self.data[self.pop_out]

        del self.data[self.pop_out]
        del self.cache_data[key]

    def push(self, key, item):
        """Function to push data onto dictionary(cache)"""

        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print("DISCARD: {}".format(self.data[self.pop_out + 1]))
            self.pop()

        self.cache_data[key] = item
        self.push_in += 1
        self.data[self.push_in] = key

    def put(self, key, item):
        """Function that assigns data to dictionary(cache)"""

        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                self.push(key, item)

    def get(self, key):
        """Function that returns value from dictionary(cache)"""

        if key is None or self.cache_data.get(key) is None:
            return None

        if key in self.cache_data:
            return self.cache_data[key]
