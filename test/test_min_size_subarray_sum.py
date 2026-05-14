from unittest import TestCase

from algorithm.sliding.min_size_subarray_sum import Solution, Solution2


class TestSolution(TestCase):
    def test_min_sub_array_len(self):
        cases = [
            (7, [2, 3, 1, 2, 4, 3], 2),
            (4, [1, 4, 4], 1),
            (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
            (11, [1, 2, 3, 4, 5], 3),
            (15, [1, 2, 3, 4, 5], 5),
            (3, [1, 1], 0),
            (5, [5], 1),
            (100, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 10),
            (20, [2, 3, 1, 2, 4, 3], 0),
            (6, [10, 2, 3], 1),
        ]
        tbt, tbt2 = Solution(), Solution2()
        for target, nums, exp in cases:
            with self.subTest(target=target, nums=nums, exp=exp):
                self.assertEqual(tbt.minSubArrayLen(target, nums), exp)
                self.assertEqual(tbt2.minSubArrayLen(target, nums), exp)
