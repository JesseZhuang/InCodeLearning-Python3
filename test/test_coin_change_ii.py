import unittest

from algorithm.dp.coin_change_ii import Solution, Solution2


class TestCoinChangeII(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for s in self.solutions:
            self.assertEqual(4, s.change(5, [1, 2, 5]))

    def test_example2(self):
        for s in self.solutions:
            self.assertEqual(0, s.change(3, [2]))

    def test_example3(self):
        for s in self.solutions:
            self.assertEqual(1, s.change(10, [10]))

    def test_amount_zero(self):
        for s in self.solutions:
            self.assertEqual(1, s.change(0, [1, 2, 5]))

    def test_single_coin(self):
        for s in self.solutions:
            self.assertEqual(1, s.change(7, [7]))
            self.assertEqual(0, s.change(7, [3]))

    def test_large(self):
        for s in self.solutions:
            self.assertEqual(242, s.change(100, [1, 5, 10, 25]))


if __name__ == '__main__':
    unittest.main()
