import time
from copy import copy
from math import pi
from unittest import TestCase

from algorithm.dp.robot_walks import RobotWalks, State, equal_epsilon


class TestRobotWalks(TestCase):
    def setUp(self):
        self.tbt_s = State()
        self.tbt_r = RobotWalks(1, 2, 3)

    def test_state(self):
        self.assertEqual((1, 0), self.tbt_s.get_point())
        self.tbt_s.angle += pi / 6
        x, y = self.tbt_s.get_point()
        self.assertTrue(equal_epsilon(x, 0.8660254))  # cos(pi/6)
        self.assertTrue(equal_epsilon(y, 0.5))  # sin(pi/6)

    def test_state_copy(self):
        """shallow copy of state is enough"""
        sc = copy(self.tbt_s)
        sc.center = (1, 0)  # tuple immutable, assign a new tuple
        self.assertEqual((1, 0), sc.center)
        self.assertEqual((0, 0), self.tbt_s.center)

    def test_state_mirror(self):
        self.tbt_s.mirror()
        # (0,0) mirror (1,0) to (2,0)
        self.assertTrue(equal_epsilon(self.tbt_s.center[0], 2))
        self.assertTrue(equal_epsilon(self.tbt_s.center[1], 0))
        self.assertEqual(self.tbt_s.angle, pi)
        # mirror does not change the end point of the arc
        x, y = self.tbt_s.get_point()
        self.assertTrue(equal_epsilon(x, 1))
        self.assertTrue(equal_epsilon(y, 0))

    def test_walks(self):
        cases = [
            # (5, 25, 1000000007, 70932),
            (2, 2, 31, 2),
            (2, 1, 31, 0),
            (2, 3, 31, 0),
            (2, 4, 31, 6),
            (3, 6, 1000000007, 8),
            (6, 7, 1000000009, 2),
            (4, 8, 1000000033, 18),
        ]
        for n, m, K, exp in cases:
            tbt = RobotWalks(n, m, K)
            start = time.time()
            self.assertEqual(exp, tbt.journeys())
            print(time.time() - start)
