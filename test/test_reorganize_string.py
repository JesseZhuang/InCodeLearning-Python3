import unittest
from collections import Counter

from algorithm.heap.reorganize_string import Solution, Solution2, Solution3


def is_valid(result: str, s: str) -> bool:
    if sorted(result) != sorted(s):
        return False
    for i in range(1, len(result)):
        if result[i] == result[i - 1]:
            return False
    return True


class TestReorganizeString(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2(), Solution3()]

    def test_example1(self):
        for sol in self.solutions:
            res = sol.reorganizeString("aab")
            self.assertTrue(is_valid(res, "aab"))

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(sol.reorganizeString("aaab"), "")

    def test_single_char(self):
        for sol in self.solutions:
            self.assertEqual(sol.reorganizeString("a"), "a")

    def test_two_same(self):
        for sol in self.solutions:
            self.assertEqual(sol.reorganizeString("aa"), "")

    def test_two_different(self):
        for sol in self.solutions:
            res = sol.reorganizeString("ab")
            self.assertTrue(is_valid(res, "ab"))

    def test_all_same(self):
        for sol in self.solutions:
            self.assertEqual(sol.reorganizeString("aaaa"), "")

    def test_balanced(self):
        for sol in self.solutions:
            res = sol.reorganizeString("aabb")
            self.assertTrue(is_valid(res, "aabb"))

    def test_max_frequency_boundary(self):
        # n=5, max freq can be 3: "aaabb" -> "ababa"
        for sol in self.solutions:
            res = sol.reorganizeString("aaabb")
            self.assertTrue(is_valid(res, "aaabb"))

    def test_longer(self):
        for sol in self.solutions:
            res = sol.reorganizeString("vvvlo")
            self.assertTrue(is_valid(res, "vvvlo"))
