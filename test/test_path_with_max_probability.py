import unittest

from algorithm.graph.path_with_max_probability import Solution, Solution2


class TestMaxProbability(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            res = sol.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2)
            self.assertAlmostEqual(res, 0.25, places=5)

    def test_example2(self):
        for sol in self.solutions:
            res = sol.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2)
            self.assertAlmostEqual(res, 0.3, places=5)

    def test_no_path(self):
        for sol in self.solutions:
            res = sol.maxProbability(3, [[0, 1]], [0.5], 0, 2)
            self.assertAlmostEqual(res, 0.0, places=5)

    def test_single_node(self):
        for sol in self.solutions:
            res = sol.maxProbability(1, [], [], 0, 0)
            self.assertAlmostEqual(res, 1.0, places=5)

    def test_direct_edge(self):
        for sol in self.solutions:
            res = sol.maxProbability(2, [[0, 1]], [0.8], 0, 1)
            self.assertAlmostEqual(res, 0.8, places=5)

    def test_longer_path_better(self):
        # Direct edge 0->2 has prob 0.1, but 0->1->2 has 0.9*0.9=0.81
        for sol in self.solutions:
            res = sol.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.9, 0.9, 0.1], 0, 2)
            self.assertAlmostEqual(res, 0.81, places=5)

    def test_large_disconnected(self):
        for sol in self.solutions:
            res = sol.maxProbability(5, [[0, 1], [2, 3]], [0.5, 0.5], 0, 4)
            self.assertAlmostEqual(res, 0.0, places=5)


if __name__ == '__main__':
    unittest.main()
