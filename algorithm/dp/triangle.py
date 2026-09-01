"""LeetCode 120 Triangle"""


class Solution:
    """Bottom-up DP in-place. O(n^2) time, O(1) extra space. n: number of rows."""

    def minimumTotal(self, triangle: list[list[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):  # O(n) rows bottom to top
            for j in range(len(triangle[i])):  # O(i) columns
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]


class Solution2:
    """Bottom-up DP with auxiliary array. O(n^2) time, O(n) space. n: number of rows."""

    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = triangle[-1][:]  # O(n) space, copy last row
        for i in range(len(triangle) - 2, -1, -1):  # O(n) rows bottom to top
            for j in range(len(triangle[i])):  # O(i) columns
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]
