import unittest

from algorithm.sliding.equal_substrings_within_budget import Solution


class TestEqualSubstringWithinBudget(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_examples(self):
        cases = [
            ("abcd", "bcdf", 3, 3),
            ("abcd", "cdef", 3, 1),
            ("abcd", "acde", 0, 1),
        ]
        for s, t, max_cost, expected in cases:
            for solution in self.solutions:
                with self.subTest(s=s, t=t, max_cost=max_cost, solution=type(solution).__name__):
                    self.assertEqual(expected, solution.equalSubstring(s, t, max_cost))

    def test_shrinks_until_cost_fits(self):
        for solution in self.solutions:
            self.assertEqual(2, solution.equalSubstring("krrgw", "zjxss", 14))

    def test_zero_budget(self):
        for solution in self.solutions:
            self.assertEqual(4, solution.equalSubstring("same", "same", 0))
            self.assertEqual(0, solution.equalSubstring("abc", "xyz", 0))

    def test_single_character(self):
        for solution in self.solutions:
            self.assertEqual(1, solution.equalSubstring("a", "a", 0))
            self.assertEqual(1, solution.equalSubstring("a", "z", 25))


if __name__ == "__main__":
    unittest.main()
