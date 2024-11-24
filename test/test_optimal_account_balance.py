from unittest import TestCase

from algorithm.dp.optimal_account_balance import Solution1, Solution2


class TestOptimalAccountBal(TestCase):
    def test_balance_graph(self):
        tbt1, tbt2 = Solution1(), Solution2()
        cases = [
            [[0, 1, 10], [1, 2, 15], [2, 3, 10]],
            [[0, 1, 100], [0, 2, 100], [1, 2, 1], [1, 3, 100], [2, 3, 100]],
            [[0, 1, 10], [2, 0, 5]],
            [[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]],
            [[9, 8, 1], [6, 8, 59], [5, 4, 28], [5, 4, 43], [0, 2, 54], [4, 3, 17], [9, 8, 72], [0, 1, 68], [4, 3, 4],
             [2, 0, 74], [7, 9, 54], [5, 4, 58], [1, 2, 42], [4, 5, 91], [0, 1, 41], [6, 8, 6], [7, 8, 51], [0, 2, 30],
             [6, 8, 57], [8, 6, 32]]
        ]
        exp = [
            2,
            2,
            2,
            1,
            7
        ]
        for case, e in zip(cases, exp):
            with self.subTest(case=case):
                self.assertEqual(e, tbt1.balance_graph(case))
                self.assertEqual(e, tbt2.minTransfers(case))
