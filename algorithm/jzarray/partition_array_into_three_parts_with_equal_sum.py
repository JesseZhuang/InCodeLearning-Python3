"""LeetCode 1013 Partition Array Into Three Parts With Equal Sum."""


class Solution:
    """Determine whether an array has three contiguous equal-sum parts."""

    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)
        if total % 3:
            return False

        target = total // 3
        current_sum = 0
        parts_found = 0
        # One pass: O(n) time and O(1) extra space.
        for value in arr:
            current_sum += value
            if current_sum == target:
                parts_found += 1
                current_sum = 0

        return parts_found >= 3
