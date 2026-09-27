"""LeetCode 189 Rotate Array"""


class Solution:
    """Triple reverse. O(n) time, O(1) space."""

    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n  # O(1) normalize
        self._reverse(nums, 0, n - 1)      # O(n) reverse all
        self._reverse(nums, 0, k - 1)      # O(k) reverse first k
        self._reverse(nums, k, n - 1)      # O(n-k) reverse rest

    @staticmethod
    def _reverse(nums: list[int], lo: int, hi: int) -> None:
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1


class Solution2:
    """Extra array copy. O(n) time, O(n) space."""

    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n  # O(1) normalize
        tmp = nums[:]  # O(n) copy
        for i in range(n):  # O(n) place each element
            nums[(i + k) % n] = tmp[i]
