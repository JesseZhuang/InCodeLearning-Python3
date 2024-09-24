"""leet code 214, hard"""
from algorithm.string.KMP import KMP


class Solution:
    """59ms, 20.7mb"""

    def shortestPalindrome(self, s: str) -> str:
        combine = s + "#" + s[::-1]
        table = KMP(combine).table
        palin_len = table[len(combine) - 1]
        if palin_len == len(s): return s
        return s[palin_len:][::-1] + s
