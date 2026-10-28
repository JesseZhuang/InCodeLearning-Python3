import unittest

from algorithm.stack.min_swaps_balance import Solution


class TestMinSwapsBalance(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_examples(self):
        cases = [("][][", 1), ("]]][[[", 2), ("[]", 0)]
        for solution in self.solutions:
            for brackets, expected in cases:
                with self.subTest(brackets=brackets):
                    self.assertEqual(expected, solution.minSwaps(brackets))

    def test_balanced_nested_and_alternating(self):
        for solution in self.solutions:
            self.assertEqual(0, solution.minSwaps("[[[]]]"))
            self.assertEqual(0, solution.minSwaps("[][][][]"))

    def test_single_unmatched_pair(self):
        for solution in self.solutions:
            self.assertEqual(1, solution.minSwaps("]["))
            self.assertEqual(1, solution.minSwaps("[]]["))

    def test_multiple_unmatched_pairs(self):
        for solution in self.solutions:
            self.assertEqual(2, solution.minSwaps("]]][[["))
            self.assertEqual(2, solution.minSwaps("[[[]]]]]][[["))

    def test_maximum_length(self):
        for solution in self.solutions:
            self.assertEqual(250_000, solution.minSwaps("]" * 500_000 + "[" * 500_000))
            self.assertEqual(0, solution.minSwaps("[" * 500_000 + "]" * 500_000))


if __name__ == "__main__":
    unittest.main()
