import unittest

from algorithm.binary_search.split_array_largest_sum import Solution


class TestSplitArrayLargestSum(unittest.TestCase):

    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(18, sol.splitArray([7, 2, 5, 10, 8], 2))
            self.assertEqual(18, sol.splitArray2([7, 2, 5, 10, 8], 2))

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(9, sol.splitArray([1, 2, 3, 4, 5], 2))
            self.assertEqual(9, sol.splitArray2([1, 2, 3, 4, 5], 2))

    def test_single_element(self):
        for sol in self.solutions:
            self.assertEqual(10, sol.splitArray([10], 1))
            self.assertEqual(10, sol.splitArray2([10], 1))

    def test_k_equals_n(self):
        """Each element is its own subarray, answer is max element."""
        for sol in self.solutions:
            self.assertEqual(5, sol.splitArray([1, 2, 3, 4, 5], 5))
            self.assertEqual(5, sol.splitArray2([1, 2, 3, 4, 5], 5))

    def test_k_equals_one(self):
        """Only one subarray, answer is total sum."""
        for sol in self.solutions:
            self.assertEqual(15, sol.splitArray([1, 2, 3, 4, 5], 1))
            self.assertEqual(15, sol.splitArray2([1, 2, 3, 4, 5], 1))

    def test_all_same(self):
        for sol in self.solutions:
            self.assertEqual(6, sol.splitArray([3, 3, 3, 3], 2))
            self.assertEqual(6, sol.splitArray2([3, 3, 3, 3], 2))

    def test_large_single_element(self):
        for sol in self.solutions:
            self.assertEqual(1000000, sol.splitArray([1000000, 1, 1], 2))
            self.assertEqual(1000000, sol.splitArray2([1000000, 1, 1], 2))

    def test_zeros(self):
        for sol in self.solutions:
            self.assertEqual(0, sol.splitArray([0, 0, 0], 2))
            self.assertEqual(0, sol.splitArray2([0, 0, 0], 2))


if __name__ == '__main__':
    unittest.main()
