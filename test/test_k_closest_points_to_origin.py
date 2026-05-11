import unittest

from algorithm.heap.k_closest_points_to_origin import Solution, Solution2


class TestKClosestPointsToOrigin(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, points, k, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                res = sol.kClosest([p[:] for p in points], k)
                self.assertEqual(len(res), len(expected))
                self.assertCountEqual([tuple(p) for p in expected], [tuple(p) for p in res])

    def test_example1(self):
        self.verify([[1, 3], [-2, 2]], 1, [[-2, 2]])

    def test_example2(self):
        self.verify([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]])

    def test_single_point(self):
        self.verify([[0, 1]], 1, [[0, 1]])

    def test_k_equals_n(self):
        self.verify([[1, 1], [2, 2], [3, 3]], 3, [[1, 1], [2, 2], [3, 3]])

    def test_origin(self):
        self.verify([[0, 0], [1, 1]], 1, [[0, 0]])

    def test_negative_coordinates(self):
        self.verify([[-1, -1], [-2, -2], [1, 1]], 2, [[-1, -1], [1, 1]])

    def test_same_distance(self):
        self.verify([[1, 0], [0, 1], [-1, 0], [0, -1]], 2, expect_any_two_of=[[1, 0], [0, 1], [-1, 0], [0, -1]])

    def test_large_coordinates(self):
        self.verify([[10000, 10000], [1, 1]], 1, [[1, 1]])

    def verify(self, points, k, expected=None, expect_any_two_of=None):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                res = sol.kClosest([p[:] for p in points], k)
                self.assertEqual(len(res), k)
                if expected is not None:
                    self.assertCountEqual([tuple(p) for p in expected], [tuple(p) for p in res])
                elif expect_any_two_of is not None:
                    for p in res:
                        self.assertIn(p, expect_any_two_of)
