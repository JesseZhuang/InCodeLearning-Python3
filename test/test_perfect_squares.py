from unittest import TestCase

from algorithm.dp.perfect_squares import Solution, Solution2


class TestPerfectSquares(TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(3, sol.numSquares(12))  # 4+4+4

    def test_example2(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(2, sol.numSquares(13))  # 4+9

    def test_perfect_square(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(1, sol.numSquares(1))
                self.assertEqual(1, sol.numSquares(4))
                self.assertEqual(1, sol.numSquares(9))
                self.assertEqual(1, sol.numSquares(100))

    def test_two_squares(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(2, sol.numSquares(2))   # 1+1
                self.assertEqual(2, sol.numSquares(5))   # 1+4
                self.assertEqual(2, sol.numSquares(10))  # 1+9

    def test_three_squares(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(3, sol.numSquares(3))   # 1+1+1
                self.assertEqual(3, sol.numSquares(6))   # 1+1+4

    def test_four_squares(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(4, sol.numSquares(7))   # 4+1+1+1
                self.assertEqual(4, sol.numSquares(15))  # by Legendre's theorem

    def test_large(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(1, sol.numSquares(10000))  # 100^2
                self.assertEqual(4, sol.numSquares(9999))   # Legendre: 9999 % 8 == 7

    def test_boundary(self):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(1, sol.numSquares(1))
