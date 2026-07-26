import unittest

from algorithm.graph.evaluate_division import Solution, Solution2


class TestEvaluateDivision(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        expected = [6.0, 0.5, -1.0, 1.0, -1.0]
        for sol in self.solutions:
            result = sol.calcEquation(equations, values, queries)
            for r, e in zip(result, expected):
                self.assertAlmostEqual(r, e, places=5)

    def test_example2(self):
        equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
        values = [1.5, 2.5, 5.0]
        queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
        expected = [3.75, 0.4, 5.0, 0.2]
        for sol in self.solutions:
            result = sol.calcEquation(equations, values, queries)
            for r, e in zip(result, expected):
                self.assertAlmostEqual(r, e, places=5)

    def test_example3(self):
        equations = [["a", "b"]]
        values = [0.5]
        queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
        expected = [0.5, 2.0, -1.0, -1.0]
        for sol in self.solutions:
            result = sol.calcEquation(equations, values, queries)
            for r, e in zip(result, expected):
                self.assertAlmostEqual(r, e, places=5)

    def test_single_variable(self):
        equations = [["a", "b"]]
        values = [2.0]
        queries = [["a", "a"], ["b", "b"]]
        expected = [1.0, 1.0]
        for sol in self.solutions:
            result = sol.calcEquation(equations, values, queries)
            for r, e in zip(result, expected):
                self.assertAlmostEqual(r, e, places=5)

    def test_disconnected_components(self):
        equations = [["a", "b"], ["c", "d"]]
        values = [2.0, 3.0]
        queries = [["a", "d"], ["c", "b"]]
        expected = [-1.0, -1.0]
        for sol in self.solutions:
            result = sol.calcEquation(equations, values, queries)
            for r, e in zip(result, expected):
                self.assertAlmostEqual(r, e, places=5)

    def test_chain(self):
        equations = [["a", "b"], ["b", "c"], ["c", "d"], ["d", "e"]]
        values = [2.0, 3.0, 4.0, 5.0]
        queries = [["a", "e"], ["e", "a"]]
        expected = [120.0, 1.0 / 120.0]
        for sol in self.solutions:
            result = sol.calcEquation(equations, values, queries)
            for r, e in zip(result, expected):
                self.assertAlmostEqual(r, e, places=5)


if __name__ == "__main__":
    unittest.main()
