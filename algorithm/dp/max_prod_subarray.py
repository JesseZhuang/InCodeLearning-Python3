'''leet code 152 '''

from math import inf
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''O(n) time, O(1) space. 88ms, 16.8MB'''
        max_here, min_here = 1, 1
        res = -inf
        for n in nums:
            # important to calc two products before update
            p1, p2 = max_here * n, min_here * n
            max_here = max(n, p1, p2)
            min_here = min(n, p1, p2)
            res = max(max_here, res)  # missed res, no need min
        return res
