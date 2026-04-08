import unittest

from algorithm.heap.kth_smallest_sorted_matrix import Solution


class TestKthSmallestSortedMatrix(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]
        self.cases = [
            (
                [
                    [1, 5, 9],
                    [10, 11, 13],
                    [12, 13, 15],
                ],
                8,
                13,
            ),
            ([[-5]], 1, -5),
            (
                [
                    [1, 2],
                    [1, 3],
                ],
                2,
                1,
            ),
            (
                [
                    [-10, -5, 0],
                    [-8, -3, 2],
                    [-6, 1, 4],
                ],
                5,
                -3,
            ),
            (
                [
                    [1, 2, 3],
                    [2, 3, 4],
                    [3, 4, 5],
                ],
                9,
                5,
            ),
            (
                [
                    [1, 2, 3],
                    [2, 3, 4],
                    [3, 4, 5],
                ],
                1,
                1,
            ),
        ]

    def test_binary_search_solution(self):
        for solution in self.solutions:
            for matrix, k, expected in self.cases:
                with self.subTest(method="binary_search", matrix=matrix, k=k):
                    self.assertEqual(expected, solution.kthSmallest(matrix, k))

    def test_heap_solution(self):
        for solution in self.solutions:
            for matrix, k, expected in self.cases:
                with self.subTest(method="heap", matrix=matrix, k=k):
                    self.assertEqual(expected, solution.kthSmallestHeap(matrix, k))


if __name__ == "__main__":
    unittest.main()
