"""
biweekly 140, Q3, medium
A string x is almost equal to y if you can change one character in x to make it identical to y.
valid sequence
1. indices ascending
2. concatenating characters at the indices in word1 result in a string almost equal to word2.
return lexicographically the smallest sequence of word2.length. if not possible, return empty sequence.

Constraints:
1. 1 <= word2.length < word1.length <= 3 * 10^5, n,m
2. word1 and word2 consist only of lowercase English letters
"""
from typing import List


class Solution:
    """m+n, m"""

    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        dp = [-1] * (m + 1)
        dp[m] = m + 1  # dp[i]: max index in word1 that word2[i] can be found, word1[dp[i]]==word2[i]
        i, j = n - 1, m - 1
        while j >= 0:
            while i >= 0 and word1[i] != word2[j]: i -= 1
            if i < 0: break
            dp[j] = i
            i -= 1
            j -= 1
        i, j = 0, 0
        res = []
        mk = 0  # almost, mismatch used or not
        while j < m:  # try to match word2[j] greedily
            if i >= n: return []  # depleted word1
            if word1[i] == word2[j]:
                res.append(i)
                i += 1
            else:
                if mk == 0 and dp[j + 1] >= i + 1:  # use mismatch because word2[j+1] can be matched later
                    res.append(i)
                    mk = 1
                    i += 1
                else:
                    while i < n and word1[i] != word2[j]: i += 1
                    if i >= n: return []
                    res.append(i)  # match word1[i]==word2[j]
                    i += 1
            j += 1
        return res
