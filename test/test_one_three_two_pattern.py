import unittest

from algorithm.stack.one_three_two_pattern import Solution, Solution2


class TestOneThreeTwoPattern(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertFalse(sol.find132pattern([1, 2, 3, 4]))

    def test_example2(self):
        for sol in self.solutions:
            self.assertTrue(sol.find132pattern([3, 1, 4, 2]))

    def test_example3(self):
        for sol in self.solutions:
            self.assertTrue(sol.find132pattern([-1, 3, 2, 0]))

    def test_too_short(self):
        for sol in self.solutions:
            self.assertFalse(sol.find132pattern([1, 2]))

    def test_single(self):
        for sol in self.solutions:
            self.assertFalse(sol.find132pattern([1]))

    def test_decreasing(self):
        for sol in self.solutions:
            self.assertFalse(sol.find132pattern([5, 4, 3, 2, 1]))

    def test_increasing(self):
        for sol in self.solutions:
            self.assertFalse(sol.find132pattern([1, 2, 3, 4, 5]))

    def test_all_same(self):
        for sol in self.solutions:
            self.assertFalse(sol.find132pattern([3, 3, 3, 3]))

    def test_negative_pattern(self):
        for sol in self.solutions:
            self.assertTrue(sol.find132pattern([-2, 1, -1]))

    def test_pattern_at_end(self):
        for sol in self.solutions:
            self.assertFalse(sol.find132pattern([1, 0, 1, -4, -3]))

    def test_pattern_spread(self):
        for sol in self.solutions:
            self.assertTrue(sol.find132pattern([3, 5, 0, 3, 4]))

    def test_large_gap(self):
        for sol in self.solutions:
            self.assertTrue(sol.find132pattern([1, 3, 2]))

    def test_two_elements(self):
        for sol in self.solutions:
            self.assertFalse(sol.find132pattern([1, 2]))

    def test_exact_three_valid(self):
        for sol in self.solutions:
            self.assertTrue(sol.find132pattern([1, 3, 2]))

    def test_exact_three_invalid(self):
        for sol in self.solutions:
            self.assertFalse(sol.find132pattern([1, 2, 3]))


if __name__ == "__main__":
    unittest.main()
