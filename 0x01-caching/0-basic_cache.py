#!/usr/bin/env python3
"""Basic caching module.

This module defines the BasicCache class, which represents an object that allows
storing and retrieving items from a dictionary.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary.
    """
    def put(self, key, item):
        """Adds an item in the cache.

        Args:
            key: The key to use for the item.
            item: The item to add to the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.

        Args:
            key: The key to use for the item.

        Returns:
            The item associated with the given key, or None if the key is not
            in the cache.
        """
        return self.cache_data.get(key, None)