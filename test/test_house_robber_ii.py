import unittest
from algorithm.dp.house_robber_ii import Solution


class TestHouseRobberII(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(sol.rob([2, 3, 2]), 3)

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.rob([1, 2, 3, 1]), 4)

    def test_example3(self):
        for sol in self.solutions:
            self.assertEqual(sol.rob([1, 2, 3]), 3)

    def test_single(self):
        for sol in self.solutions:
            self.assertEqual(sol.rob([5]), 5)

    def test_two_elements(self):
        for sol in self.solutions:
            self.assertEqual(sol.rob([1, 2]), 2)

    def test_two_same(self):
        for sol in self.solutions:
            self.assertEqual(sol.rob([3, 3]), 3)

    def test_all_same_four(self):
        for sol in self.solutions:
            self.assertEqual(sol.rob([3, 3, 3, 3]), 6)

    def test_large_values(self):
        for sol in self.solutions:
            self.assertEqual(sol.rob([1000, 1, 1000, 1]), 2000)

    def test_alternating(self):
        for sol in self.solutions:
            self.assertEqual(sol.rob([200, 3, 140, 20, 10]), 340)

    def test_all_zeros(self):
        for sol in self.solutions:
            self.assertEqual(sol.rob([0, 0, 0, 0]), 0)

    def test_five_elements(self):
        for sol in self.solutions:
            self.assertEqual(sol.rob([1, 2, 3, 4, 5]), 8)

    def test_constraint_max_length(self):
        nums = [i % 5 for i in range(100)]
        for sol in self.solutions:
            result = sol.rob(nums)
            self.assertIsInstance(result, int)
            self.assertGreater(result, 0)


if __name__ == '__main__':
    unittest.main()
