import unittest

from algorithm.dp.climbing_stairs import Solution


class TestClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_one_step(self):
        for solution in self.solutions:
            self.assertEqual(1, solution.climbStairs(1))

    def test_two_steps(self):
        for solution in self.solutions:
            self.assertEqual(2, solution.climbStairs(2))

    def test_three_steps(self):
        for solution in self.solutions:
            self.assertEqual(3, solution.climbStairs(3))

    def test_four_steps(self):
        for solution in self.solutions:
            self.assertEqual(5, solution.climbStairs(4))

    def test_maximum_constraint(self):
        for solution in self.solutions:
            self.assertEqual(1836311903, solution.climbStairs(45))


if __name__ == '__main__':
    unittest.main()
