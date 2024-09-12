"""leet code 224, hard"""
from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        vals = deque()
        res, sign, i = 0, 1, 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                n = int(c)
                while i + 1 < len(s) and s[i + 1].isdigit():
                    n = n * 10 + int(s[i + 1])
                    i += 1
                res += n * sign
            elif c == "-":
                sign = -1
            elif c == "+":
                sign = 1
            elif c == "(":
                vals.append(res)
                vals.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res = res * vals.pop() + vals.pop()
            i += 1
        return res

# Solution().calculate("2147483647")  # i+=1 in for i in range does not increment
