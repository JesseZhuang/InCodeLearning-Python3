import unittest

from algorithm.graph.is_graph_bipartite import Solution, Solution2


class TestIsGraphBipartite(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1_bipartite(self):
        graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertTrue(sol.isBipartite(graph))

    def test_example2_not_bipartite(self):
        graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertFalse(sol.isBipartite(graph))

    def test_single_node(self):
        graph = [[]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertTrue(sol.isBipartite(graph))

    def test_disconnected_bipartite(self):
        graph = [[1], [0], [3], [2]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertTrue(sol.isBipartite(graph))

    def test_disconnected_not_bipartite(self):
        graph = [[1], [0], [3, 4], [2, 4], [2, 3]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertFalse(sol.isBipartite(graph))

    def test_no_edges(self):
        graph = [[], [], []]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertTrue(sol.isBipartite(graph))

    def test_self_loop_odd_cycle(self):
        # Triangle: 0-1, 1-2, 2-0
        graph = [[1, 2], [0, 2], [0, 1]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertFalse(sol.isBipartite(graph))

    def test_large_bipartite(self):
        # Complete bipartite K3,3
        graph = [[3, 4, 5], [3, 4, 5], [3, 4, 5], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertTrue(sol.isBipartite(graph))

    def test_two_nodes_connected(self):
        graph = [[1], [0]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertTrue(sol.isBipartite(graph))


if __name__ == '__main__':
    unittest.main()
