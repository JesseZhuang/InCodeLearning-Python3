"""leet 934, medium, tags: array, dfs, bfs, matrix."""

from collections import deque


class Solution:
    """DFS to find island + multi-source BFS to expand. O(n^2) time, O(n^2) space."""

    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()

        def dfs(r, c):
            grid[r][c] = 2  # mark as visited
            queue.append((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    dfs(nr, nc)

        # find first island via DFS
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        # BFS expand from first island until reaching second island
        steps = 0
        while queue:
            for _ in range(len(queue)):  # O(n^2) total across all levels
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            return steps
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            queue.append((nr, nc))
            steps += 1
        return -1


class Solution2:
    """Two-pass BFS from both islands, meet in the middle. O(n^2) time, O(n^2) space."""

    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        islands = [[], []]
        visited = [[False] * n for _ in range(n)]

        def bfs_collect(sr, sc, idx):
            q = deque([(sr, sc)])
            visited[sr][sc] = True
            while q:
                r, c = q.popleft()
                islands[idx].append((r, c))
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 1:
                        visited[nr][nc] = True
                        q.append((nr, nc))

        # collect both islands
        idx = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    bfs_collect(i, j, idx)
                    idx += 1

        # BFS expand from island 0
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        island1_set = set(islands[1])
        for r, c in islands[0]:
            dist[r][c] = 0
            q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    if (nr, nc) in island1_set:  # O(1) lookup
                        return dist[nr][nc] - 1
                    q.append((nr, nc))
        return -1
