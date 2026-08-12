"""LeetCode 221 Maximal Square"""


class Solution:
    """DP. O(m*n) time, O(n) space."""

    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n + 1)  # O(n) space
        max_side = 0
        for i in range(m):  # O(m)
            new_dp = [0] * (n + 1)
            for j in range(n):  # O(n)
                if matrix[i][j] == '1':
                    new_dp[j + 1] = min(dp[j], dp[j + 1], new_dp[j]) + 1
                    max_side = max(max_side, new_dp[j + 1])
            dp = new_dp
        return max_side * max_side
