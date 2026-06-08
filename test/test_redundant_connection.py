from unittest import TestCase

from algorithm.graph.redundant_connection import Solution, Solution2


class TestRedundantConnection(TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        edges = [[1, 2], [1, 3], [2, 3]]
        for sol in self.solutions:
            self.assertEqual([2, 3], sol.findRedundantConnection(edges))

    def test_example2(self):
        edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
        for sol in self.solutions:
            self.assertEqual([1, 4], sol.findRedundantConnection(edges))

    def test_three_nodes_last_edge_redundant(self):
        edges = [[1, 2], [2, 3], [1, 3]]
        for sol in self.solutions:
            self.assertEqual([1, 3], sol.findRedundantConnection(edges))

    def test_linear_with_back_edge(self):
        edges = [[1, 2], [2, 3], [3, 4], [4, 5], [3, 5]]
        for sol in self.solutions:
            self.assertEqual([3, 5], sol.findRedundantConnection(edges))

    def test_star_shape(self):
        edges = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3]]
        for sol in self.solutions:
            self.assertEqual([2, 3], sol.findRedundantConnection(edges))

    def test_large_cycle(self):
        # 1-2-3-4-5-1 cycle, edge [5,1] creates it
        edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]
        for sol in self.solutions:
            self.assertEqual([5, 1], sol.findRedundantConnection(edges))
