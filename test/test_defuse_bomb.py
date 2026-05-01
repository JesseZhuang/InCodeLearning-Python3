from unittest import TestCase

from algorithm.jzarray.defuse_bomb import Solution


class TestSolution(TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_defuse_bomb(self):
        cases = [
            ([5, 7, 1, 4], 3, [12, 10, 16, 13]),
            ([1, 2, 3, 4], 0, [0, 0, 0, 0]),
            ([2, 4, 9, 3], -2, [12, 5, 6, 13]),
        ]
        for sol in self.solutions:
            for code, k, exp in cases:
                with self.subTest(sol=sol.__class__.__name__, code=code, k=k):
                    self.assertEqual(sol.decrypt(list(code), k), exp)
