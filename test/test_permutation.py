import unittest

from algorithm.jzarray.permutation import Solution, Solution2


class TestPermutation(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        expected = {(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)}
        for sol in self.solutions:
            result = sol.permute([1, 2, 3])
            self.assertEqual({tuple(p) for p in result}, expected)

    def test_example2(self):
        expected = {(0, 1), (1, 0)}
        for sol in self.solutions:
            result = sol.permute([0, 1])
            self.assertEqual({tuple(p) for p in result}, expected)

    def test_single(self):
        for sol in self.solutions:
            self.assertEqual(sol.permute([1]), [[1]])

    def test_negative(self):
        expected = {(-1, 0), (0, -1)}
        for sol in self.solutions:
            result = sol.permute([-1, 0])
            self.assertEqual({tuple(p) for p in result}, expected)

    def test_four_elements(self):
        for sol in self.solutions:
            result = sol.permute([1, 2, 3, 4])
            self.assertEqual(len(result), 24)
            self.assertEqual(len({tuple(p) for p in result}), 24)

    def test_max_size(self):
        for sol in self.solutions:
            result = sol.permute([1, 2, 3, 4, 5, 6])
            self.assertEqual(len(result), 720)


if __name__ == "__main__":
    unittest.main()
