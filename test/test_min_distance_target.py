import unittest

from algorithm.jzarray.min_distance_target import Solution


class TestMinDistanceTarget(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def verify(self, nums, target, start, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.getMinDistance(nums, target, start))

    def test_example1(self):
        self.verify([1, 2, 3, 4, 5], 5, 3, 1)

    def test_example2(self):
        self.verify([1], 1, 0, 0)

    def test_example3(self):
        self.verify([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 0, 0)

    def test_target_at_start(self):
        self.verify([5, 1, 2, 3, 4], 5, 0, 0)

    def test_target_at_end(self):
        self.verify([1, 2, 3, 4, 5], 5, 0, 4)

    def test_multiple_occurrences(self):
        self.verify([1, 2, 3, 2, 1], 2, 2, 1)

    def test_start_between_two_targets(self):
        self.verify([3, 1, 1, 1, 3], 3, 2, 2)

    def test_all_same(self):
        self.verify([7, 7, 7], 7, 1, 0)

    def test_single_match_far(self):
        self.verify([2, 1, 1, 1, 1, 1, 1], 2, 6, 6)
