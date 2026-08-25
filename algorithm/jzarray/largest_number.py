"""179. Largest Number https://leetcode.com/problems/largest-number/"""

from functools import cmp_to_key
from typing import List


class Solution:
    """Custom comparator sort.

    For two numbers a, b, compare str(a)+str(b) vs str(b)+str(a).
    """

    def largestNumber(self, nums: List[int]) -> str:
        strs = [str(n) for n in nums]  # O(n) space

        def cmp(a: str, b: str) -> int:  # O(k) per comparison, k = avg digit length
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            return 0

        strs.sort(key=cmp_to_key(cmp))  # O(n log n * k) time
        result = "".join(strs)
        return "0" if result[0] == "0" else result
