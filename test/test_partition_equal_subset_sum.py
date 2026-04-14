import unittest

from algorithm.dp.partition_equal_subset_sum import Solution, Solution2


class TestPartitionEqualSubsetSum(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_can_partition(self):
        cases = [
            ([1, 5, 11, 5], True),
            ([1, 2, 3, 5], False),
            ([1, 1], True),
            ([1, 2, 5], False),
            ([2, 2, 1, 1], True),
            ([1], False),
            ([100], False),
            ([1, 2, 3, 4, 5, 6, 7], True),
            ([14, 9, 8, 4, 3, 2], True),
            ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], True),
        ]
        for sol in self.solutions:
            for nums, expected in cases:
                with self.subTest(sol=sol.__class__.__name__, nums=nums, expected=expected):
                    self.assertEqual(sol.canPartition(nums), expected)
