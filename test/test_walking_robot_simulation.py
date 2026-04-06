import unittest

from algorithm.hash.walking_robot_simulation import Solution


class TestWalkingRobotSimulation(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for s in self.solutions:
            self.assertEqual(25, s.robotSim([4, -1, 3], []))

    def test_example2(self):
        for s in self.solutions:
            self.assertEqual(65, s.robotSim([4, -1, 4, -2, 4], [[2, 4]]))

    def test_example3(self):
        for s in self.solutions:
            self.assertEqual(36, s.robotSim([6, -1, -1, 6], [[0, 0]]))

    def test_no_movement(self):
        """Only turn commands, no forward movement."""
        for s in self.solutions:
            self.assertEqual(0, s.robotSim([-2, -1, -2, -1], []))

    def test_single_step(self):
        for s in self.solutions:
            self.assertEqual(1, s.robotSim([1], []))

    def test_blocked_immediately(self):
        """Obstacle at (0,1), robot can't move north."""
        for s in self.solutions:
            self.assertEqual(0, s.robotSim([4], [[0, 1]]))

    def test_all_directions(self):
        """Move in all four directions."""
        for s in self.solutions:
            # N4 -> (0,4), R, E3 -> (3,4), R, S2 -> (3,2), R, W1 -> (2,2)
            self.assertEqual(25, s.robotSim([4, -1, 3, -1, 2, -1, 1], []))

    def test_negative_coordinates(self):
        """Robot moves into negative coordinates."""
        for s in self.solutions:
            # turn left (west), move 3 -> (-3, 0), sq dist = 9
            self.assertEqual(9, s.robotSim([-2, 3], []))

    def test_multiple_obstacles(self):
        for s in self.solutions:
            # N9 blocked at (0,3) -> (0,2), R, E9 blocked at (3,2) -> (2,2)
            self.assertEqual(8, s.robotSim([9, -1, 9], [[0, 3], [3, 2]]))


if __name__ == '__main__':
    unittest.main()
