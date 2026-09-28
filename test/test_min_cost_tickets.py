"""test LeetCode 983 Minimum Cost For Tickets"""
import unittest

from algorithm.dp.min_cost_tickets import Solution, Solution2


class TestMinCostTickets(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(11, sol.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(17, sol.mincostTickets(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))

    def test_single_day(self):
        for sol in self.solutions:
            self.assertEqual(2, sol.mincostTickets([1], [2, 7, 15]))

    def test_seven_day_pass_cheaper(self):
        """7 consecutive days: 7-day pass (7) beats 7 x 1-day (14)."""
        for sol in self.solutions:
            self.assertEqual(7, sol.mincostTickets(
                [1, 2, 3, 4, 5, 6, 7], [2, 7, 15]))

    def test_thirty_day_pass_cheaper(self):
        """Many days in a month: 30-day pass wins."""
        days = list(range(1, 31))
        for sol in self.solutions:
            self.assertEqual(15, sol.mincostTickets(days, [2, 7, 15]))

    def test_sparse_days(self):
        """Sparse travel: individual 1-day passes are cheapest."""
        for sol in self.solutions:
            self.assertEqual(6, sol.mincostTickets([1, 100, 200], [2, 7, 15]))

    def test_one_day_pass_always_cheapest(self):
        """When 1-day cost is very low."""
        for sol in self.solutions:
            self.assertEqual(5, sol.mincostTickets(
                [1, 2, 3, 4, 5], [1, 10, 100]))

    def test_all_same_cost(self):
        """All pass types cost the same; one 30-day pass suffices."""
        for sol in self.solutions:
            self.assertEqual(5, sol.mincostTickets(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 5, 5]))

    def test_last_day_365(self):
        """Maximum constraint: last day = 365."""
        for sol in self.solutions:
            self.assertEqual(10, sol.mincostTickets([1, 365], [5, 50, 200]))


if __name__ == '__main__':
    unittest.main()
