import unittest

from algorithm.graph.number_of_connected_components import Solution, Solution2


class TestNumberOfConnectedComponents(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        """n=5, edges=[[0,1],[1,2],[3,4]] -> 2"""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.countComponents(5, [[0, 1], [1, 2], [3, 4]]), 2)

    def test_example2(self):
        """n=5, edges=[[0,1],[1,2],[2,3],[3,4]] -> 1"""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]), 1)

    def test_no_edges(self):
        """Each node is its own component."""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.countComponents(4, []), 4)

    def test_single_node(self):
        """n=1, no edges -> 1 component."""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.countComponents(1, []), 1)

    def test_fully_connected(self):
        """All nodes connected in a line -> 1 component."""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                edges = [[i, i + 1] for i in range(4)]
                self.assertEqual(sol.countComponents(5, edges), 1)

    def test_three_components(self):
        """n=6, three pairs -> 3 components."""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.countComponents(6, [[0, 1], [2, 3], [4, 5]]), 3)

    def test_cycle(self):
        """Cycle does not create extra components."""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.countComponents(3, [[0, 1], [1, 2], [0, 2]]), 1)

    def test_two_nodes_one_edge(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.countComponents(2, [[0, 1]]), 1)


if __name__ == "__main__":
    unittest.main()
