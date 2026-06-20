"""leet code 329, hard"""

from collections import deque
from functools import lru_cache
from typing import List


class SolutionDFS:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """DFS + memoization. Time O(m*n), Space O(m*n)."""
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(matrix), len(matrix[0])

        @lru_cache(maxsize=None)  # memoize: each cell computed once, O(m*n) total
        def dfs(r, c):
            steps = 1
            for d in dirs:  # O(4) directions
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nr >= m or nc < 0 or nc >= n or matrix[nr][nc] <= matrix[r][c]:
                    continue
                steps = max(steps, 1 + dfs(nr, nc))
            return steps

        res = 1
        for r in range(m):  # O(m)
            for c in range(n):  # O(n)
                res = max(res, dfs(r, c))
        return res


class SolutionBFS:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """Topological sort BFS. Time O(m*n), Space O(m*n)."""
        m, n = len(matrix), len(matrix[0])
        indegree = [[0] * n for _ in range(m)]
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for r in range(m):  # O(m*n) build indegree
            for c in range(n):
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] < matrix[r][c]:
                        indegree[r][c] += 1
        q = deque()
        for r in range(m):
            for c in range(n):
                if indegree[r][c] == 0:  # local minima as BFS sources
                    q.append([r, c])
        res = 0
        while len(q) > 0:  # each level = one step in longest path
            s = len(q)
            for i in range(s):
                r, c = q.popleft()
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                        indegree[nr][nc] -= 1
                        if indegree[nr][nc] == 0:
                            q.append([nr, nc])
            res += 1
        return res
