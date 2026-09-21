'''leet code 377, medium, tags: array, dynamic programming.'''


from typing import List


class Solution:
    # O(N*target) time, O(target) space. Bottom-up DP.
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):  # O(target)
            for num in nums:  # O(N)
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[target]


class Solution2:
    # O(N*target) time, O(target) space. Top-down memoization.
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {0: 1}

        def dfs(remain):
            if remain in memo:
                return memo[remain]
            res = 0
            for num in nums:  # O(N)
                if remain >= num:
                    res += dfs(remain - num)
            memo[remain] = res
            return res

        return dfs(target)
