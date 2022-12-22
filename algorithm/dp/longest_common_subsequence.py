"""leetcode 1143"""


import functools
# pylint: disable=invalid-name


def longestCommonSubsequenceDP(self, text1: str, text2: str) -> int:
    '''dp, O(MN)time, O(min(M,N)) space, 322ms, 13.8Mb'''
    m, n = map(len, (text1, text2))
    if m < n:
        return self.longestCommonSubsequence(text2, text1)
    dp = [0] * (n + 1)
    for char1 in text1:
        prevRow, prevRowPrevCol = 0, 0
        for j, char2 in enumerate(text2):
            prevRow, prevRowPrevCol = dp[j + 1], prevRow
            dp[j + 1] = prevRowPrevCol + 1 if char1 == char2 else max(dp[j], prevRow)
    return dp[-1]


def longestCommonSubsequenceRecursive(self, text1: str, text2: str) -> int:
    '''726ms, 140.5Mb. O(2^N) time and space'''
    @functools.lru_cache(None)
    def helper(i, j):
        if i < 0 or j < 0:
            return 0
        if text1[i] == text2[j]:
            return helper(i-1, j-1)+1
        return max(helper(i-1, j), helper(i, j-1))
    return helper(len(text1)-1, len(text2)-1)
