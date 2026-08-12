import unittest

from algorithm.binary_search.minimize_max_difference_of_pairs import Solution


class TestMinimizeMaxDifference(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(sol.minimizeMax([10, 1, 2, 7, 1, 3], 2), 1)

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.minimizeMax([4, 2, 1, 2], 1), 0)

    def test_p_zero(self):
        for sol in self.solutions:
            self.assertEqual(sol.minimizeMax([5, 3, 1], 0), 0)

    def test_single_pair(self):
        for sol in self.solutions:
            self.assertEqual(sol.minimizeMax([1, 5], 1), 4)

    def test_all_same(self):
        for sol in self.solutions:
            self.assertEqual(sol.minimizeMax([3, 3, 3, 3], 2), 0)

    def test_large_gap(self):
        # sorted: [1,2,3,98,99,100], pairs: (1,2),(3,98),(99,100) -> max=95
        # or (1,2),(98,99),(3,100) not possible (greedy). Min max = 95
        for sol in self.solutions:
            self.assertEqual(sol.minimizeMax([1, 100, 2, 99, 3, 98], 3), 95)

    def test_max_pairs(self):
        # n=6, p=3 means all elements paired
        for sol in self.solutions:
            self.assertEqual(sol.minimizeMax([1, 2, 3, 4, 5, 6], 3), 1)

    def test_two_elements(self):
        for sol in self.solutions:
            self.assertEqual(sol.minimizeMax([0, 0], 1), 0)


if __name__ == "__main__":
    unittest.main()
