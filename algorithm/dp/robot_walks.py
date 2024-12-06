"""
related to project euler 208, hacker rank robot walks
ChatGPT, gemini all failed
"""
from math import cos, sin, pi

RADIUS = 1


def equal_epsilon(a, b) -> bool:
    return abs(a - b) < 1e-6


class State:
    def __init__(self):
        """arc center at origin (0,0), staring point (1,0), counterclockwise rotation"""
        self.center = (0, 0)
        self.angle = 0
        self.d = 1  # direction: 1 counterclockwise, -1 clockwise

    def get_point(self):
        """ending point"""
        (x, y), a = self.center, self.angle
        return x + RADIUS * cos(a), y + RADIUS * sin(a)

    def mirror(self):
        """mirror center and update angle"""
        x1, y1 = self.get_point()
        x0, y0 = self.center
        self.center = (2 * x1 - x0, 2 * y1 - y0)  # mirror
        self.angle += pi
        if self.angle > 2 * pi: self.angle -= 2 * pi
        if self.angle < -2 * pi: self.angle += 2 * pi
        self.d = -self.d

    def rotate(self, angle: float, d: int):
        if d != self.d: self.mirror()
        self.angle += angle * self.d
        if self.angle > 2 * pi: self.angle -= 2 * pi
        if self.angle < -2 * pi: self.angle += 2 * pi


class RobotWalks:
    def __init__(self, n: int, m: int, K: int):
        self.n = n
        self.angle = 2 * pi / self.n
        self.m = m
        self.K = K

    def journeys(self) -> int:
        # start at (1,0)

        def helper(steps, s: State) -> int:
            res = 0
            if steps == 0:
                x, y = s.get_point()  # check whether returned to starting point (1,0)
                return 1 if equal_epsilon(x, RADIUS) and equal_epsilon(y, 0) else 0
            # sc = copy(s)
            # try counterclockwise arc
            s.rotate(self.angle, 1)
            res += helper(steps - 1, s)
            s.rotate(-self.angle, 1)  # backtrack
            if steps == self.m: return res * 2
            # try clockwise arc
            s.rotate(self.angle, -1)
            res += helper(steps - 1, s)
            s.rotate(-self.angle, -1)
            return res

        return helper(self.m, State()) % self.K
