'''leet code 329, hard'''


from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ''''''
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


Solution().longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]])
