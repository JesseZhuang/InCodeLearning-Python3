"""leet code 1041, medium"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        i, x, y, dirs = 0, 0, 0, [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for c in instructions:
            match c:
                case 'G':
                    x, y = x + dirs[i][0], y + dirs[i][1]
                case 'L':
                    i = (i + 3) % 4
                case 'R':
                    i = (i + 1) % 4
        return x == 0 and y == 0 or i > 0
