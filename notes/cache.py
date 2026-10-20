"""A small in-process cache whose entries expire."""
import time


class Cache:
    """Keeps each value for `ttl` seconds."""

    def __init__(self, ttl):
        self.ttl = ttl
        self._items = {}

    def get(self, key):
        """Returns the value stored under `key`.

        Raises KeyError if `key` was never stored or has expired.
        """
        value, expires = self._items[key]
        if time.monotonic() >= expires:
            del self._items[key]
            raise KeyError(key)
        return value

    def put(self, key, value):
        """Stores `value` under `key` for `ttl` seconds."""
        self._items[key] = (value, time.monotonic() + self.ttl)
