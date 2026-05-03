from unittest import TestCase

from algorithm.dp.gen_parentheses import Solution, Solution2


class TestSolution(TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_n1(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sorted(sol.generateParenthesis(1)), ['()'])

    def test_n2(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sorted(sol.generateParenthesis(2)), sorted(['(())', '()()']))

    def test_n3(self):
        expected = sorted(['((()))', '(()())', '(())()', '()(())', '()()()'])
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sorted(sol.generateParenthesis(3)), expected)

    def test_n4(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.generateParenthesis(4)
                self.assertEqual(len(result), 14)  # Catalan(4) = 14
                self.assertEqual(len(set(result)), 14)

    def test_n0_edge(self):
        """n=0 not in constraints (1<=n<=8) but DP handles it."""
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.generateParenthesis(0)
                self.assertEqual(result, [''])
