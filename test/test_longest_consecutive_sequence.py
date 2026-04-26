import unittest

from algorithm.hash.longest_consecutive_sequence import Solution, Solution2


class TestLongestConsecutiveSequence(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, nums, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.longestConsecutive(nums))

    def test_example1(self):
        self.verify([100, 4, 200, 1, 3, 2], 4)

    def test_example2(self):
        self.verify([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9)

    def test_empty(self):
        self.verify([], 0)

    def test_single(self):
        self.verify([1], 1)

    def test_duplicates(self):
        self.verify([1, 2, 0, 1], 3)

    def test_negative(self):
        self.verify([-1, -2, -3, 0, 1], 5)

    def test_no_consecutive(self):
        self.verify([10, 30, 50], 1)

    def test_all_same(self):
        self.verify([5, 5, 5, 5], 1)

    def test_two_sequences(self):
        self.verify([1, 2, 3, 10, 11, 12, 13], 4)


if __name__ == '__main__':
    unittest.main()
