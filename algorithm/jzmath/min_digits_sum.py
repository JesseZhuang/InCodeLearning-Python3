"""
leet code 3300, biweekly 140, Q1, easy

1 <= nums.length <= 100, n
1 <= nums[i] <= 10^4, d:digits <=5
"""
from typing import List


class Solution1:
    """nd,1"""

    def minElement(self, nums: List[int]) -> int:
        res = float('inf')
        for n in nums:
            sum = 0
            while n > 0:
                sum += n % 10
                n //= 10
            res = min(res, sum)
        return res


class Solution2:
    """nd,nd"""

    def minElement(self, nums: List[int]) -> int:
        def add_digits(n):
            return sum([int(c) for c in str(n)])

        return min(map(add_digits, nums))
