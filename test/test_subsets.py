import unittest

from algorithm.jzarray.subsets import Solution, Solution2


class TestSubsets(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_basic(self):
        cases = [
            ([1, 2, 3], [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
            ([0], [[], [0]]),
        ]
        for sol in self.solutions:
            for nums, expected in cases:
                with self.subTest(sol=sol.__class__.__name__, nums=nums):
                    result = sol.subsets(nums)
                    self.assertEqual(len(result), len(expected))
                    self.assertEqual(sorted(map(sorted, result)), sorted(map(sorted, expected)))

    def test_empty_input(self):
        for sol in self.solutions:
            result = sol.subsets([])
            self.assertEqual(result, [[]])

    def test_two_elements(self):
        for sol in self.solutions:
            result = sol.subsets([1, 2])
            self.assertEqual(len(result), 4)
            self.assertEqual(sorted(map(sorted, result)), sorted([[], [1], [2], [1, 2]]))

    def test_negative_numbers(self):
        for sol in self.solutions:
            result = sol.subsets([-1, 0, 1])
            self.assertEqual(len(result), 8)

    def test_max_size(self):
        nums = list(range(10))
        for sol in self.solutions:
            result = sol.subsets(nums)
            self.assertEqual(len(result), 1024)  # 2^10
