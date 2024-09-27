"""leet code 214, hard"""
from algorithm.string.KMP import KMP
from algorithm.string.Manacher import Manacher


class SolutionKmp:
    """59ms, 20.7mb"""

    def shortestPalindrome(self, s: str) -> str:
        combine = s + "#" + s[::-1]
        table = KMP(combine).table
        palin_len = table[len(combine) - 1]
        if palin_len == len(s): return s
        return s[palin_len:][::-1] + s


class SolutionManacher:
    """154ms, 20.98mb"""

    def shortestPalindrome(self, s: str) -> str:
        mppl = Manacher(s).mppl
        return s[mppl:][::-1] + s
