"""leet 2290, hard"""


class Solution:
    """todo editorial, 0,1 bfs, mn, mn"""
    # Directions for movement: right, left, down, up
    _directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def minimumObstacles(self, grid):
        # Helper method to check if the cell is within the grid bounds
        def _is_valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        m, n = len(grid), len(grid[0])

        # Distance matrix to store the minimum obstacles removed to reach each cell
        min_obstacles = [[float("inf")] * n for _ in range(m)]
        min_obstacles[0][0] = 0

        deque_cells = deque([(0, 0, 0)])  # (obstacles, row, col)

        while deque_cells:
            obstacles, row, col = deque_cells.popleft()

            # Explore all four possible directions from the current cell
            for dr, dc in self._directions:
                new_row, new_col = row + dr, col + dc

                if _is_valid(new_row, new_col) and min_obstacles[new_row][
                    new_col
                ] == float("inf"):
                    if grid[new_row][new_col] == 1:
                        # If it's an obstacle, add 1 to obstacles and push to the back
                        min_obstacles[new_row][new_col] = obstacles + 1
                        deque_cells.append((obstacles + 1, new_row, new_col))
                    else:
                        # If it's an empty cell, keep the obstacle count and push to the front
                        min_obstacles[new_row][new_col] = obstacles
                        deque_cells.appendleft((obstacles, new_row, new_col))

        return min_obstacles[m - 1][n - 1]
