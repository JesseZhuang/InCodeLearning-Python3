"""LeetCode 983 Minimum Cost For Tickets"""


class Solution:
    """DP on calendar days. O(last_day) time, O(last_day) space."""

    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        travel = set(days)
        last_day = days[-1]
        dp = [0] * (last_day + 1)  # dp[d]: min cost to cover days 1..d
        for d in range(1, last_day + 1):  # O(last_day)
            if d not in travel:
                dp[d] = dp[d - 1]
            else:
                dp[d] = min(
                    dp[d - 1] + costs[0],                  # 1-day pass
                    dp[max(0, d - 7)] + costs[1],          # 7-day pass
                    dp[max(0, d - 30)] + costs[2],         # 30-day pass
                )
        return dp[last_day]


class Solution2:
    """DP on travel day indices with recursion + memo. O(n) time, O(n) space."""

    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        n = len(days)
        durations = [1, 7, 30]
        memo = {}

        def dp(i: int) -> int:
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            res = float('inf')
            j = i
            for cost, dur in zip(costs, durations):  # O(3)
                while j < n and days[j] < days[i] + dur:  # advance pointer
                    j += 1
                res = min(res, cost + dp(j))
            memo[i] = res
            return res

        return dp(0)
