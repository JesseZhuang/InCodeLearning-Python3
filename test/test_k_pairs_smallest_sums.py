import unittest

from algorithm.heap.k_pairs_smallest_sums import Solution


class TestKPairsSmallestSums(unittest.TestCase):
    def setUp(self):
        sol = Solution()
        self.solutions = [sol.kSmallestPairs, sol.kSmallestPairsBFS]

    def verify(self, nums1, nums2, k, expected):
        for fn in self.solutions:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(expected, fn(nums1, nums2, k))

    def test_example1(self):
        self.verify([1, 7, 11], [2, 4, 6], 3, [[1, 2], [1, 4], [1, 6]])

    def test_example2(self):
        self.verify([1, 1, 2], [1, 2, 3], 2, [[1, 1], [1, 1]])

    def test_example3(self):
        self.verify([1, 2], [3], 3, [[1, 3], [2, 3]])

    def test_k_larger_than_total(self):
        self.verify([1, 2], [3], 10, [[1, 3], [2, 3]])

    def test_single_element_each(self):
        self.verify([1], [2], 1, [[1, 2]])

    def test_empty_nums1(self):
        self.verify([], [1, 2], 3, [])

    def test_empty_nums2(self):
        self.verify([1, 2], [], 3, [])

    def test_large_k_equal_elements(self):
        self.verify([1, 1, 1], [1, 1, 1], 9,
                    [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]])

    def test_negative_numbers(self):
        self.verify([-5, -3, 0], [-2, 0, 4], 4,
                    [[-5, -2], [-5, 0], [-3, -2], [-3, 0]])
