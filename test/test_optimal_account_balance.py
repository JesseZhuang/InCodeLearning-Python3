from unittest import TestCase

from algorithm.dp.optimal_account_balance import Solution1, Solution2


class TestOptimalAccountBal(TestCase):
    def test_balance_graph(self):
        tbt1, tbt2 = Solution1(), Solution2()
        cases = [
            [[0, 1, 10], [1, 2, 15], [2, 3, 10]],
            [[0, 1, 100], [0, 2, 100], [1, 2, 1], [1, 3, 100], [2, 3, 100]],
            [[0, 1, 10], [2, 0, 5]],
            [[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]
        ]
        exp = [
            2,
            2,
            2,
            1
        ]
        for case, e in zip(cases, exp):
            with self.subTest(case=case):
                self.assertEqual(e, tbt1.balance_graph(case))
                self.assertEqual(e, tbt2.minTransfers(case))
