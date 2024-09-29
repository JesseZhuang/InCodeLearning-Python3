"""
biweekly 140, Q1, easy

1 <= nums.length <= 100, n
1 <= nums[i] <= 10^4, d:digits, <=5
"""
from typing import List


class Solution1:
    """nd,n"""

    def minElement(self, nums: List[int]) -> int:
        res = []
        for n in nums:
            sum = 0
            while n > 0:
                sum += n % 10
                n //= 10
            res.append(sum)
        return min(res)


class Solution2:
    """nd,nd"""

    def minElement(self, nums: List[int]) -> int:
        def check(n):
            return sum([int(c) for c in str(n)])

        return min([check(n) for n in nums])
