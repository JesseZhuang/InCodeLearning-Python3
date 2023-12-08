'''leet code 329, hard'''


from collections import deque
from typing import List


class Solution:
    def longestIncreasingPath1(self, matrix: List[List[int]]) -> int:
        '''374ms, 19.8Mb'''
        def dfs(matrix, r, c, m, n, cache):
            if cache[r][c] != 0:
                return cache[r][c]
            res = 1
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for d in dirs:
                nr, nc = r+d[0], c+d[1]
                if nr < 0 or nr >= m or nc < 0 or nc >= n or matrix[nr][nc] <= matrix[r][c]:
                    continue
                len = 1+dfs(matrix, nr, nc, m, n, cache)
                res = max(res, len)
            cache[r][c] = res
            return res

        m, n = len(matrix), len(matrix[0])
        cache = [[0]*n for _ in range(m)]  # [[0]*n]* m bug, same list copied m times
        res = 1
        for r in range(m):
            for c in range(n):
                res = max(res, dfs(matrix, r, c, m, n, cache))
        return res

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''399ms, 17.04Mb'''
        m, n = len(matrix), len(matrix[0])
        indegree = [[0]*n for _ in range(m)]
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for r in range(m):
            for c in range(n):
                for d in dirs:
                    nr, nc = r+d[0], c+d[1]
                    if nr >= 0 and nr < m and nc >= 0 and nc < n and matrix[nr][nc] < matrix[r][c]:
                        indegree[r][c] += 1
        q = deque()
        for r in range(m):
            for c in range(n):
                if indegree[r][c] == 0:
                    q.append([r, c])
        res = 0
        while (len(q) > 0):
            s = len(q)
            for i in range(s):
                rc = q.popleft()
                r, c = rc[0], rc[1]
                for d in dirs:
                    nr, nc = r+d[0], c+d[1]
                    if nr >= 0 and nr < m and nc >= 0 and nc < n and matrix[nr][nc] > matrix[r][c]:
                        indegree[nr][nc] -= 1  # bug indegree[r][c] -= 1
                        if indegree[r][c] == 0:
                            q.append([r, c])
            res += 1
        return res


Solution().longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]])
