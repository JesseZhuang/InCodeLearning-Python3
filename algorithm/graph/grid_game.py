"""leet 2017, medium"""


class Solution:
    """85 ms, 29.8 mb"""

    def gridGame(self, grid: list[list[int]]) -> int:
        first, second, res = sum(grid[0]), 0, float('inf')
        for i in range(len(grid[0])):
            first -= grid[0][i]
            res = min(res, max(first, second))
            second += grid[1][i]
        return res
