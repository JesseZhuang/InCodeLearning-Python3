import unittest

from algorithm.jzstring.robot_bounded_in_circle import Solution


class TestRobotBoundedInCircle(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertTrue(self.sol.isRobotBounded("GGLLGG"))

    def test_example2(self):
        self.assertFalse(self.sol.isRobotBounded("GG"))

    def test_example3(self):
        self.assertTrue(self.sol.isRobotBounded("GL"))


if __name__ == '__main__':
    unittest.main()
