import unittest

from algorithm.tree.subtree_sizes_after_change import Solution


class TestStrings(unittest.TestCase):
    def test1(self):
        tbt = Solution()
        cases = [
            ([-1, 0, 1, 2, 3], "abbbb", [5, 4, 3, 2, 1]),  # no parent change needed
            ([-1, 0, 0, 1, 1, 1], "abaabc", [6, 3, 1, 1, 1, 1]),
            ([-1, 0, 4, 0, 1], "abbba", [5, 2, 1, 1, 1]),
            ([-1, 10, 0, 12, 10, 18, 11, 12, 2, 3, 2, 2, 2, 0, 4, 11, 4, 2, 0], "babadabbdabcbaceeda",
             [19, 1, 15, 2, 3, 1, 1, 1, 1, 1, 5, 2, 4, 1, 1, 1, 1, 1, 2]),
        ]
        for parent, s, expected in cases:
            with self.subTest(parent=parent, s=s, expected=expected):
                self.assertEqual(tbt.findSubtreeSizes(parent, s), expected)
