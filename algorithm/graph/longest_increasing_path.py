"""leet code 329, hard"""

from collections import deque
from typing import List


class Solution:

    def longestIncreasingPath1(self, matrix: List[List[int]]) -> int:
        '''374ms, 19.8Mb'''

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(matrix), len(matrix[0])
        cache = [[0] * n for _ in range(m)]  # [[0]*n]* m bug, same list copied m times

        def dfs(r, c):
            if cache[r][c] != 0:  # can use @cache (since py3.9)
                return cache[r][c]
            steps = 1
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nr >= m or nc < 0 or nc >= n or matrix[nr][nc] <= matrix[r][c]:
                    continue
                steps = max(steps, 1 + dfs(nr, nc))
            cache[r][c] = steps
            return steps

        res = 1
        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r, c))
        return res

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''399ms, 17.04Mb'''
        m, n = len(matrix), len(matrix[0])
        indegree = [[0] * n for _ in range(m)]
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for r in range(m):
            for c in range(n):
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] < matrix[r][c]:
                        indegree[r][c] += 1
        q = deque()
        for r in range(m):
            for c in range(n):
                if indegree[r][c] == 0:
                    q.append([r, c])
        res = 0
        while len(q) > 0:
            s = len(q)
            for i in range(s):
                r, c = q.popleft()
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                        indegree[nr][nc] -= 1  # bug indegree[r][c] -= 1
                        if indegree[r][c] == 0:
                            q.append([r, c])
            res += 1
        return res


Solution().longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]])
