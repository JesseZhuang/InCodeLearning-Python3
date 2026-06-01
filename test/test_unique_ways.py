from algorithm.dp.unique_ways import Solution, Solution2
import unittest


class TestUniquePaths(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for s in self.solutions:
            self.assertEqual(28, s.uniquePaths(3, 7))

    def test_example2(self):
        for s in self.solutions:
            self.assertEqual(3, s.uniquePaths(3, 2))

    def test_1x1(self):
        for s in self.solutions:
            self.assertEqual(1, s.uniquePaths(1, 1))

    def test_1xn(self):
        for s in self.solutions:
            self.assertEqual(1, s.uniquePaths(1, 100))

    def test_mx1(self):
        for s in self.solutions:
            self.assertEqual(1, s.uniquePaths(100, 1))

    def test_symmetric(self):
        for s in self.solutions:
            self.assertEqual(s.uniquePaths(3, 7), s.uniquePaths(7, 3))

    def test_large(self):
        for s in self.solutions:
            self.assertEqual(48620, s.uniquePaths(10, 10))


if __name__ == '__main__':
    unittest.main()
