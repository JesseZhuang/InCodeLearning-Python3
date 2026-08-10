import unittest

from algorithm.jzarray.subsets_ii import Solution, Solution2


class TestSubsetsII(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            res = sol.subsetsWithDup([1, 2, 2])
            res_set = {tuple(sorted(s)) for s in res}
            expected = {(), (1,), (2,), (1, 2), (2, 2), (1, 2, 2)}
            self.assertEqual(res_set, expected)
            self.assertEqual(len(res), 6)

    def test_example2(self):
        for sol in self.solutions:
            res = sol.subsetsWithDup([0])
            res_set = {tuple(s) for s in res}
            expected = {(), (0,)}
            self.assertEqual(res_set, expected)

    def test_all_duplicates(self):
        for sol in self.solutions:
            res = sol.subsetsWithDup([1, 1, 1])
            res_set = {tuple(s) for s in res}
            expected = {(), (1,), (1, 1), (1, 1, 1)}
            self.assertEqual(res_set, expected)
            self.assertEqual(len(res), 4)

    def test_no_duplicates(self):
        for sol in self.solutions:
            res = sol.subsetsWithDup([1, 2, 3])
            self.assertEqual(len(res), 8)

    def test_multiple_duplicate_groups(self):
        for sol in self.solutions:
            res = sol.subsetsWithDup([1, 2, 2, 3, 3])
            expected_count = 18  # (1+1)*(2+1)*(2+1) = 18
            self.assertEqual(len(res), expected_count)

    def test_negative_numbers(self):
        for sol in self.solutions:
            res = sol.subsetsWithDup([-1, -1, 2])
            res_set = {tuple(s) for s in res}
            expected = {(), (-1,), (-1, -1), (2,), (-1, 2), (-1, -1, 2)}
            self.assertEqual(res_set, expected)

    def test_single_element(self):
        for sol in self.solutions:
            res = sol.subsetsWithDup([5])
            self.assertEqual(len(res), 2)

    def test_max_constraint(self):
        for sol in self.solutions:
            nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
            res = sol.subsetsWithDup(nums)
            expected_count = 3**5  # each of 5 groups has 3 choices (0, 1, or 2)
            self.assertEqual(len(res), expected_count)


if __name__ == "__main__":
    unittest.main()
