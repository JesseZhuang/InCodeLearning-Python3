from unittest import TestCase

from algorithm.jzarray.count_unguarded_cells import Solution


class TestSolution(TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_count_unguarded(self):
        cases = [
            (4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]], 7),
            (3, 3, [[1, 1]], [[0, 1], [1, 0], [2, 1], [1, 2]], 4),
        ]
        for sol in self.solutions:
            for m, n, guards, walls, exp in cases:
                with self.subTest(sol=sol.__class__.__name__, m=m, n=n):
                    self.assertEqual(sol.countUnguarded(m, n, guards, walls), exp)
