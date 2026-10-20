import unittest
from unittest import mock

from notes.cache import Cache


class CacheTest(unittest.TestCase):
    def test_hit(self):
        cache = Cache(ttl=10)
        cache.put("k", 1)
        self.assertEqual(cache.get("k"), 1)

    def test_miss_raises(self):
        with self.assertRaises(KeyError):
            Cache(ttl=10).get("k")

    def test_expiry(self):
        cache = Cache(ttl=10)
        with mock.patch("notes.cache.time.monotonic", return_value=100.0):
            cache.put("k", 1)
        with mock.patch("notes.cache.time.monotonic", return_value=110.0):
            with self.assertRaises(KeyError):
                cache.get("k")
