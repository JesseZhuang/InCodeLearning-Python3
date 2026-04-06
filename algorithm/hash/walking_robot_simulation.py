"""leet 874, medium, tags: array, hash table, simulation."""


class Solution:
    """O(n*k+m) time, O(m) space. n: commands length, k: max steps (9), m: obstacles length."""

    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        dx = [0, 1, 0, -1]  # N, E, S, W
        dy = [1, 0, -1, 0]
        obs = set(map(tuple, obstacles))
        x = y = d = 0  # d: 0=N, 1=E, 2=S, 3=W
        res = 0
        for c in commands:
            if c == -2:
                d = (d + 3) % 4  # turn left
            elif c == -1:
                d = (d + 1) % 4  # turn right
            else:
                for _ in range(c):
                    nx, ny = x + dx[d], y + dy[d]
                    if (nx, ny) in obs:
                        break
                    x, y = nx, ny
                res = max(res, x * x + y * y)
        return res
