import unittest
from algorithm.dp.house_robber import Solution


class TestHouseRobber(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(sol.rob([1, 2, 3, 1]), 4)

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.rob([2, 7, 9, 3, 1]), 12)

    def test_single(self):
        for sol in self.solutions:
            self.assertEqual(sol.rob([5]), 5)

    def test_two_elements(self):
        for sol in self.solutions:
            self.assertEqual(sol.rob([1, 2]), 2)

    def test_all_same(self):
        for sol in self.solutions:
            self.assertEqual(sol.rob([3, 3, 3, 3]), 6)

    def test_descending(self):
        for sol in self.solutions:
            self.assertEqual(sol.rob([10, 5, 1]), 11)

    def test_alternating_high_low(self):
        for sol in self.solutions:
            self.assertEqual(sol.rob([100, 1, 100, 1, 100]), 300)

    def test_empty(self):
        for sol in self.solutions:
            self.assertEqual(sol.rob([]), 0)

    def test_large_values(self):
        for sol in self.solutions:
            self.assertEqual(sol.rob([400, 400]), 400)

    def test_three_elements(self):
        for sol in self.solutions:
            self.assertEqual(sol.rob([2, 1, 1]), 3)


if __name__ == '__main__':
    unittest.main()
