from typing import List


class Solution:
    """LeetCode 54, medium, tags: array, matrix, simulation."""

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """Direction-based simulation. O(m*n) time, O(1) space."""
        m, n = len(matrix), len(matrix[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        limits = [n, m - 1]  # O(1) space for bounds tracking
        res = []
        d, r, c = 0, 0, -1
        while limits[d % 2] > 0:  # O(m*n) total iterations
            for _ in range(limits[d % 2]):
                r += dirs[d][0]
                c += dirs[d][1]
                res.append(matrix[r][c])
            limits[d % 2] -= 1
            d = (d + 1) % 4
        return res


class Solution2:
    """Layer-by-layer peeling approach."""

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """Peel layers from outside in. O(m*n) time, O(1) space."""
        res = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:  # O(min(m,n)/2) layers
            for c in range(left, right + 1):  # O(n) per layer top
                res.append(matrix[top][c])
            for r in range(top + 1, bottom + 1):  # O(m) per layer right
                res.append(matrix[r][right])
            if top < bottom:
                for c in range(right - 1, left - 1, -1):  # O(n) per layer bottom
                    res.append(matrix[bottom][c])
            if left < right:
                for r in range(bottom - 1, top, -1):  # O(m) per layer left
                    res.append(matrix[r][left])
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return res
