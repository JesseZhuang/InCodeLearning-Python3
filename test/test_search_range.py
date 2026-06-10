import unittest

from algorithm.binary_search.search_range import Solution


class TestSearchRange(unittest.TestCase):

    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for s in self.solutions:
            self.assertEqual([3, 4], s.search_range([5, 7, 7, 8, 8, 10], 8))
            self.assertEqual([3, 4], s.search_range_builtin([5, 7, 7, 8, 8, 10], 8))

    def test_example2(self):
        for s in self.solutions:
            self.assertEqual([-1, -1], s.search_range([5, 7, 7, 8, 8, 10], 6))
            self.assertEqual([-1, -1], s.search_range_builtin([5, 7, 7, 8, 8, 10], 6))

    def test_empty(self):
        for s in self.solutions:
            self.assertEqual([-1, -1], s.search_range([], 0))
            self.assertEqual([-1, -1], s.search_range_builtin([], 0))

    def test_single_element_found(self):
        for s in self.solutions:
            self.assertEqual([0, 0], s.search_range([1], 1))
            self.assertEqual([0, 0], s.search_range_builtin([1], 1))

    def test_single_element_not_found(self):
        for s in self.solutions:
            self.assertEqual([-1, -1], s.search_range([1], 2))
            self.assertEqual([-1, -1], s.search_range_builtin([1], 2))

    def test_all_same(self):
        for s in self.solutions:
            self.assertEqual([0, 4], s.search_range([2, 2, 2, 2, 2], 2))
            self.assertEqual([0, 4], s.search_range_builtin([2, 2, 2, 2, 2], 2))

    def test_target_at_start(self):
        for s in self.solutions:
            self.assertEqual([0, 2], s.search_range([1, 1, 1, 3, 5], 1))
            self.assertEqual([0, 2], s.search_range_builtin([1, 1, 1, 3, 5], 1))

    def test_target_at_end(self):
        for s in self.solutions:
            self.assertEqual([3, 4], s.search_range([1, 2, 3, 5, 5], 5))
            self.assertEqual([3, 4], s.search_range_builtin([1, 2, 3, 5, 5], 5))

    def test_target_smaller_than_all(self):
        for s in self.solutions:
            self.assertEqual([-1, -1], s.search_range([3, 4, 5], 1))
            self.assertEqual([-1, -1], s.search_range_builtin([3, 4, 5], 1))

    def test_target_larger_than_all(self):
        for s in self.solutions:
            self.assertEqual([-1, -1], s.search_range([3, 4, 5], 9))
            self.assertEqual([-1, -1], s.search_range_builtin([3, 4, 5], 9))


if __name__ == '__main__':
    unittest.main()
