import unittest

from algorithm.jzarray.car_fleet import Solution


class TestCarFleet(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(3, sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.carFleet(10, [3], [3]))

    def test_example3(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.carFleet(100, [0, 2, 4], [4, 2, 1]))

    def test_all_same_speed(self):
        for sol in self.solutions:
            self.assertEqual(3, sol.carFleet(10, [1, 4, 7], [2, 2, 2]))

    def test_already_at_target(self):
        for sol in self.solutions:
            self.assertEqual(2, sol.carFleet(5, [0, 4], [1, 1]))

    def test_single_car(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.carFleet(100, [50], [10]))


if __name__ == '__main__':
    unittest.main()
