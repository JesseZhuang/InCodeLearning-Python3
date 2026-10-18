import random
import unittest

from algorithm.dp.jump_game_vi import Solution, Solution2


class TestJumpGameVI(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def check_all(self, nums: list[int], k: int, expected: int):
        for solution in self.solutions:
            with self.subTest(solution=type(solution).__name__, nums=nums[:10], k=k):
                self.assertEqual(expected, solution.maxResult(nums, k))

    def test_examples(self):
        self.check_all([1, -1, -2, 4, -7, 3], 2, 7)
        self.check_all([10, -5, -2, 4, 0, 3], 3, 17)
        self.check_all([1, -5, -20, 4, -1, 3, -6, -3], 2, 0)

    def test_single_element(self):
        self.check_all([-10000], 1, -10000)

    def test_forced_adjacent_jumps(self):
        self.check_all([5, -7, 3, -2], 1, -1)

    def test_all_negative_and_expiring_best(self):
        self.check_all([-1, -2, -3, -4, -5], 2, -9)
        self.check_all([10, -100, -100, -100, -100, 1], 2, -189)

    def test_ties_and_large_window(self):
        self.check_all([0, 0, 0, 0, 0], 3, 0)
        self.check_all([1, -10000, -10000, 10], 4, 11)

    def test_random_small_against_quadratic_dp(self):
        generator = random.Random(1696)
        for length in range(2, 31):
            for _ in range(8):
                nums = [generator.randint(-10, 10) for _ in range(length)]
                k = generator.randint(1, length)
                scores = [nums[0]]
                for index in range(1, length):
                    scores.append(nums[index] + max(scores[max(0, index - k):index]))
                self.check_all(nums, k, scores[-1])

    def test_constraint_boundary(self):
        self.check_all([10000] * 100000, 100000, 1000000000)
