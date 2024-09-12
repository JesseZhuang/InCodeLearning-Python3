"""leet code 227, medium """
from math import trunc


class Solution:
    def calculate(self, s):
        res, cur, last, prev_op = 0, 0, 0, '+'
        for c in s + "##":  # finish processing in loop
            if c.isspace():
                continue
            elif c.isdigit():
                cur = cur * 10 + int(c)
            else:
                if prev_op == '*':
                    last *= cur
                elif prev_op == '/':
                    last = trunc(last / cur)
                else:
                    res += last
                    last = cur if prev_op == '+' else -cur
                prev_op, cur = c, 0
        return res
