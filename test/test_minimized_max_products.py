from unittest import TestCase

from algorithm.jzarray.minimized_max_products import Solution


class TestSolution(TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_minimized_maximum(self):
        cases = [
            (6, [11, 6], 3),
            (7, [15, 10, 10], 5),
            (1, [100000], 100000),
        ]
        for sol in self.solutions:
            for n, quantities, exp in cases:
                with self.subTest(sol=sol.__class__.__name__, n=n, q=quantities):
                    self.assertEqual(sol.minimizedMaximum(n, list(quantities)), exp)
