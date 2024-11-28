"""leet code 2232, medium"""

from math import inf


class Solution:
    def minimizeResult(self, expression: str) -> str:
        sp = expression.split("+")
        l, r = sp[0], sp[1]
        min_l, min_r, min_res = 0, 1, inf
        for i in range(0, len(l)):
            # a*(b+c)*d
            a = 1 if i == 0 else int(l[:i])
            b = int(l[i:])
            for j in range(1, len(r) + 1):
                c = int(r[:j])
                d = 1 if j == len(r) else int(r[j:])
                res = a * (b + c) * d
                if res < min_res:
                    min_res = res
                    min_l = i
                    min_r = j
        return l[:min_l] + "(" + l[min_l:] + "+" + r[:min_r] + ")" + r[min_r:]
