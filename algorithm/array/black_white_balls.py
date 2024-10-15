"""leet code 2938, medium"""


class Solution:
    def minimumSteps(self, s: str) -> int:
        res = j = 0
        for i, c in enumerate(s):
            if c == '0':
                res += i - j
                j += 1
        return res
