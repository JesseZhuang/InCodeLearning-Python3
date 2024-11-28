"""leet code 5, medium"""
from algorithm.jzstring.Manacher import Manacher


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return Manacher(s).longestPalindromeSubstring()


class Solution2:
    """275ms, 16.61,b"""

    def __init__(self):
        self.left = 0
        self.max_l = 0

    def longestPalindrome(self, s: str) -> str:

        def expand(i: int, j: int):
            left, right = i, j
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > self.max_l:
                self.max_l = right - left - 1
                self.left = left + 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return s[self.left:self.left + self.max_l]
