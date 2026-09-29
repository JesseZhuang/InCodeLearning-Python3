import unittest

from algorithm.jzarray.car_pooling import Solution, Solution2


class TestCarPooling(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertFalse(sol.carPooling([[2, 1, 5], [3, 3, 7]], 4))

    def test_example2(self):
        for sol in self.solutions:
            self.assertTrue(sol.carPooling([[2, 1, 5], [3, 3, 7]], 5))

    def test_example3(self):
        for sol in self.solutions:
            self.assertTrue(sol.carPooling([[2, 1, 5], [3, 5, 7]], 3))

    def test_single_trip(self):
        for sol in self.solutions:
            self.assertTrue(sol.carPooling([[3, 2, 7]], 3))

    def test_single_trip_over_capacity(self):
        for sol in self.solutions:
            self.assertFalse(sol.carPooling([[3, 2, 7]], 2))

    def test_no_overlap(self):
        for sol in self.solutions:
            self.assertTrue(sol.carPooling([[5, 0, 3], [5, 3, 6]], 5))

    def test_exact_capacity(self):
        for sol in self.solutions:
            self.assertTrue(sol.carPooling([[2, 0, 5], [3, 0, 5]], 5))

    def test_exceed_at_one_stop(self):
        for sol in self.solutions:
            self.assertFalse(sol.carPooling([[2, 0, 5], [3, 0, 5]], 4))

    def test_drop_off_before_pick_up(self):
        for sol in self.solutions:
            self.assertTrue(sol.carPooling([[3, 0, 2], [3, 2, 4]], 3))

    def test_many_trips_same_range(self):
        for sol in self.solutions:
            self.assertFalse(sol.carPooling([[1, 0, 5]] * 6, 5))

    def test_max_range(self):
        for sol in self.solutions:
            self.assertTrue(sol.carPooling([[1, 0, 1000]], 1))

    def test_empty_trips(self):
        for sol in self.solutions:
            self.assertTrue(sol.carPooling([], 1))


if __name__ == '__main__':
    unittest.main()
