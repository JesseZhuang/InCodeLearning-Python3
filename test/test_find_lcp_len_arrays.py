import unittest

from algorithm.jzstring.find_lcp_len_arrays import Solution, Solution2


class TestFindLCPLenArrays(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, arr1, arr2, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.longestCommonPrefix(arr1, arr2))

    def test_example1(self):
        self.verify([1, 10, 100], [1000], 3)

    def test_example2(self):
        self.verify([1, 2, 3], [4, 4, 4], 0)


if __name__ == '__main__':
    unittest.main()
