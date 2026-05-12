"""LeetCode 48 Rotate Image"""


class Solution:
    """Transpose then reflect. O(n^2) time, O(1) space."""

    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for i in range(n):  # O(n^2) transpose
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):  # O(n^2) reflect left-right
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]


class Solution2:
    """Rotate four cells at a time, layer by layer. O(n^2) time, O(1) space."""

    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):  # O(n/2) layers
            for j in range(i, n - i - 1):  # O(n) elements per layer
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = tmp
