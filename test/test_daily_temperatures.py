import unittest

from algorithm.stack.daily_temperatures import Solution


class TestDailyTemperatures(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(
                [1, 1, 4, 2, 1, 1, 0, 0],
                sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]),
            )

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(
                [1, 1, 1, 0],
                sol.dailyTemperatures([30, 40, 50, 60]),
            )

    def test_example3(self):
        for sol in self.solutions:
            self.assertEqual(
                [1, 1, 0],
                sol.dailyTemperatures([30, 60, 90]),
            )

    def test_single(self):
        for sol in self.solutions:
            self.assertEqual([0], sol.dailyTemperatures([50]))

    def test_decreasing(self):
        for sol in self.solutions:
            self.assertEqual(
                [0, 0, 0, 0],
                sol.dailyTemperatures([90, 80, 70, 60]),
            )

    def test_all_same(self):
        for sol in self.solutions:
            self.assertEqual(
                [0, 0, 0],
                sol.dailyTemperatures([70, 70, 70]),
            )

    def test_warmer_at_end(self):
        for sol in self.solutions:
            self.assertEqual(
                [4, 3, 2, 1, 0],
                sol.dailyTemperatures([30, 30, 30, 30, 31]),
            )


if __name__ == "__main__":
    unittest.main()
