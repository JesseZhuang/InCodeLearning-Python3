import unittest

from algorithm.binary_search.min_days_bouquets import Solution


class TestMinDaysBouquets(unittest.TestCase):

    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(3, sol.minDays([1, 10, 3, 10, 2], 3, 1))

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(-1, sol.minDays([1, 10, 3, 10, 2], 3, 2))

    def test_example3(self):
        for sol in self.solutions:
            self.assertEqual(12, sol.minDays([7, 7, 7, 7, 12, 7, 7], 2, 3))

    def test_all_same_day(self):
        for sol in self.solutions:
            self.assertEqual(5, sol.minDays([5, 5, 5, 5], 2, 2))

    def test_single_flower(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.minDays([1], 1, 1))

    def test_impossible(self):
        for sol in self.solutions:
            self.assertEqual(-1, sol.minDays([1, 2, 3], 2, 2))

    def test_need_max_day(self):
        for sol in self.solutions:
            self.assertEqual(1000000000, sol.minDays([1000000000, 1000000000], 1, 2))

    def test_already_bloomed(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.minDays([1, 1, 1, 1], 2, 2))


if __name__ == '__main__':
    unittest.main()
