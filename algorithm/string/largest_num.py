'''leet code 179 medium'''

from functools import cmp_to_key
from typing import List


class Solution:
    '''O(nLgn) time O(n) space'''

    def largestNumber1(self, nums: List[int]) -> str:
        s_nums = [str(n) for n in nums]

        def cmp(s1, s2): return -1 if s1+s2 > s2+s1 else \
            0 if s1+s2 == s2+s1 else \
            1
        s_nums.sort(key=cmp_to_key(cmp))
        if s_nums[0] == "0":
            return "0"
        return "".join(s_nums)

    def largestNumber2(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        def cmp(x, y): return (x+y < y+x) - (x+y > y+x)
        nums = sorted(nums, key=cmp_to_key(cmp))
        if nums[0] == "0":
            return "0"
        return "".join(nums)
