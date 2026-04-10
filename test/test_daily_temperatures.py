import unittest

from algorithm.deq.daily_temperatures import Solution


class TestDailyTemperatures(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def verify(self, temperatures, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.dailyTemperatures(temperatures))

    def test_example1(self):
        self.verify([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0])

    def test_example2(self):
        self.verify([30, 40, 50, 60], [1, 1, 1, 0])

    def test_example3(self):
        self.verify([30, 60, 90], [1, 1, 0])

    def test_single(self):
        self.verify([50], [0])

    def test_decreasing(self):
        self.verify([90, 80, 70, 60], [0, 0, 0, 0])

    def test_all_same(self):
        self.verify([70, 70, 70], [0, 0, 0])

    def test_two_elements(self):
        self.verify([31, 32], [1, 0])
        self.verify([32, 31], [0, 0])
