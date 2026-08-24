import unittest

from algorithm.binary_search.capacity_ship_packages import Solution


class TestCapacityShipPackages(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for s in self.solutions:
            self.assertEqual(15, s.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))

    def test_example2(self):
        for s in self.solutions:
            self.assertEqual(6, s.shipWithinDays([3, 2, 2, 4, 1, 4], 3))

    def test_example3(self):
        for s in self.solutions:
            self.assertEqual(3, s.shipWithinDays([1, 2, 3, 1, 1], 4))

    def test_single_package(self):
        for s in self.solutions:
            self.assertEqual(5, s.shipWithinDays([5], 1))

    def test_one_day(self):
        for s in self.solutions:
            self.assertEqual(15, s.shipWithinDays([1, 2, 3, 4, 5], 1))

    def test_days_equal_packages(self):
        for s in self.solutions:
            self.assertEqual(3, s.shipWithinDays([1, 2, 3, 1, 1], 5))

    def test_all_same_weight(self):
        for s in self.solutions:
            self.assertEqual(6, s.shipWithinDays([3, 3, 3, 3, 3, 3], 3))

    def test_heavy_last(self):
        for s in self.solutions:
            self.assertEqual(500, s.shipWithinDays([1, 1, 1, 500], 2))


if __name__ == "__main__":
    unittest.main()
