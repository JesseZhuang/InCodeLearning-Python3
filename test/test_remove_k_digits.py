import unittest

from algorithm.stack.remove_k_digits import Solution


class TestRemoveKDigits(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(sol.removeKdigits("1432219", 3), "1219")

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.removeKdigits("10200", 1), "200")

    def test_example3(self):
        for sol in self.solutions:
            self.assertEqual(sol.removeKdigits("10", 2), "0")

    def test_single_digit(self):
        for sol in self.solutions:
            self.assertEqual(sol.removeKdigits("9", 1), "0")

    def test_no_removal(self):
        for sol in self.solutions:
            self.assertEqual(sol.removeKdigits("123", 0), "123")

    def test_all_same_digits(self):
        for sol in self.solutions:
            self.assertEqual(sol.removeKdigits("1111", 2), "11")

    def test_descending(self):
        for sol in self.solutions:
            self.assertEqual(sol.removeKdigits("9876", 2), "76")

    def test_leading_zeros(self):
        for sol in self.solutions:
            self.assertEqual(sol.removeKdigits("10001", 1), "1")

    def test_remove_from_end(self):
        for sol in self.solutions:
            self.assertEqual(sol.removeKdigits("1234", 2), "12")

    def test_large_k(self):
        for sol in self.solutions:
            self.assertEqual(sol.removeKdigits("112", 1), "11")


if __name__ == "__main__":
    unittest.main()
