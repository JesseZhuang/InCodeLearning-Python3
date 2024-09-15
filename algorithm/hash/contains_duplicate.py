"""leet code 217, easy"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen: return True
            seen.add(n)
        return False
