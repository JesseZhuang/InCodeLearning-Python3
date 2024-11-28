"""leet code 214, hard"""
from algorithm.jzstring.KMP import KMP
from algorithm.jzstring.Manacher import Manacher


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


class SolutionHash:
    """47 ms, 18.02 mb"""

    def shortestPalindrome(self, s: str) -> str:
        base, pow, mod, end, forward, reverse = 31, 1, 1e9 + 7, -1, 0, 0
        for i, c in enumerate(s):
            id = ord(c) - ord('a') + 1
            forward = (forward * base + id) % mod
            reverse = (reverse + id * pow) % mod
            pow = (pow * base) % mod
            if forward == reverse: end = i
        return s[end + 1:][::-1] + s
