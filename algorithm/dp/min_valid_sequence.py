"""
leet code 3302, biweekly 140, Q3, medium
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
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        last = [-1] * m
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1
        res = []
        skip = j = 0
        for i, c in enumerate(word1):
            if j == m: break
            if c == word2[j] or skip == 0 and (j == m - 1 or i < last[j + 1]):
                skip += c != word2[j]
                res.append(i)
                j += 1
        return res if j == m else []
