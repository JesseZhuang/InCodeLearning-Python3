from unittest import TestCase

from algorithm.math.possible_events import Solution


class TestSolution(TestCase):

    def setUp(self) -> None:
        self.tbt = Solution()

    def test_number_of_ways(self):
        cases = [
            [6, [1, 2, 3]],
            [32, [5, 2, 1]],
            [684, [3, 3, 4]]
        ]
        for exp, [n, x, y] in cases:
            with self.subTest(n=n, x=x, y=y):
                self.assertEqual(exp, self.tbt.numberOfWays(n, x, y))
