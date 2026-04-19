from unittest import TestCase

from algorithm.jzarray.search_rotated_sorted_array import Solution, Solution2


class TestSearchRotatedSortedArray(TestCase):
    def test_search(self):
        cases = [
            ([4, 5, 6, 7, 0, 1, 2], 0, 4),
            ([4, 5, 6, 7, 0, 1, 2], 3, -1),
            ([1], 0, -1),
            ([1], 1, 0),
            ([3, 1], 1, 1),
            ([3, 1], 3, 0),
            ([5, 1, 3], 5, 0),
            ([5, 1, 3], 3, 2),
            ([5, 1, 3], 1, 1),
            ([5, 1, 3], 4, -1),
            ([2, 3, 4, 5, 1], 1, 4),
            ([2, 3, 4, 5, 1], 3, 1),
            ([1, 2, 3, 4, 5], 3, 2),  # no rotation
            ([4, 5, 6, 7, 8, 1, 2, 3], 8, 4),
        ]
        solutions = [Solution(), Solution2()]
        for nums, target, exp in cases:
            for sol in solutions:
                with self.subTest(nums=nums, target=target, sol=sol.__class__.__name__):
                    self.assertEqual(sol.search(nums, target), exp)
