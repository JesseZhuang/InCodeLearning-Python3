import unittest

from algorithm.jzarray.container_with_most_water import Solution, Solution2


class TestContainerWithMostWater(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(49, sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.maxArea([1, 1]))

    def test_decreasing(self):
        for sol in self.solutions:
            self.assertEqual(16, sol.maxArea([4, 3, 2, 1, 4]))

    def test_all_same(self):
        for sol in self.solutions:
            self.assertEqual(20, sol.maxArea([5, 5, 5, 5, 5]))

    def test_two_elements(self):
        for sol in self.solutions:
            self.assertEqual(3, sol.maxArea([3, 100]))

    def test_large_at_ends(self):
        for sol in self.solutions:
            self.assertEqual(80, sol.maxArea([10, 1, 1, 1, 1, 1, 1, 1, 10]))


if __name__ == "__main__":
    unittest.main()
