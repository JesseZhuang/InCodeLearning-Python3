"""leet 3653, medium, tags: array, simulation."""

MOD = 10 ** 9 + 7


class Solution:
    """O(q*n) time, O(1) space. n: nums length, q: queries length."""

    def xorAfterRangeMultiplicationQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        for l, r, k, v in queries:
            for idx in range(l, r + 1, k):
                nums[idx] = nums[idx] * v % MOD
        res = 0
        for x in nums:
            res ^= x
        return res
