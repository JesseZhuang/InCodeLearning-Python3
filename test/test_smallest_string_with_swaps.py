import unittest

from algorithm.graph.smallest_string_with_swaps import Solution, Solution2


class TestSmallestStringWithSwaps(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, s, pairs, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.smallestStringWithSwaps(s, pairs))

    def test_example1(self):
        self.verify("dcab", [[0, 3], [1, 2]], "bacd")

    def test_example2(self):
        self.verify("dcab", [[0, 3], [1, 2], [0, 2]], "abcd")

    def test_example3(self):
        self.verify("cba", [[0, 1], [1, 2]], "abc")

    def test_single_char(self):
        self.verify("a", [], "a")

    def test_no_pairs(self):
        self.verify("dcba", [], "dcba")

    def test_all_connected(self):
        self.verify("zyx", [[0, 1], [1, 2]], "xyz")

    def test_duplicate_pairs(self):
        self.verify("dcab", [[0, 3], [0, 3], [1, 2]], "bacd")

    def test_self_loop(self):
        self.verify("ba", [[0, 0]], "ba")

    def test_transitive_chain(self):
        self.verify("edcba", [[0, 1], [1, 2], [2, 3], [3, 4]], "abcde")

    def test_two_groups(self):
        self.verify("dcbaf", [[0, 1], [2, 3]], "cdabf")

    def test_already_sorted(self):
        self.verify("abc", [[0, 1], [1, 2]], "abc")
