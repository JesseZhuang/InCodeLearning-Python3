import unittest

from algorithm.heap.top_k_frequent_elements import Solution, Solution2


class TestTopKFrequentElements(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, nums, k, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertCountEqual(expected, sol.topKFrequent(nums, k))

    def test_example1(self):
        self.verify([1, 1, 1, 2, 2, 3], 2, [1, 2])

    def test_example2(self):
        self.verify([1], 1, [1])

    def test_all_same_frequency(self):
        # k=2 among elements with equal frequency, any 2 are valid
        res = Solution().topKFrequent([1, 2, 3], 3)
        self.assertCountEqual([1, 2, 3], res)

    def test_negative_numbers(self):
        self.verify([-1, -1, -2, -2, -2, -3], 2, [-2, -1])

    def test_single_element_repeated(self):
        self.verify([5, 5, 5, 5], 1, [5])

    def test_k_equals_unique_count(self):
        self.verify([1, 1, 2, 2, 3, 3], 3, [1, 2, 3])

    def test_large_k(self):
        self.verify([4, 4, 4, 1, 1, 2, 2, 2, 3], 3, [4, 2, 1])
