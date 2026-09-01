"""LeetCode 64 Minimum Path Sum"""


class Solution:
    """In-place DP. O(m*n) time, O(1) extra space (modifies input)."""

    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(1, n):  # O(n) first row prefix sum
            grid[0][i] += grid[0][i - 1]
        for i in range(1, m):  # O(m) rows
            grid[i][0] += grid[i - 1][0]
            for j in range(1, n):  # O(n) cols
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[m - 1][n - 1]


class Solution2:
    """1D DP without modifying input. O(m*n) time, O(n) space."""

    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        for j in range(1, n):  # O(n) first row
            dp[j] = dp[j - 1] + grid[0][j]
        for i in range(1, m):  # O(m) rows
            dp[0] += grid[i][0]
            for j in range(1, n):  # O(n) cols
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[n - 1]
