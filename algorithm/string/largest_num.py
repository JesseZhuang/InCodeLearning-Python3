"""leet code 179 medium"""

from functools import cmp_to_key
from typing import List


class Solution:

    def largestNumber1(self, nums: List[int]) -> str:
        s_nums = [str(n) for n in nums]

        def cmp(s1, s2):
            if s1 + s2 < s2 + s1:
                return -1
            elif s1 + s2 > s1 + s1:
                return 1
            else:
                return 0

        s_nums.sort(key=cmp_to_key(cmp))
        if s_nums[0] == "0": return "0"
        return "".join(s_nums)

    def largestNumber2(self, nums: List[int]) -> str:
        """34ms, 16.6mb"""
        a = list(map(str, nums))
        a.sort(key=cmp_to_key(lambda x, y: (x + y < y + x) * 2 - 1))  # (x + y < y + x) - (x + y > y + x)
        if a[0] == "0": return "0"
        return "".join(a)
