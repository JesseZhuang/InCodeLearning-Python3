"""leet 1930, medium"""
from math import inf


class Solution:
    """266 ms, 19.3 mb"""

    def countPalindromicSubsequence(self, s: str) -> int:
        first, last, res = [inf] * 26, [0] * 26, 0
        for i, c in enumerate(s):
            id = ord(c) - ord('a')
            first[id] = min(i, first[id])
            last[id] = i
        for i in range(26):
            if first[i] < last[i]:
                res += len(set(list(s[first[i] + 1:last[i]])))
        return res
