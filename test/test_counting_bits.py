import unittest

from algorithm.bit.counting_bits import Solution, Solution2


class TestCountingBits(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_zero(self):
        for sol in self.solutions:
            self.assertEqual([0], sol.countBits(0))

    def test_two(self):
        for sol in self.solutions:
            self.assertEqual([0, 1, 1], sol.countBits(2))

    def test_five(self):
        for sol in self.solutions:
            self.assertEqual([0, 1, 1, 2, 1, 2], sol.countBits(5))

    def test_one(self):
        for sol in self.solutions:
            self.assertEqual([0, 1], sol.countBits(1))

    def test_power_of_two(self):
        for sol in self.solutions:
            res = sol.countBits(8)
            self.assertEqual(1, res[8])  # 1000 in binary
            self.assertEqual(1, res[4])  # 100 in binary
            self.assertEqual(1, res[2])  # 10 in binary

    def test_all_bits_set(self):
        for sol in self.solutions:
            res = sol.countBits(15)
            self.assertEqual(4, res[15])  # 1111 in binary
            self.assertEqual(3, res[7])   # 111 in binary
            self.assertEqual(2, res[3])   # 11 in binary

    def test_large(self):
        for sol in self.solutions:
            res = sol.countBits(100000)
            self.assertEqual(100001, len(res))
            self.assertEqual(0, res[0])
            self.assertEqual(bin(100000).count('1'), res[100000])
