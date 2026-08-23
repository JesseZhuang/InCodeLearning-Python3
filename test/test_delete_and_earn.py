import unittest
from algorithm.dp.delete_and_earn import Solution, Solution2


class TestDeleteAndEarn(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(sol.deleteAndEarn([3, 4, 2]), 6)

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.deleteAndEarn([2, 2, 3, 3, 3, 4]), 9)

    def test_single_element(self):
        for sol in self.solutions:
            self.assertEqual(sol.deleteAndEarn([1]), 1)

    def test_all_same(self):
        for sol in self.solutions:
            self.assertEqual(sol.deleteAndEarn([3, 3, 3]), 9)

    def test_non_adjacent_values(self):
        for sol in self.solutions:
            self.assertEqual(sol.deleteAndEarn([1, 1, 1, 5, 5, 5]), 18)

    def test_two_adjacent(self):
        for sol in self.solutions:
            self.assertEqual(sol.deleteAndEarn([1, 2]), 2)

    def test_large_gap(self):
        for sol in self.solutions:
            self.assertEqual(sol.deleteAndEarn([1, 100]), 101)

    def test_chain(self):
        # 1,2,3,4 -> earn[1]=1, earn[2]=2, earn[3]=3, earn[4]=4
        # house robber: pick 2+4=6 or 1+3=4 -> 6
        for sol in self.solutions:
            self.assertEqual(sol.deleteAndEarn([1, 2, 3, 4]), 6)

    def test_duplicates_favor_skip(self):
        # [3, 3, 3, 4] -> earn[3]=9, earn[4]=4 -> pick 3s = 9
        for sol in self.solutions:
            self.assertEqual(sol.deleteAndEarn([3, 3, 3, 4]), 9)

    def test_max_constraint(self):
        for sol in self.solutions:
            self.assertEqual(sol.deleteAndEarn([10000]), 10000)

    def test_alternating_worth_more(self):
        # [1,1,1,1,2,3,3,3,3] earn[1]=4, earn[2]=2, earn[3]=12
        # pick 1+3 = 4+12 = 16 vs pick 2 = 2 -> 16
        for sol in self.solutions:
            self.assertEqual(sol.deleteAndEarn([1, 1, 1, 1, 2, 3, 3, 3, 3]), 16)


if __name__ == '__main__':
    unittest.main()
