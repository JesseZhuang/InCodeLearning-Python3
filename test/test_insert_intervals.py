from unittest import TestCase

from algorithm.jzarray.insert_intervals import Solution


class TestInsertInterval(TestCase):
    def test_insert(self):
        cases = [
            ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
            ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
            ([], [5, 7], [[5, 7]]),
            ([[1, 5]], [2, 3], [[1, 5]]),
            ([[1, 5]], [6, 8], [[1, 5], [6, 8]]),
            ([[1, 5]], [0, 0], [[0, 0], [1, 5]]),
            ([[1, 5]], [0, 6], [[0, 6]]),
            ([[1, 2], [5, 6]], [3, 4], [[1, 2], [3, 4], [5, 6]]),
            ([[1, 2], [3, 4], [5, 6]], [0, 7], [[0, 7]]),
            ([[0, 0]], [0, 0], [[0, 0]]),
        ]
        solutions = [Solution()]
        for intervals, new, exp in cases:
            for sol in solutions:
                with self.subTest(intervals=intervals, new=new, sol=sol.__class__.__name__):
                    self.assertEqual(sol.insert([iv[:] for iv in intervals], new[:]), exp)
