"""leet 33, medium, tags: array, binary search."""


class Solution:
    """Modified binary search, single pass. O(log n) time, O(1) space."""

    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:  # O(log n) iterations
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:  # left half [l..m] is sorted
                if nums[l] <= target < nums[m]:  # target in sorted left half
                    r = m - 1
                else:
                    l = m + 1
            else:  # right half [m..r] is sorted
                if nums[m] < target <= nums[r]:  # target in sorted right half
                    l = m + 1
                else:
                    r = m - 1
        return -1


class Solution2:
    """Two-pass: find pivot then binary search. O(log n) time, O(1) space."""

    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # pass 1: find index of minimum element (pivot), O(log n)
        l, r = 0, n - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l
        # pass 2: binary search in the correct half, O(log n)
        if target >= nums[pivot] and target <= nums[-1]:
            l, r = pivot, n - 1
        else:
            l, r = 0, pivot - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1
