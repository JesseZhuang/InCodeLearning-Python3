"""
biweekly 140, Q2, medium
maximumHeight[i] denotes the maximum height the ith tower can be assigned
1. no two towers have same height
2. tower height should be a positive int
return max total sum, -1 if not possible.

Constraints:
1 <= maximumHeight.length<= 10^5, n
1 <= maximumHeight[i] <= 10^9, m
"""
from collections import Counter, defaultdict
from typing import List


class Solution1:
    """nlgn, 1, one pass"""

    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        r = 0
        hs = sorted(maximumHeight, reverse=True)
        p = -1
        for h in hs:
            if p == -1:
                r += h
                p = h - 1
            else:
                h = min(h, p)
                r += h
                p = h - 1
            if h <= 0: return -1
        return r


class Solution2:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        """
        n, m+n. three passes n.
        TLE when using python set for mem (memorize whether this height has been assigned
        MLE when using boolean array for mem
        """
        counts = Counter(maximumHeight)  # size k, k<n
        mem = dict()  # size n, may grow to m
        for h in counts: mem[h] = h - 1
        res = 0
        for h, cnt in counts.items():
            res += h
            while cnt > 1:
                nh = mem[h]
                while nh in mem: nh -= 1
                if nh == 0: return -1
                mem[nh] = nh - 1
                res += nh
                mem[h] = nh - 1
                cnt -= 1
        return res

    def maximumTotalSum2(self, maximumHeight):
        """n,m+n. two passes n"""
        counts = defaultdict(int)
        mem = dict()
        for h in maximumHeight:
            counts[h] += 1
            if h not in mem:
                mem[h] = h - 1
            else:
                while mem[h] in mem:
                    mem[h] -= 1
                    if mem[h] == 0: return -1
        res = 0
        for h, cnt in counts.items():
            res += h
            while cnt > 1:
                nh = mem[h]
                while nh in mem: nh -= 1
                if nh == 0: return -1
                res += nh
                mem[h] = mem[nh] = nh - 1
                cnt -= 1
        return res
