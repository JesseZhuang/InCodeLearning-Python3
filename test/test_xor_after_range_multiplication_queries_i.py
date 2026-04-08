import unittest

from algorithm.jzarray.xor_after_range_multiplication_queries_i import Solution


class TestXorAfterRangeMultiplicationQueries(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for s in self.solutions:
            self.assertEqual(4, s.xorAfterRangeMultiplicationQueries([1, 1, 1], [[0, 2, 1, 4]]))

    def test_example2(self):
        for s in self.solutions:
            self.assertEqual(31, s.xorAfterRangeMultiplicationQueries([2, 3, 1, 5, 4], [[1, 4, 2, 3], [0, 2, 1, 2]]))

    def test_single_element(self):
        for s in self.solutions:
            self.assertEqual(6, s.xorAfterRangeMultiplicationQueries([3], [[0, 0, 1, 2]]))

    def test_no_effect_step_larger_than_range(self):
        """k=3, range [1,2], only index 1 is hit."""
        for s in self.solutions:
            self.assertEqual(1 ^ 10 ^ 3, s.xorAfterRangeMultiplicationQueries([1, 5, 3], [[1, 2, 3, 2]]))

    def test_multiple_queries_same_index(self):
        for s in self.solutions:
            # [2,3] -> query1 [0,0,1,5] -> [10,3] -> query2 [0,0,1,3] -> [30,3]
            self.assertEqual(30 ^ 3, s.xorAfterRangeMultiplicationQueries([2, 3], [[0, 0, 1, 5], [0, 0, 1, 3]]))

    def test_large_values_mod(self):
        """Ensure mod is applied."""
        for s in self.solutions:
            mod = 10 ** 9 + 7
            # nums=[10^9], query multiply by 10^5
            expected = (10 ** 9 * 10 ** 5) % mod
            self.assertEqual(expected, s.xorAfterRangeMultiplicationQueries([10 ** 9], [[0, 0, 1, 10 ** 5]]))


if __name__ == '__main__':
    unittest.main()
