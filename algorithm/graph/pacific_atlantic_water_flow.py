from collections import deque


class Solution:
    """LeetCode 417, medium, tags: array, dfs, bfs, matrix."""

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """DFS from ocean borders. O(m*n) time, O(m*n) space."""
        if not heights:
            return []
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prev_height):
            if (r, c) in visited or r < 0 or r >= m or c < 0 or c >= n:
                return
            if heights[r][c] < prev_height:
                return
            visited.add((r, c))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(r + dr, c + dc, visited, heights[r][c])

        for i in range(m):  # O(m)
            dfs(i, 0, pacific, 0)  # left edge -> pacific
            dfs(i, n - 1, atlantic, 0)  # right edge -> atlantic
        for j in range(n):  # O(n)
            dfs(0, j, pacific, 0)  # top edge -> pacific
            dfs(m - 1, j, atlantic, 0)  # bottom edge -> atlantic

        return [[r, c] for r, c in pacific & atlantic]


class Solution2:
    """BFS approach for LeetCode 417."""

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """BFS from ocean borders. O(m*n) time, O(m*n) space."""
        if not heights:
            return []
        m, n = len(heights), len(heights[0])

        def bfs(starts):
            visited = set(starts)
            q = deque(starts)
            while q:  # O(m*n) total
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        if heights[nr][nc] >= heights[r][c]:  # can flow uphill
                            visited.add((nr, nc))
                            q.append((nr, nc))
            return visited

        pacific_starts = (
            [(i, 0) for i in range(m)] + [(0, j) for j in range(n)]
        )
        atlantic_starts = (
            [(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(n)]
        )
        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)
        return [[r, c] for r, c in pacific & atlantic]
