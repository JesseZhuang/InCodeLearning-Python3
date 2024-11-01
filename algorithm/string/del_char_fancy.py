"""leet code 1957, easy"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        res = [ch for i, ch in enumerate(s)
               if i < 2 or s[i - 1] != ch or s[i - 2] != ch]
        return ''.join(res)
