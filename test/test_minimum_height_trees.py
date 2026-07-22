import unittest

from algorithm.graph.minimum_height_trees import Solution


class TestMinimumHeightTrees(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_single_node(self):
        for sol in self.solutions:
            self.assertEqual(sol.findMinHeightTrees(1, []), [0])

    def test_two_nodes(self):
        for sol in self.solutions:
            self.assertEqual(sol.findMinHeightTrees(2, [[0, 1]]), [0, 1])

    def test_example1(self):
        for sol in self.solutions:
            # Tree: 0-1-2-3, 1-4
            res = sol.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])
            self.assertEqual(sorted(res), [1])

    def test_example2(self):
        for sol in self.solutions:
            # Tree: 0-3-1, 3-2, 3-4, 4-5
            res = sol.findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])
            self.assertEqual(sorted(res), [3, 4])

    def test_linear_odd(self):
        for sol in self.solutions:
            # 0-1-2-3-4: center is 2
            res = sol.findMinHeightTrees(5, [[0, 1], [1, 2], [2, 3], [3, 4]])
            self.assertEqual(sorted(res), [2])

    def test_linear_even(self):
        for sol in self.solutions:
            # 0-1-2-3: centers are 1,2
            res = sol.findMinHeightTrees(4, [[0, 1], [1, 2], [2, 3]])
            self.assertEqual(sorted(res), [1, 2])

    def test_star(self):
        for sol in self.solutions:
            # Star with center 0 connected to 1,2,3,4
            res = sol.findMinHeightTrees(5, [[0, 1], [0, 2], [0, 3], [0, 4]])
            self.assertEqual(sorted(res), [0])


if __name__ == "__main__":
    unittest.main()
