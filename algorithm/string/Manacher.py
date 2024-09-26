"""Manacher's palindrome search algorithm"""


class Manacher:
    __slots__ = "m", "p", "mppl", "s"

    def __init__(self, s: str) -> None:
        t = ["$", "#"]
        for c in s:
            t.append(c)
            t.append("#")
        t.append("@")
        self.m = m = len(t)
        self.p = p = [0] * m
        self.mppl = 0
        self.s = s

        center = right = 0
        for i in range(1, m - 1):
            mirror = 2 * center - i
            if right > i: p[i] = min(right - i, p[mirror])
            while t[i - (p[i] + 1)] == t[i + (p[i] + 1)]: p[i] += 1
            if i + p[i] > right:
                center = i
                right = i + p[i]
            if i - p[i] == 1: self.mppl = max(self.mppl, p[i])

    def cntPalindromeSubstrings(self) -> int:
        res = 0
        for i in range(1, self.m - 1):
            res += (1 + self.p[i]) // 2
        return res

    def longestPalindromeSubstring(self) -> str:
        max_l = center = 0
        for i in range(1, self.m - 1):
            if self.p[i] > max_l:
                max_l = self.p[i]
                center = i
        return self.s[(center - 1 - max_l) // 2:(center - 1 + max_l) // 2]
