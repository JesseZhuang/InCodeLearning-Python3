"""leet 1368, hard"""
from collections import deque


class Solution:
    """todo editorial"""
    # Direction vectors: right, left, down, up (matching grid values 1,2,3,4)
    _dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def minCost(self, grid: list[list[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        cost = 0

        # Track minimum cost to reach each cell
        min_cost = [[float("inf")] * num_cols for _ in range(num_rows)]

        # Queue for BFS part - stores cells that need cost increment
        queue = deque()

        # Start DFS from origin with cost 0
        self._dfs(grid, 0, 0, min_cost, cost, queue)

        # BFS part - process cells level by level with increasing cost
        while queue:
            cost += 1
            level_size = len(queue)

            for _ in range(level_size):
                row, col = queue.popleft()

                # Try all 4 directions for next level
                for dir_idx, (dx, dy) in enumerate(self._dirs):
                    self._dfs(grid, row + dx, col + dy, min_cost, cost, queue)

        return min_cost[num_rows - 1][num_cols - 1]

    # DFS to explore all reachable cells with current cost
    def _dfs(
            self,
            grid: list[list[int]],
            row: int,
            col: int,
            min_cost: list[list[int]],
            cost: int,
            queue: deque,
    ) -> None:
        if not self._is_unvisited(min_cost, row, col):
            return

        min_cost[row][col] = cost
        queue.append((row, col))

        # Follow the arrow direction without cost increase
        next_dir = grid[row][col] - 1
        dx, dy = self._dirs[next_dir]
        self._dfs(grid, row + dx, col + dy, min_cost, cost, queue)

    # Check if cell is within bounds and unvisited
    def _is_unvisited(
            self, min_cost: list[list[int]], row: int, col: int
    ) -> bool:
        return (
                0 <= row < len(min_cost)
                and 0 <= col < len(min_cost[0])
                and min_cost[row][col] == float("inf")
        )
