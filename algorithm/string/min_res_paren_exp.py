"""leet code 2232, medium"""

import math


class Solution:
    def minimizeResult(self, expression: str) -> str:
        sp = expression.split("+")
        left, right = sp[0], sp[1]
        min_l, min_r, min_res = 0, 1, math.inf
        for l in range(0, len(left)):
            # a*(b+c)*d
            a = 1 if l == 0 else int(left[:l])
            b = int(left[l:])
            for r in range(1, len(right) + 1):
                c = int(right[:r])
                d = 1 if r == len(right) else int(right[r:])
                res = a * (b + c) * d
                if res < min_res:
                    min_res = res
                    min_l = l
                    min_r = r
        return left[:min_l] + "(" + left[min_l:] + "+" + right[:min_r] + ")" + right[min_r:]
