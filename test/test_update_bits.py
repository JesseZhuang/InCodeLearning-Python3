from unittest import TestCase

from algorithm.bit.update_bits import Solution


class TestSolution2(TestCase):

    def test_update_bits(self):
        tbt = Solution()
        cases = [
            (1024, 21, 2, 6, 1108),  # (10001010100)2
            (456, 31, 27, 31, -134217272),
            (1, -1, 0, 31, -1)
        ]
        for n, m, i, j, exp in cases:
            with self.subTest(n=n, m=m, i=i, j=j):
                self.assertEqual(exp, tbt.updateBits(n, m, i, j))
