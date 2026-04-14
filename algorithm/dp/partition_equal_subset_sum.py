"""leet 416, medium, tags: array, dynamic programming."""


class Solution:
    """dp with boolean array, O(n*target) time, O(target) space."""

    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)  # O(target) space
        dp[0] = True
        for num in nums:  # O(n) outer loop
            for j in range(target, num - 1, -1):  # O(target) inner loop, iterate backward to avoid reuse
                dp[j] = dp[j] or dp[j - num]
        return dp[target]


class Solution2:
    """dp with bitset (integer), O(n*target) time, O(target) space."""

    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        bits = 1  # bit 0 is set, meaning sum 0 is reachable
        for num in nums:  # O(n) outer loop
            bits |= bits << num  # O(target) shift and or
        return bool(bits & (1 << target))
