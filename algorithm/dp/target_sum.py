"""leet 494, medium, tags: array, dynamic programming, backtracking."""


class Solution:
    """Subset sum DP. O(n*s) time, O(s) space. n: len(nums), s: sum(nums)."""

    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total = sum(nums)
        if (total + target) % 2 != 0 or abs(target) > total:
            return 0
        p = (total + target) // 2  # sum of elements assigned '+'
        dp = [0] * (p + 1)  # dp[j]: ways to reach sum j
        dp[0] = 1
        for num in nums:  # O(n)
            for j in range(p, num - 1, -1):  # O(s), reverse to avoid reuse
                dp[j] += dp[j - num]
        return dp[p]


class Solution2:
    """DFS + memoization. O(n*s) time, O(n*s) space."""

    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        from functools import cache

        @cache
        def dfs(i: int, cur: int) -> int:  # O(n*s) states
            if i == len(nums):
                return 1 if cur == target else 0
            return dfs(i + 1, cur + nums[i]) + dfs(i + 1, cur - nums[i])

        return dfs(0, 0)
