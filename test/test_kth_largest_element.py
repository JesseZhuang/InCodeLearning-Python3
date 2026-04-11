import unittest

from algorithm.heap.kth_largest_element import Solution, Solution2


class TestKthLargestElement(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, nums, k, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.findKthLargest(list(nums), k))

    def test_example1(self):
        self.verify([3, 2, 1, 5, 6, 4], 2, 5)

    def test_example2(self):
        self.verify([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4)

    def test_single(self):
        self.verify([1], 1, 1)

    def test_all_same(self):
        self.verify([7, 7, 7, 7], 2, 7)

    def test_sorted_ascending(self):
        self.verify([1, 2, 3, 4, 5], 1, 5)

    def test_sorted_descending(self):
        self.verify([5, 4, 3, 2, 1], 5, 1)

    def test_two_elements(self):
        self.verify([2, 1], 1, 2)
        self.verify([2, 1], 2, 1)

    def test_negatives(self):
        self.verify([-1, -2, -3, -4], 2, -2)

    def test_mixed(self):
        self.verify([-1, 2, 0], 1, 2)

    def test_duplicates_k_equals_n(self):
        self.verify([3, 1, 2], 3, 1)
