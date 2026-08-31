import unittest
from math import isclose

from algorithm.jzmath.pow_x_n import Solution, Solution2


class TestPowXN(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, x, n, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertTrue(isclose(sol.myPow(x, n), expected, rel_tol=1e-5))

    def test_example1(self):
        self.verify(2.0, 10, 1024.0)

    def test_example2(self):
        self.verify(2.1, 3, 9.261)

    def test_example3(self):
        self.verify(2.0, -2, 0.25)

    def test_zero_exponent(self):
        self.verify(2.0, 0, 1.0)
        self.verify(0.0, 0, 1.0)

    def test_one_exponent(self):
        self.verify(5.0, 1, 5.0)

    def test_negative_base_even(self):
        self.verify(-2.0, 4, 16.0)

    def test_negative_base_odd(self):
        self.verify(-2.0, 3, -8.0)

    def test_fractional_base(self):
        self.verify(0.5, 3, 0.125)

    def test_large_negative_exponent(self):
        self.verify(2.0, -3, 0.125)

    def test_int_min_exponent(self):
        """n = -2^31, tests overflow handling."""
        result = Solution().myPow(1.0, -2147483648)
        self.assertTrue(isclose(result, 1.0, rel_tol=1e-5))
        result2 = Solution2().myPow(1.0, -2147483648)
        self.assertTrue(isclose(result2, 1.0, rel_tol=1e-5))

    def test_base_one(self):
        self.verify(1.0, 2147483647, 1.0)

    def test_base_negative_one_even(self):
        self.verify(-1.0, 100, 1.0)

    def test_base_negative_one_odd(self):
        self.verify(-1.0, 99, -1.0)
