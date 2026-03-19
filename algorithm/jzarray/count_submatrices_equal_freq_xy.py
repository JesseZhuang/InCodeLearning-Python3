"""leetcode 3212, medium"""
from typing import List


class Solution:
    # 351ms, 103.60mb
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        col_x, col_y = [0] * n, [0] * n
        for i in range(m):
            row_x = row_y = 0
            for j in range(n):
                col_x[j] += (grid[i][j] == 'X')
                col_y[j] += (grid[i][j] == 'Y')
                row_x += col_x[j]
                row_y += col_y[j]
                if row_x == row_y and row_x > 0:
                    res += 1
        return res
