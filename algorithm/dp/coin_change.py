"""LeetCode 322 Coin Change"""

from collections import deque


class Solution:
    """Bottom-up DP. O(N*M) time, O(M) space. N: len(coins), M: amount."""

    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount  # dp[i]: min coins for amount i
        for coin in coins:  # O(N)
            for i in range(coin, amount + 1):  # O(M)
                if dp[i - coin] != float('inf'):
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


class Solution2:
    """BFS shortest path. O(N*M) time, O(M) space. N: len(coins), M: amount."""

    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        visited = [False] * (amount + 1)
        visited[amount] = True
        q = deque([amount])
        count = 0
        while q:
            for _ in range(len(q)):  # O(level size)
                cur = q.popleft()
                if cur == 0:
                    return count
                for coin in coins:  # O(N)
                    nxt = cur - coin
                    if 0 <= nxt and not visited[nxt]:
                        q.append(nxt)
                        visited[nxt] = True
            count += 1
        return -1
