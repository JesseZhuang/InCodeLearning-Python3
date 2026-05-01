"""LeetCode 1041, medium, tags: math, string, simulation."""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """O(n) time, O(1) space."""
        x, y, d = 0, 0, 0  # 0:N, 1:E, 2:S, 3:W
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for c in instructions:
            if c == 'G':
                x += dirs[d][0]
                y += dirs[d][1]
            elif c == 'R':
                d = (d + 1) % 4
            else:
                d = (d + 3) % 4
        return (x == 0 and y == 0) or d > 0
