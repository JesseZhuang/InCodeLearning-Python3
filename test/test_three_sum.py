import unittest

from algorithm.jzarray.three_sum import Solution, Solution2


class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, nums, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.threeSum(nums[:])  # pass copy to avoid mutation issues
                self.assertEqual(sorted(map(tuple, expected)), sorted(map(tuple, result)))

    def test_example1(self):
        self.verify([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])

    def test_example2(self):
        self.verify([0, 1, 1], [])

    def test_example3(self):
        self.verify([0, 0, 0], [[0, 0, 0]])

    def test_empty(self):
        self.verify([], [])

    def test_two_elements(self):
        self.verify([1, -1], [])

    def test_all_zeros(self):
        self.verify([0, 0, 0, 0], [[0, 0, 0]])

    def test_no_triplet(self):
        self.verify([1, 2, 3, 4, 5], [])

    def test_all_negative(self):
        self.verify([-5, -4, -3, -2, -1], [])

    def test_multiple_triplets(self):
        self.verify([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]])

    def test_large_duplicates(self):
        self.verify([-1, -1, -1, 0, 1, 1, 1], [[-1, 0, 1]])

    def test_single_element(self):
        self.verify([0], [])
