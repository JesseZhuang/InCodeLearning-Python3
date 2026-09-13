"""leet code 167, medium, tags: array, two pointers, binary search."""
from bisect import bisect_left
from typing import List


class Solution:
    """Two pointers. O(n) time, O(1) space. 108ms, 17.8mb"""

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:  # O(n)
            v = numbers[l] + numbers[r]
            if v == target:
                return [l + 1, r + 1]
            elif v < target:
                l += 1
            else:
                r -= 1


class Solution2:
    """Binary search for each element. O(n log n) time, O(1) space."""

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):  # O(n)
            complement = target - numbers[i]
            j = bisect_left(numbers, complement, i + 1)  # O(log n)
            if j < len(numbers) and numbers[j] == complement:
                return [i + 1, j + 1]
