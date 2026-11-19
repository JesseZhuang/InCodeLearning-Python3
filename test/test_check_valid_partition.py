import unittest
from itertools import product

from algorithm.dp.check_valid_partition import Solution


class TestCheckValidPartition(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_examples(self):
        for solution in self.solutions:
            self.assertTrue(solution.validPartition([4, 4, 4, 5, 6]))
            self.assertFalse(solution.validPartition([1, 1, 1, 2]))

    def test_group_rules_and_boundaries(self):
        cases = [
            ([1, 1], True),
            ([1, 2], False),
            ([7, 7, 7], True),
            ([1, 2, 3], True),
            ([1, 2, 4], False),
            ([1, 3, 4], False),
            ([3, 2, 1], False),
            ([1, 1, 2], False),
            ([1, 2, 2], False),
            ([1, 1, 1, 1], True),
            ([1, 1, 1, 2, 3], True),
            ([1, 1, 2, 2, 3, 3], True),
            ([1, 2, 3, 4], False),
            ([1, 2, 3, 4, 5, 6], True),
            ([999998, 999999, 1000000], True),
            ([1000000, 1000000], True),
        ]
        for solution in self.solutions:
            for nums, expected in cases:
                with self.subTest(nums=nums):
                    original = nums.copy()
                    self.assertEqual(solution.validPartition(nums), expected)
                    self.assertEqual(nums, original)

    def test_maximum_length(self):
        for solution in self.solutions:
            self.assertTrue(solution.validPartition([1000000] * 100000))
            self.assertFalse(solution.validPartition([1] * 99999 + [2]))

    def test_exhaustive_small_arrays(self):
        def can_split(nums, start=0):
            # Independent oracle: try each possible next block recursively.
            if start == len(nums):
                return True
            for size in (2, 3):
                block = nums[start:start + size]
                if len(block) != size:
                    continue
                equal = len(set(block)) == 1
                consecutive = size == 3 and list(block) == list(range(block[0], block[0] + 3))
                if (equal or consecutive) and can_split(nums, start + size):
                    return True
            return False

        for size in range(2, 9):
            for values in product((1, 2, 3), repeat=size):
                expected = can_split(values)
                for solution in self.solutions:
                    self.assertEqual(solution.validPartition(list(values)), expected, values)
