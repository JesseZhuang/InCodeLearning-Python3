"""LeetCode 85, hard, tags: array, dynamic programming, stack, matrix, monotonic stack."""


class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        """Build histogram row by row and apply largest rectangle in histogram.

        For each row, heights[j] = number of consecutive '1's above (including current row).
        Then apply monotonic stack to find largest rectangle.
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0
        for i in range(m):  # O(m)
            for j in range(n):  # O(n)
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            max_area = max(max_area, self._largest_rect(heights))
        return max_area  # Time O(m*n), Space O(n)

    def _largest_rect(self, heights: list[int]) -> int:
        n = len(heights)
        stack = []  # monotonic increasing stack of indices
        max_area = 0
        for i in range(n + 1):  # O(n), each index pushed/popped once
            h = 0 if i == n else heights[i]
            while stack and h < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, cur_height * width)
            stack.append(i)
        return max_area


class Solution2:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        """DP approach tracking height, left boundary, and right boundary per cell."""
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        height = [0] * n
        left = [0] * n
        right = [n] * n
        max_area = 0
        for i in range(m):  # O(m)
            cur_left, cur_right = 0, n
            for j in range(n):  # O(n) update height and left
                if matrix[i][j] == '1':
                    height[j] += 1
                    left[j] = max(left[j], cur_left)
                else:
                    height[j] = 0
                    left[j] = 0
                    cur_left = j + 1
            for j in range(n - 1, -1, -1):  # O(n) update right
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            for j in range(n):  # O(n)
                max_area = max(max_area, height[j] * (right[j] - left[j]))
        return max_area  # Time O(m*n), Space O(n)
