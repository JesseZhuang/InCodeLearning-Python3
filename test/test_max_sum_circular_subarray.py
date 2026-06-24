import unittest

from algorithm.dp.max_sum_circular_subarray import Solution, Solution2


class TestMaxSumCircularSubarray(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(sol.maxSubarraySumCircular([1, -2, 3, -2]), 3)

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.maxSubarraySumCircular([5, -3, 5]), 10)

    def test_example3(self):
        for sol in self.solutions:
            self.assertEqual(sol.maxSubarraySumCircular([-3, -2, -3]), -2)

    def test_single_element_positive(self):
        for sol in self.solutions:
            self.assertEqual(sol.maxSubarraySumCircular([7]), 7)

    def test_single_element_negative(self):
        for sol in self.solutions:
            self.assertEqual(sol.maxSubarraySumCircular([-1]), -1)

    def test_all_negative(self):
        for sol in self.solutions:
            self.assertEqual(sol.maxSubarraySumCircular([-5, -3, -4, -1, -2]), -1)

    def test_all_positive(self):
        for sol in self.solutions:
            self.assertEqual(sol.maxSubarraySumCircular([3, 1, 2, 4]), 10)

    def test_wrap_around(self):
        """Max subarray wraps around: [5, ..., -100, ..., 4] -> 5+4=9 via wrapping."""
        for sol in self.solutions:
            self.assertEqual(sol.maxSubarraySumCircular([5, -3, -100, 2, 4]), 11)

    def test_two_elements(self):
        for sol in self.solutions:
            self.assertEqual(sol.maxSubarraySumCircular([3, -1]), 3)
            self.assertEqual(sol.maxSubarraySumCircular([3, 2]), 5)

    def test_large_wrap(self):
        for sol in self.solutions:
            self.assertEqual(sol.maxSubarraySumCircular([8, -1, -1, 8, -7, 4]), 18)


if __name__ == "__main__":
    unittest.main()
