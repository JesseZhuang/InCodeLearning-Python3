import unittest

from algorithm.jzarray.shortest_subarray_sum_at_least_k import Solution


class TestShortestSubarraySumAtLeastK(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(1, self.sol.shortestSubarray([1], 1))

    def test_example2(self):
        self.assertEqual(-1, self.sol.shortestSubarray([1, 2], 4))

    def test_example3(self):
        self.assertEqual(3, self.sol.shortestSubarray([2, -1, 2], 3))


if __name__ == '__main__':
    unittest.main()
