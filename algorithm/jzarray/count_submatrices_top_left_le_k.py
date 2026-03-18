"""leetcode 3070, medium"""
from typing import List


class Solution:
    """123 ms, 55.70 mb"""
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        res, col_sum = 0, [0] * n
        for i in range(m):
            cur = 0
            for j in range(n):
                col_sum[j] += grid[i][j]
                cur += col_sum[j]
                if cur <= k:
                    res += 1
                else:
                    break
        return res
