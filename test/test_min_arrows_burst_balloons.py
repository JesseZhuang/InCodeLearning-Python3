import unittest

from algorithm.jzarray.min_arrows_burst_balloons import Solution


class TestMinArrowsBurstBalloons(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        points = [[10, 16], [2, 8], [1, 6], [7, 12]]
        for sol in self.solutions:
            self.assertEqual(sol.findMinArrowShots(points[:]), 2)
            self.assertEqual(sol.findMinArrowShots2(points[:]), 2)

    def test_example2(self):
        points = [[1, 2], [3, 4], [5, 6], [7, 8]]
        for sol in self.solutions:
            self.assertEqual(sol.findMinArrowShots(points[:]), 4)
            self.assertEqual(sol.findMinArrowShots2(points[:]), 4)

    def test_example3(self):
        points = [[1, 2], [2, 3], [3, 4], [4, 5]]
        for sol in self.solutions:
            self.assertEqual(sol.findMinArrowShots(points[:]), 2)
            self.assertEqual(sol.findMinArrowShots2(points[:]), 2)

    def test_single_balloon(self):
        points = [[1, 5]]
        for sol in self.solutions:
            self.assertEqual(sol.findMinArrowShots(points[:]), 1)
            self.assertEqual(sol.findMinArrowShots2(points[:]), 1)

    def test_all_overlapping(self):
        points = [[1, 10], [2, 9], [3, 8], [4, 7]]
        for sol in self.solutions:
            self.assertEqual(sol.findMinArrowShots(points[:]), 1)
            self.assertEqual(sol.findMinArrowShots2(points[:]), 1)

    def test_touching_edges(self):
        points = [[1, 2], [2, 3], [3, 4]]
        for sol in self.solutions:
            self.assertEqual(sol.findMinArrowShots(points[:]), 2)
            self.assertEqual(sol.findMinArrowShots2(points[:]), 2)

    def test_negative_coordinates(self):
        points = [[-2147483648, 2147483647]]
        for sol in self.solutions:
            self.assertEqual(sol.findMinArrowShots(points[:]), 1)
            self.assertEqual(sol.findMinArrowShots2(points[:]), 1)

    def test_large_range(self):
        points = [[-1, 1], [0, 2], [1, 3]]
        for sol in self.solutions:
            self.assertEqual(sol.findMinArrowShots(points[:]), 1)
            self.assertEqual(sol.findMinArrowShots2(points[:]), 1)


if __name__ == '__main__':
    unittest.main()
