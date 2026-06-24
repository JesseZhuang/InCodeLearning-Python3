import unittest

from algorithm.dp.target_sum import Solution, Solution2


class TestTargetSum(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(5, sol.findTargetSumWays([1, 1, 1, 1, 1], 3))

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.findTargetSumWays([1], 1))

    def test_target_zero(self):
        for sol in self.solutions:
            self.assertEqual(2, sol.findTargetSumWays([1, 0], 1))

    def test_all_zeros(self):
        for sol in self.solutions:
            self.assertEqual(32, sol.findTargetSumWays([0, 0, 0, 0, 0], 0))

    def test_impossible(self):
        for sol in self.solutions:
            self.assertEqual(0, sol.findTargetSumWays([1, 2, 3], 7))

    def test_negative_target(self):
        for sol in self.solutions:
            self.assertEqual(5, sol.findTargetSumWays([1, 1, 1, 1, 1], -3))

    def test_single_zero(self):
        for sol in self.solutions:
            self.assertEqual(2, sol.findTargetSumWays([0], 0))

    def test_larger(self):
        for sol in self.solutions:
            self.assertEqual(2, sol.findTargetSumWays([1, 2, 1], 0))


if __name__ == '__main__':
    unittest.main()
