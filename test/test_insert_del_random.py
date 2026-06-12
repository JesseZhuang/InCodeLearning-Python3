import unittest

from algorithm.hash.insert_del_random import RandomizedSet


class TestRandomizedSet(unittest.TestCase):
    def test_example1(self):
        rs = RandomizedSet()
        self.assertTrue(rs.insert(1))
        self.assertFalse(rs.remove(2))
        self.assertTrue(rs.insert(2))
        self.assertIn(rs.getRandom(), {1, 2})
        self.assertTrue(rs.remove(1))
        self.assertFalse(rs.insert(2))
        self.assertEqual(rs.getRandom(), 2)

    def test_insert_duplicate(self):
        rs = RandomizedSet()
        self.assertTrue(rs.insert(5))
        self.assertFalse(rs.insert(5))

    def test_remove_nonexistent(self):
        rs = RandomizedSet()
        self.assertFalse(rs.remove(99))

    def test_insert_remove_reinsert(self):
        rs = RandomizedSet()
        self.assertTrue(rs.insert(10))
        self.assertTrue(rs.remove(10))
        self.assertTrue(rs.insert(10))
        self.assertEqual(rs.getRandom(), 10)

    def test_multiple_elements_random_distribution(self):
        rs = RandomizedSet()
        for i in range(100):
            rs.insert(i)
        results = {rs.getRandom() for _ in range(500)}
        self.assertGreater(len(results), 50)

    def test_remove_last_element_then_insert(self):
        rs = RandomizedSet()
        rs.insert(1)
        rs.insert(2)
        rs.insert(3)
        rs.remove(3)
        self.assertTrue(rs.insert(3))
        self.assertIn(rs.getRandom(), {1, 2, 3})

    def test_remove_first_element(self):
        rs = RandomizedSet()
        rs.insert(1)
        rs.insert(2)
        rs.insert(3)
        rs.remove(1)
        for _ in range(50):
            self.assertIn(rs.getRandom(), {2, 3})

    def test_single_element(self):
        rs = RandomizedSet()
        rs.insert(42)
        self.assertEqual(rs.getRandom(), 42)
        self.assertTrue(rs.remove(42))
        self.assertFalse(rs.remove(42))


if __name__ == "__main__":
    unittest.main()
