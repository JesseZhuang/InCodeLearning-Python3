"""leet code 2275, medium"""
from typing import List


class Solution:
    """315ms"""

    def largestCombination(self, candidates: List[int]) -> int:
        res, cur = 0, 0
        i = 1
        while i <= 10_000_000:
            cnt = 0
            for c in candidates:
                if c & i: cnt += 1
            res = max(res, cnt)
            i <<= 1
        return res


class Solution2:
    """659ms"""

    def largestCombination(self, A):
        return max(sum(1 << i & a > 0 for a in A) for i in range(24))
