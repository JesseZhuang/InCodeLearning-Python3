from unittest import TestCase

from algorithm.jzarray.shortest_subarray_removed import Solution


class TestSolution(TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_shortest_subarray_removed(self):
        cases = [
            ([1, 2, 3, 10, 4, 2, 3, 5], 3),
            ([5, 4, 3, 2, 1], 4),
            ([1, 2, 3], 0),
            ([1], 0),
            ([2, 2, 2, 1, 1, 1], 3),
        ]
        for sol in self.solutions:
            for arr, exp in cases:
                with self.subTest(sol=sol.__class__.__name__, arr=arr):
                    self.assertEqual(sol.findLengthOfShortestSubarray(list(arr)), exp)
