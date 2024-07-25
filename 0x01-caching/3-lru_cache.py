#!/usr/bin/env python3
"""Module conatining class with a LRU(Least Recently Used) caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Class defining methods th@ assign to dict & return data from it"""

    def __init__(self):
        """Function to initialise class intances"""

        super().__init__()
        self.head = ""
        self.tail = ""

        self.previous = {}
        self.next = {}

        self.cache_line(self.head, self.tail)

    def cache_line(self, head, tail):
        """Function that handles cache line instances"""

        self.next[head] = tail
        self.previous[tail] = head

    def pop(self, key):
        """Function to pop data out of dictionary(cache)"""

        self.cache_line(self.previous[key], self.next[key])
        del self.previous[key]
        del self.next[key]
        del self.cache_data[key]

    def push(self, key, item):
        """Function to push data onto dictionary(cache)"""

        self.cache_data[key] = item
        self.cache_line(self.previous[self.tail], key)
        self.cache_line(key, self.tail)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.next[self.head]))
            self.pop(self.next[self.head])

    def put(self, key, item):
        """Function that assigns data to dictionary(cache)"""

        if key and item:
            if key in self.cache_data:
                self.pop(key)
            self.push(key, item)

    def get(self, key):
        """Function that returns value from dictionary(cache)"""

        if key is None or self.cache_data.get(key) is None:
            return None

        if key in self.cache_data:
            res = self.cache_data[key]
            self.pop(key)
            self.push(key, res)
            return res
