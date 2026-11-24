import unittest

from algorithm.graph.jump_game_iii import Solution, Solution2


class TestJumpGameIII(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def assert_all_solutions(self, arr, start, expected):
        for solution in self.solutions:
            with self.subTest(solution=solution.__class__.__name__, arr=arr, start=start):
                self.assertEqual(solution.canReach(arr[:], start), expected)

    def test_example_one_reaches_zero(self):
        self.assert_all_solutions([4, 2, 3, 0, 3, 1, 2], 5, True)

    def test_example_two_reaches_zero(self):
        self.assert_all_solutions([4, 2, 3, 0, 3, 1, 2], 0, True)

    def test_zero_exists_but_is_unreachable(self):
        self.assert_all_solutions([3, 0, 2, 1, 2], 2, False)

    def test_single_zero_at_start(self):
        self.assert_all_solutions([0], 0, True)

    def test_reaches_zero_by_jumping_right(self):
        self.assert_all_solutions([2, 1, 0], 0, True)

    def test_reaches_zero_by_jumping_left(self):
        self.assert_all_solutions([1, 0, 2], 2, True)

    def test_cycle_without_zero_terminates(self):
        self.assert_all_solutions([1, 1], 0, False)

    def test_both_jumps_can_be_out_of_bounds(self):
        self.assert_all_solutions([2, 2, 2], 1, False)


if __name__ == '__main__':
    unittest.main()
