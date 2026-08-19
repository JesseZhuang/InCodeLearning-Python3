import unittest

from algorithm.dp.jump_game_ii import Solution, Solution2


class TestJumpGameII(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for s in self.solutions:
            self.assertEqual(2, s.jump([2, 3, 1, 1, 4]))

    def test_example2(self):
        for s in self.solutions:
            self.assertEqual(2, s.jump([2, 3, 0, 1, 4]))

    def test_single_element(self):
        for s in self.solutions:
            self.assertEqual(0, s.jump([0]))

    def test_two_elements(self):
        for s in self.solutions:
            self.assertEqual(1, s.jump([1, 2]))

    def test_already_at_end(self):
        for s in self.solutions:
            self.assertEqual(1, s.jump([3, 2, 1]))

    def test_all_ones(self):
        for s in self.solutions:
            self.assertEqual(4, s.jump([1, 1, 1, 1, 1]))

    def test_large_first_jump(self):
        for s in self.solutions:
            self.assertEqual(1, s.jump([10, 0, 0, 0, 0]))

    def test_zeros_in_middle(self):
        for s in self.solutions:
            self.assertEqual(2, s.jump([2, 3, 0, 0, 4]))

    def test_large_jump_covers_all(self):
        nums = [10000] + [0] * 9999
        for s in self.solutions:
            self.assertEqual(1, s.jump(nums))

    def test_greedy_choice(self):
        for s in self.solutions:
            self.assertEqual(3, s.jump([1, 2, 1, 1, 1]))
