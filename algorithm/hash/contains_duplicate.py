"""leet code 217, easy"""
from typing import List


class Solution1:
    """431ms, 31.96mb"""

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


class Solution2:
    """403ms, 31.9mb"""

    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen: return True
            seen.add(n)
        return False
