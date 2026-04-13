"""leet 1848, easy"""


class Solution:
    """Linear scan, O(n) time, O(1) space."""

    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        res = len(nums)  # upper bound
        for i, v in enumerate(nums):  # O(n)
            if v == target:
                res = min(res, abs(i - start))
        return res
