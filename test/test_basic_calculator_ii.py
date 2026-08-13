import unittest

from algorithm.deq.basic_calculator_ii import Solution


class TestBasicCalculatorII(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_examples(self):
        for sol in self.solutions:
            self.assertEqual(sol.calculate("3+2*2"), 7)
            self.assertEqual(sol.calculate(" 3/2 "), 1)
            self.assertEqual(sol.calculate(" 3+5 / 2 "), 5)

    def test_edge_cases(self):
        for sol in self.solutions:
            self.assertEqual(sol.calculate("1-1+1"), 1)
            self.assertEqual(sol.calculate("2147483647"), 2147483647)
            self.assertEqual(sol.calculate("0"), 0)
            self.assertEqual(sol.calculate("1+1+1+1+1"), 5)
            self.assertEqual(sol.calculate("14-3/2"), 13)

    def test_all_operators(self):
        for sol in self.solutions:
            self.assertEqual(sol.calculate("2*3+4"), 10)
            self.assertEqual(sol.calculate("2+3*4"), 14)
            self.assertEqual(sol.calculate("10-2*3+1"), 5)
            self.assertEqual(sol.calculate("100/10/2"), 5)


if __name__ == "__main__":
    unittest.main()
