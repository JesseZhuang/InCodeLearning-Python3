"""LeetCode 1574 Shortest Subarray to be Removed to Make Array Sorted"""


class Solution:
    """Two pointers. O(n) time, O(1) space."""

    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        r = len(arr) - 1
        while r > 0 and arr[r] >= arr[r - 1]:
            r -= 1
        res, l = r, 0  # can remove arr[0:r]
        while l < r and (l == 0 or arr[l - 1] <= arr[l]):
            # find r such that removing [l+1, r-1] makes array sorted
            while r < len(arr) and arr[l] > arr[r]:
                r += 1
            res = min(res, r - l - 1)
            l += 1
        return res
