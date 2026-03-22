import unittest

from algorithm.graph.max_candies_boxes import Solution


class TestMaxCandiesBoxes(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def verify(self, status, candies, keys, contained, initial, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.maxCandies(status, candies, keys, contained, initial))

    def test_example1(self):
        self.verify(
            [1, 0, 1, 0], [7, 5, 4, 100],
            [[], [], [1], []], [[1, 2], [3], [], []], [0],
            16
        )

    def test_example2(self):
        self.verify(
            [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1],
            [[1, 2, 3, 4, 5], [], [], [], [], []],
            [[1, 2, 3, 4, 5], [], [], [], [], []], [0],
            6
        )

    def test_no_initial_boxes(self):
        self.verify([1, 1], [10, 20], [[], []], [[], []], [], 0)

    def test_single_open_box(self):
        self.verify([1], [42], [[]], [[]], [0], 42)

    def test_single_closed_no_key(self):
        self.verify([0], [42], [[]], [[]], [0], 0)

    def test_chain_unlock(self):
        """box0 open -> key to box1 -> key to box2"""
        self.verify(
            [1, 0, 0], [1, 2, 3],
            [[1], [2], []], [[1], [2], []], [0],
            6
        )

    def test_key_before_box(self):
        """get key to box1 from box0, but box1 is received from box2"""
        self.verify(
            [1, 0, 1], [10, 100, 1],
            [[1], [], []], [[], [], [1]], [0, 2],
            111
        )

    def test_unreachable_box(self):
        """box2 has candy but is never obtained"""
        self.verify(
            [1, 0, 0], [5, 10, 100],
            [[], [], []], [[1], [], []], [0],
            5
        )

    def test_duplicate_keys(self):
        """key to box2 appears in both box0 and box1"""
        self.verify(
            [1, 1, 0], [1, 2, 3],
            [[2], [2], []], [[1], [2], []], [0],
            6
        )

    def test_all_closed_with_circular_keys(self):
        """box0 has key to box1, box1 has key to box0, both closed initially"""
        self.verify(
            [0, 0], [10, 20],
            [[1], [0]], [[], []], [0, 1],
            0
        )
