class Solution:
    def find_peak_element(self, nums: list[int]) -> int:
        """Binary search. O(log n) time, O(1) space."""
        lo, hi = 0, len(nums) - 1
        while lo < hi:  # O(log n)
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[mid + 1]:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def find_peak_element_linear(self, nums: list[int]) -> int:
        """Linear scan. O(n) time, O(1) space."""
        for i in range(len(nums) - 1):  # O(n)
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1
