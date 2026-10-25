"""LeetCode 1034: Coloring A Border."""

from collections import deque


class Solution:
    def colorBorder(self, grid: list[list[int]], row: int, col: int, color: int) -> list[list[int]]:
        """BFS, O(m*n) time and O(m*n) auxiliary space."""
        original = grid[row][col]
        if original == color:
            return grid

        rows, cols = len(grid), len(grid[0])
        seen = [[False] * cols for _ in range(rows)]
        seen[row][col] = True
        queue = deque([(row, col)])
        border = []

        while queue:  # O(m*n): each cell in the component is visited once.
            current_row, current_col = queue.popleft()
            is_border = False
            for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row, next_col = current_row + delta_row, current_col + delta_col
                if not (0 <= next_row < rows and 0 <= next_col < cols):
                    is_border = True
                elif grid[next_row][next_col] != original:
                    is_border = True
                elif not seen[next_row][next_col]:
                    seen[next_row][next_col] = True
                    queue.append((next_row, next_col))
            if is_border:
                border.append((current_row, current_col))

        for border_row, border_col in border:  # O(m*n) worst case; colors change only after BFS.
            grid[border_row][border_col] = color
        return grid
