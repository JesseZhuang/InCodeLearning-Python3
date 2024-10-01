"""
biweekly 140, Q4, hard
return the smallest starting index of s that the substring starting at that index is almost equal to pattern.
if no such index exists, return -1.

Constraints:
1. 1 <= word2.length < word1.length <= 3 * 10^5, n,m
2. word1 and word2 consist only of lowercase English letters
"""

from algorithm.string.z_func import zfunc


class Solution2:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        n, m = len(s), len(pattern)  # ggabcqe, abcde len:7,5
        z1 = zfunc(pattern + s)
        z2 = zfunc(pattern[::-1] + s[::-1])
        for i in range(n):
            if i + m > n: break
            c1 = z1[i + m]  # longest prefix of pattern in s
            if c1 >= m: return i
            j = i - 1 + m  # assume i:2, c j:6 g, right after pattern string, c1:3
            c2 = z2[n + m - 1 - j]  # n+m-1: len(concat) l-j:5. c2:1 found almost equal
            if c1 + c2 == m - 1: return i
        return -1
