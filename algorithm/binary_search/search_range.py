class Solution:
    def search_range(self, nums: list[int], target: int) -> list[int]:
        """Two binary searches for left and right boundaries. O(log n) time, O(1) space."""
        left = self._lower_bound(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = self._upper_bound(nums, target)
        return [left, right]

    def _lower_bound(self, nums: list[int], target: int) -> int:
        """Find first index where nums[i] >= target. O(log n)"""
        lo, hi = 0, len(nums)
        while lo < hi:  # O(log n)
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def _upper_bound(self, nums: list[int], target: int) -> int:
        """Find last index where nums[i] == target. O(log n)"""
        lo, hi = 0, len(nums) - 1
        while lo < hi:  # O(log n)
            mid = lo + (hi - lo + 1) // 2
            if nums[mid] <= target:
                lo = mid
            else:
                hi = mid - 1
        return lo

    def search_range_builtin(self, nums: list[int], target: int) -> list[int]:
        """Using bisect_left and bisect_right. O(log n) time, O(1) space."""
        from bisect import bisect_left, bisect_right
        left = bisect_left(nums, target)  # O(log n)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = bisect_right(nums, target) - 1  # O(log n)
        return [left, right]
