import unittest
from algorithm.dp.diff_ways_parentheses import Solution1, Solution2


class TestDiffWaysParentheses(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution1(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(sorted(sol.diffWaysToCompute("2-1-1")), [0, 2])

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sorted(sol.diffWaysToCompute("2*3-4*5")), [-34, -14, -10, -10, 10])

    def test_single_number(self):
        for sol in self.solutions:
            self.assertEqual(sol.diffWaysToCompute("3"), [3])

    def test_two_digit_number(self):
        for sol in self.solutions:
            self.assertEqual(sol.diffWaysToCompute("11"), [11])

    def test_single_operator(self):
        for sol in self.solutions:
            self.assertEqual(sol.diffWaysToCompute("2+3"), [5])

    def test_single_subtraction(self):
        for sol in self.solutions:
            self.assertEqual(sol.diffWaysToCompute("5-2"), [3])

    def test_single_multiplication(self):
        for sol in self.solutions:
            self.assertEqual(sol.diffWaysToCompute("4*3"), [12])

    def test_all_addition(self):
        for sol in self.solutions:
            self.assertEqual(sorted(sol.diffWaysToCompute("1+2+3")), [6, 6])

    def test_all_multiplication(self):
        for sol in self.solutions:
            self.assertEqual(sorted(sol.diffWaysToCompute("2*3*4")), [24, 24])

    def test_mixed_operators(self):
        for sol in self.solutions:
            result = sorted(sol.diffWaysToCompute("1+2*3"))
            self.assertEqual(result, [7, 9])

    def test_two_digit_operands(self):
        for sol in self.solutions:
            self.assertEqual(sorted(sol.diffWaysToCompute("10+5")), [15])

    def test_zeros(self):
        for sol in self.solutions:
            self.assertEqual(sorted(sol.diffWaysToCompute("0+0")), [0])

    def test_negative_results(self):
        for sol in self.solutions:
            result = sorted(sol.diffWaysToCompute("1-2-3"))
            self.assertEqual(result, [-4, 2])


if __name__ == '__main__':
    unittest.main()
