import unittest

from algorithm.dp.jump_game import Solution


class TestJumpGame(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_can_jump(self):
        for s in self.solutions:
            self.assertTrue(s.canJump([2, 3, 1, 1, 4]))

    def test_cannot_jump(self):
        for s in self.solutions:
            self.assertFalse(s.canJump([3, 2, 1, 0, 4]))

    def test_single_element(self):
        for s in self.solutions:
            self.assertTrue(s.canJump([0]))

    def test_two_elements_reachable(self):
        for s in self.solutions:
            self.assertTrue(s.canJump([1, 0]))

    def test_two_elements_unreachable(self):
        for s in self.solutions:
            self.assertFalse(s.canJump([0, 1]))

    def test_all_zeros(self):
        for s in self.solutions:
            self.assertFalse(s.canJump([0, 0, 0]))

    def test_large_first_jump(self):
        for s in self.solutions:
            self.assertTrue(s.canJump([10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))

    def test_just_barely_reachable(self):
        for s in self.solutions:
            self.assertTrue(s.canJump([1, 1, 1, 1, 1]))

    def test_stuck_at_zero(self):
        for s in self.solutions:
            self.assertFalse(s.canJump([1, 0, 0, 1]))


if __name__ == '__main__':
    unittest.main()
