import unittest

from algorithm.graph.swim_in_rising_water import Solution, Solution2


class TestSwimInRisingWater(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        grid = [[0, 2], [1, 3]]
        for sol in self.solutions:
            self.assertEqual(sol.swimInWater(grid), 3)

    def test_example2(self):
        grid = [
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6],
        ]
        for sol in self.solutions:
            self.assertEqual(sol.swimInWater(grid), 16)

    def test_single_cell(self):
        grid = [[0]]
        for sol in self.solutions:
            self.assertEqual(sol.swimInWater(grid), 0)

    def test_straight_path(self):
        grid = [[0, 1], [3, 2]]
        for sol in self.solutions:
            self.assertEqual(sol.swimInWater(grid), 2)

    def test_large_corner(self):
        grid = [[3, 2], [0, 1]]
        for sol in self.solutions:
            self.assertEqual(sol.swimInWater(grid), 3)


if __name__ == "__main__":
    unittest.main()
