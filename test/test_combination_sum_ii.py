import unittest

from algorithm.jzarray.combination_sum_ii import Solution, Solution2


class TestCombinationSumII(unittest.TestCase):

    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    @staticmethod
    def sorted_result(result):
        return sorted([sorted(c) for c in result])

    def test_example1(self):
        """candidates=[10,1,2,7,6,1,5], target=8"""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
                expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
                self.assertEqual(self.sorted_result(result), self.sorted_result(expected))

    def test_example2(self):
        """candidates=[2,5,2,1,2], target=5"""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.combinationSum2([2, 5, 2, 1, 2], 5)
                expected = [[1, 2, 2], [5]]
                self.assertEqual(self.sorted_result(result), self.sorted_result(expected))

    def test_no_solution(self):
        """target too large"""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.combinationSum2([2, 4, 6], 1)
                self.assertEqual(result, [])

    def test_single_element_match(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.combinationSum2([1], 1)
                self.assertEqual(self.sorted_result(result), [[1]])

    def test_single_element_no_match(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.combinationSum2([2], 1)
                self.assertEqual(result, [])

    def test_all_same_elements(self):
        """candidates=[1,1,1,1,1], target=3"""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.combinationSum2([1, 1, 1, 1, 1], 3)
                self.assertEqual(self.sorted_result(result), [[1, 1, 1]])

    def test_all_same_elements_exact(self):
        """candidates=[3,3,3], target=9"""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.combinationSum2([3, 3, 3], 9)
                self.assertEqual(self.sorted_result(result), [[3, 3, 3]])

    def test_duplicates_no_combo(self):
        """candidates=[3,3,3], target=10"""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.combinationSum2([3, 3, 3], 10)
                self.assertEqual(result, [])

    def test_multiple_duplicates(self):
        """candidates=[1,1,1,2,2], target=4"""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.combinationSum2([1, 1, 1, 2, 2], 4)
                expected = [[1, 1, 2], [2, 2]]
                self.assertEqual(self.sorted_result(result), self.sorted_result(expected))

    def test_large_candidates(self):
        """all candidates exceed target"""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.combinationSum2([50, 40, 30], 5)
                self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
