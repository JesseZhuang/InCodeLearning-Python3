import unittest

from algorithm.jzarray.power_k_size_subarrays import Solution


class TestPowerKSizeSubarrays(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual([3, 4, -1, -1, -1], self.sol.resultsArray([1, 2, 3, 4, 3, 2, 5], 3))

    def test_example2(self):
        self.assertEqual([-1, -1], self.sol.resultsArray([2, 2, 2, 2, 2], 4))

    def test_example3(self):
        self.assertEqual([-1, 3, -1, 3, -1], self.sol.resultsArray([3, 2, 3, 2, 3, 2], 2))


if __name__ == '__main__':
    unittest.main()
