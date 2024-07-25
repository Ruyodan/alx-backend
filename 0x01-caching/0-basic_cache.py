#!/usr/bin/env python3
"""Module conatining class with a basic caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Class defining methods th@ assign to dict & return data from it"""

    def put(self, key, item):
        """Function that assigns data to dictionary(cache)"""

        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Function that returns value from dictionary(cache)"""

        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
