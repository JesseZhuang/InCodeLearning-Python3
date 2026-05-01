"""LeetCode 2257 Count Unguarded Cells in the Grid"""


class Solution:
    """Simulation. O(mn + g(m+n)) time, O(mn) space."""

    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        GUARD, WALL, GUARDED = 2, 3, 1
        for r, c in guards:
            grid[r][c] = GUARD
        for r, c in walls:
            grid[r][c] = WALL
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for gr, gc in guards:
            for dr, dc in dirs:
                nr, nc = gr + dr, gc + dc
                while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != GUARD and grid[nr][nc] != WALL:
                    grid[nr][nc] = GUARDED
                    nr += dr
                    nc += dc
        return sum(1 for r in range(m) for c in range(n) if grid[r][c] == 0)
