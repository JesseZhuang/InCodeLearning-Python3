import unittest

from algorithm.dp.max_profit_job import Solution, Solution2


class TestMaxProfitJob(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, start, end, profit, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.jobScheduling(start, end, profit))

    def test_example1(self):
        self.verify([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70], 120)

    def test_example2(self):
        self.verify([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60], 150)

    def test_example3(self):
        self.verify([1, 1, 1], [2, 3, 4], [5, 6, 4], 6)

    def test_single_job(self):
        self.verify([1], [2], [50], 50)

    def test_no_overlap(self):
        self.verify([1, 3, 5], [2, 4, 6], [10, 20, 30], 60)

    def test_all_overlap(self):
        self.verify([1, 1, 1], [10, 10, 10], [5, 6, 4], 6)

    def test_chain_end_equals_start(self):
        """job ending at time X allows job starting at X"""
        self.verify([1, 2, 3], [2, 3, 4], [10, 20, 30], 60)

    def test_best_skip_middle(self):
        self.verify([1, 2, 4], [3, 5, 6], [60, 10, 70], 130)

    def test_large_time_values(self):
        self.verify([1, 1000000000], [1000000000, 1000000001], [100, 200], 300)
