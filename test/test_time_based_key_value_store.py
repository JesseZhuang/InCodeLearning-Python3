import unittest

from algorithm.binary_search.time_based_key_value_store import TimeMap, TimeMap2


class TestTimeBasedKeyValueStore(unittest.TestCase):
    def setUp(self):
        self.solutions = [TimeMap, TimeMap2]

    def test_basic(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                tm = cls()
                tm.set("foo", "bar", 1)
                self.assertEqual(tm.get("foo", 1), "bar")
                self.assertEqual(tm.get("foo", 3), "bar")
                tm.set("foo", "bar2", 4)
                self.assertEqual(tm.get("foo", 4), "bar2")
                self.assertEqual(tm.get("foo", 5), "bar2")

    def test_timestamp_before_any_set(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                tm = cls()
                tm.set("foo", "bar", 2)
                self.assertEqual(tm.get("foo", 1), "")

    def test_key_not_found(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                tm = cls()
                self.assertEqual(tm.get("missing", 1), "")

    def test_multiple_keys(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                tm = cls()
                tm.set("a", "v1", 1)
                tm.set("b", "v2", 1)
                self.assertEqual(tm.get("a", 1), "v1")
                self.assertEqual(tm.get("b", 1), "v2")
                self.assertEqual(tm.get("a", 2), "v1")

    def test_exact_timestamp_match(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                tm = cls()
                tm.set("key", "a", 1)
                tm.set("key", "b", 2)
                tm.set("key", "c", 3)
                self.assertEqual(tm.get("key", 2), "b")

    def test_large_gap(self):
        for cls in self.solutions:
            with self.subTest(cls=cls.__name__):
                tm = cls()
                tm.set("k", "first", 1)
                tm.set("k", "second", 1000000)
                self.assertEqual(tm.get("k", 500000), "first")
                self.assertEqual(tm.get("k", 1000000), "second")


if __name__ == "__main__":
    unittest.main()
