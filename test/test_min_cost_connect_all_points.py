import unittest

from algorithm.graph.min_cost_connect_all_points import Solution, Solution2


class TestMinCostConnectAllPoints(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, points, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.minCostConnectPoints(points))

    def test_example1(self):
        self.verify([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20)

    def test_example2(self):
        self.verify([[3, 12], [-2, 5], [-4, 1]], 18)

    def test_single_point(self):
        self.verify([[0, 0]], 0)

    def test_two_points(self):
        self.verify([[0, 0], [1, 1]], 2)

    def test_collinear(self):
        self.verify([[0, 0], [1, 0], [2, 0], [3, 0]], 3)

    def test_same_point(self):
        self.verify([[0, 0], [0, 0], [0, 0]], 0)

    def test_negative_coords(self):
        self.verify([[-1000000, -1000000], [1000000, 1000000]], 4000000)


if __name__ == '__main__':
    unittest.main()
