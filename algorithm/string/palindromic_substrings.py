"""leet code 647, medium"""
from algorithm.string.Manacher import Manacher


class Solution1:
    """46ms, 16.8mb"""

    def countSubstrings(self, s: str) -> int:
        return Manacher(s).cntPalindromeSubstrings()


class Solution2:
    """151ms, 16.50mb"""

    def countSubstrings(self, s: str) -> int:
        def expand(i: int, j: int) -> int:
            count = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                count += 1
            return count

        res = 0
        for i in range(len(s)):
            res += expand(i, i) + expand(i, i + 1)
        return res
