from unittest import TestCase

from algorithm.deq.parse_bool_expression import Solution1, Solution2


class TestSolution(TestCase):

    def setUp(self) -> None:
        self.tbt1 = Solution1()
        self.tbt2 = Solution2()

    def test_parse_bool_expr(self):
        self.assertEqual(True, self.tbt2.parseBoolExpr("|(f,f,f,t)"))
        self.assertEqual(True, self.tbt1.parseBoolExpr("|(f,f,f,t)"))

    def test_eval(self):
        """
        eval basically evaluates the string as python code and return result
        so return eval("t") -> return t, when parameter t is default to True, result is true
        """

        def test1(s, t=True, f=False, one=1):
            return eval(s)

        self.assertEqual(True, test1("t"))
        self.assertEqual(False, test1("t and f"))
        self.assertEqual(1, test1("t + f"))
        self.assertEqual(2, test1("t + one"))
