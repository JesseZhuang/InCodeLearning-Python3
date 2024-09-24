import unittest

from algorithm.dp.jump_game_ii import Solution


class TestJumpGame(unittest.TestCase):
    def setUp(self):
        self.tbt = Solution()

    def test_jump(self):
        self.assertEqual(2, self.tbt.jump([2, 3, 1, 1, 4]))

    def test_pos_over_0(self):
        """
        i:pos:val:reach
        actual 0:0:2:2->1:1:3:4->2:4:4:8
        p: 0:0:2:2->1:2:0:4->2:2:0:4->3:4:0:4
        """
        self.assertEqual(2, self.tbt.jump([2, 3, 0, 0, 4]))
