import unittest

from algorithm.heap.total_cost_hire_k_workers import Solution, Solution2


class TestTotalCostHireKWorkers(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, costs, k, candidates, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.totalCost(costs, k, candidates))

    def test_example1(self):
        self.verify([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4, 11)

    def test_example2(self):
        self.verify([1, 2, 4, 1], 3, 3, 4)

    def test_single_element(self):
        self.verify([5], 1, 1, 5)

    def test_all_same_cost(self):
        self.verify([3, 3, 3, 3], 2, 2, 6)

    def test_candidates_cover_all(self):
        self.verify([10, 1, 10, 1], 2, 3, 2)

    def test_k_equals_n(self):
        self.verify([2, 1, 3], 3, 1, 6)

    def test_large_candidates(self):
        self.verify([5, 4, 3, 2, 1], 3, 10, 6)

    def test_descending(self):
        self.verify([5, 4, 3, 2, 1], 2, 1, 3)

    def test_tie_prefer_front(self):
        self.verify([1, 1, 1, 1, 1], 3, 2, 3)
