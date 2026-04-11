import unittest

from algorithm.jzstring.decode_string import Solution, Solution2


class TestDecodeString(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, s, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.decodeString(s))

    def test_example1(self):
        self.verify("3[a]2[bc]", "aaabcbc")

    def test_example2(self):
        self.verify("3[a2[c]]", "accaccacc")

    def test_example3(self):
        self.verify("2[abc]3[cd]ef", "abcabccdcdcdef")

    def test_no_encoding(self):
        self.verify("abc", "abc")

    def test_single_char_repeat(self):
        self.verify("1[a]", "a")

    def test_large_repeat(self):
        self.verify("10[a]", "aaaaaaaaaa")

    def test_deeply_nested(self):
        self.verify("2[a2[b3[c]]]", "abcccbcccabcccbccc")

    def test_empty_string(self):
        self.verify("", "")

    def test_adjacent_brackets(self):
        self.verify("2[a]2[b]", "aabb")
