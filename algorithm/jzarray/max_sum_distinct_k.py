"""LeetCode 2461 Maximum Sum of Distinct Subarrays With Length K"""


class Solution:
    """Sliding window with last-seen map. O(n) time, O(n) space."""

    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        res, cur, dup = 0, 0, -1
        last: dict[int, int] = {}  # val -> last seen index
        for i, v in enumerate(nums):
            cur += v
            if i >= k:
                cur -= nums[i - k]
            dup = max(dup, last.get(v, -1))
            if i - dup >= k:
                res = max(res, cur)
            last[v] = i
        return res
