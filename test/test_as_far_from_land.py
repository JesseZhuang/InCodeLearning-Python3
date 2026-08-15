import copy
import unittest

from algorithm.graph.as_far_from_land import Solution, Solution2


class TestAsFarFromLand(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        expected = 2
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.maxDistance(copy.deepcopy(grid)), expected)

    def test_example2(self):
        grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected = 4
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.maxDistance(copy.deepcopy(grid)), expected)

    def test_all_land(self):
        grid = [[1, 1], [1, 1]]
        expected = -1
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.maxDistance(copy.deepcopy(grid)), expected)

    def test_all_water(self):
        grid = [[0, 0], [0, 0]]
        expected = -1
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.maxDistance(copy.deepcopy(grid)), expected)

    def test_single_land_corner(self):
        grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected = 4
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.maxDistance(copy.deepcopy(grid)), expected)

    def test_land_center(self):
        grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        expected = 2
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.maxDistance(copy.deepcopy(grid)), expected)

    def test_min_grid(self):
        grid = [[0, 1], [1, 0]]
        expected = 1
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.maxDistance(copy.deepcopy(grid)), expected)


if __name__ == '__main__':
    unittest.main()
