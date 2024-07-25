#!/usr/bin/env python3
"""Module conatining class with a LFU(Least Frequently Used) caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Class defining methods th@ assign to dict & return data from it"""

    def __init__(self):
        """Function to initialise class intances"""

        super().__init__()
        self.block = []
        self.frequency = {}

    def put(self, key, item):
        """Function that assigns data to dictionary(cache)"""

        if key and item:
            counter = len(self.cache_data)

            if counter >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                LFU = min(self.frequency.values())
                keys = []

                for lfu_key, count in self.frequency.items():
                    if count == LFU:
                        keys.append(lfu_key)

                if len(keys) > 1:
                    LRU_LFU = {}

                    for lfu_key in keys:
                        LRU_LFU[lfu_key] = self.block.index(lfu_key)

                    discard = min(LRU_LFU.values())
                    discard = self.block[discard]
                else:
                    discard = keys[0]

                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
                del self.block[self.block.index(discard)]
                del self.frequency[discard]

            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1

            if key in self.block:
                del self.block[self.block.index(key)]

            self.block.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Function that returns value from dictionary(cache)"""

        if key is not None and key in self.cache_data.keys():
            del self.block[self.block.index(key)]

            self.block.append(key)
            self.frequency[key] += 1

            return self.cache_data[key]
        return None
