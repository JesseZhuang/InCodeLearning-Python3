import unittest

from algorithm.jzarray.two_subtract import two_subtract


class TestTwoSubtract(unittest.TestCase):

    def test_two_subtract(self):
        cases = [
            ([1, 2], 3, 0),  # no index pairs
            ([1, 2], 1, 1),  # [[0,1]]
            ([1, 2, 0], 1, 2),  # [[0,1],[0,2]]
            ([1, 2, 1, 2, 0], 1, 6)  # [[0,1],[0,3],[1,2],[2,3],[0,4],[2,4]]
        ]
        for nums, target, exp in cases:
            with self.subTest(nums=nums, target=target, exp=exp):
                self.assertEqual(exp, two_subtract(nums, target))
