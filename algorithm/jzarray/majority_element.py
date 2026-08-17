from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """Boyer-Moore Voting Algorithm. O(n) time, O(1) space."""
        count = 0
        candidate = 0
        for num in nums:  # O(n)
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate

    def majorityElementSort(self, nums: List[int]) -> int:
        """Sorting approach. O(n log n) time, O(1) space (in-place sort)."""
        nums.sort()  # O(n log n)
        return nums[len(nums) // 2]
