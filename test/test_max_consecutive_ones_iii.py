import unittest

from algorithm.sliding.max_consecutive_ones_iii import Solution, Solution2


class TestMaxConsecutiveOnesIII(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
        for sol in self.solutions:
            self.assertEqual(6, sol.longestOnes(nums, 2))

    def test_example2(self):
        nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
        for sol in self.solutions:
            self.assertEqual(10, sol.longestOnes(nums, 3))

    def test_all_ones(self):
        for sol in self.solutions:
            self.assertEqual(5, sol.longestOnes([1, 1, 1, 1, 1], 0))

    def test_all_zeros_k_covers(self):
        for sol in self.solutions:
            self.assertEqual(4, sol.longestOnes([0, 0, 0, 0], 4))

    def test_all_zeros_k_partial(self):
        for sol in self.solutions:
            self.assertEqual(2, sol.longestOnes([0, 0, 0, 0], 2))

    def test_k_zero(self):
        for sol in self.solutions:
            self.assertEqual(3, sol.longestOnes([1, 1, 1, 0, 1, 1], 0))

    def test_single_element_one(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.longestOnes([1], 0))

    def test_single_element_zero_k1(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.longestOnes([0], 1))

    def test_single_element_zero_k0(self):
        for sol in self.solutions:
            self.assertEqual(0, sol.longestOnes([0], 0))

    def test_k_larger_than_zeros(self):
        nums = [1, 0, 1, 0, 1]
        for sol in self.solutions:
            self.assertEqual(5, sol.longestOnes(nums, 3))

    def test_alternating(self):
        nums = [0, 1, 0, 1, 0, 1]
        for sol in self.solutions:
            self.assertEqual(5, sol.longestOnes(nums, 2))


if __name__ == '__main__':
    unittest.main()
