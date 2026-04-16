import unittest

from algorithm.hash.group_anagrams import Solution, Solution2


class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def normalize(self, groups: list[list[str]]) -> list[list[str]]:
        """Sort each group and sort groups by first element for comparison."""
        return sorted(sorted(g) for g in groups)

    def verify(self, strs, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.groupAnagrams(strs)
                self.assertEqual(self.normalize(expected), self.normalize(result))

    def test_example1(self):
        self.verify(
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        )

    def test_example2(self):
        self.verify([""], [[""]])

    def test_example3(self):
        self.verify(["a"], [["a"]])

    def test_all_same(self):
        self.verify(["abc", "bca", "cab"], [["abc", "bca", "cab"]])

    def test_all_different(self):
        self.verify(["a", "b", "c"], [["a"], ["b"], ["c"]])

    def test_empty_list(self):
        self.verify([], [])

    def test_single_char_anagrams(self):
        self.verify(["a", "a", "a"], [["a", "a", "a"]])

    def test_mixed_lengths(self):
        self.verify(
            ["ab", "ba", "abc", "cba", "a"],
            [["ab", "ba"], ["abc", "cba"], ["a"]],
        )


if __name__ == '__main__':
    unittest.main()
