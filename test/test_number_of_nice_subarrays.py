import unittest

from algorithm.hash.number_of_nice_subarrays import Solution


class TestNumberOfNiceSubarrays(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def check(self, nums, k, expected):
        for solution in self.solutions:
            self.assertEqual(expected, solution.numberOfSubarrays(nums, k))
            self.assertEqual(expected, solution.numberOfSubarraysSliding(nums, k))

    def test_example(self):
        self.check([1, 1, 2, 1, 1], 3, 2)

    def test_no_odd_numbers(self):
        self.check([2, 4, 6], 1, 0)

    def test_all_odd_numbers(self):
        self.check([1, 3, 5], 2, 2)

    def test_exactly_one_odd_with_even_runs(self):
        self.check([2, 1, 2, 1, 2], 1, 8)

    def test_k_equals_number_of_odds(self):
        self.check([1, 2, 3], 2, 1)

    def test_k_exceeds_number_of_odds(self):
        self.check([1, 2, 3], 3, 0)

    def test_single_odd_number(self):
        self.check([1], 1, 1)

    def test_large_answer_within_constraints(self):
        nums = [2] * 24_999 + [1] + [2] * 24_999
        self.check(nums, 1, 625_000_000)


if __name__ == "__main__":
    unittest.main()
