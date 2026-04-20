import unittest

from algorithm.jzarray.sum_of_subarray_minimums import Solution, Solution2


class TestSumOfSubarrayMinimums(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, arr, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.sumSubarrayMins(arr))

    def test_example1(self):
        self.verify([3, 1, 2, 4], 17)

    def test_example2(self):
        self.verify([11, 81, 94, 43, 3], 444)

    def test_single_element(self):
        self.verify([5], 5)

    def test_two_elements(self):
        self.verify([1, 2], 4)  # [1]=1, [2]=2, [1,2]=1 -> 4

    def test_decreasing(self):
        self.verify([3, 2, 1], 10)  # [3]=3,[2]=2,[1]=1,[3,2]=2,[2,1]=1,[3,2,1]=1 -> 10

    def test_increasing(self):
        self.verify([1, 2, 3], 10)  # [1]=1,[2]=2,[3]=3,[1,2]=1,[2,3]=2,[1,2,3]=1 -> 10

    def test_all_same(self):
        self.verify([2, 2, 2], 12)  # 6 subarrays, each min=2 -> 12

    def test_large_values(self):
        self.verify([10000] * 3, 60000)
