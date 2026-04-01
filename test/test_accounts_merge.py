import unittest

from algorithm.graph.accounts_merge import Solution, Solution2


class TestAccountsMerge(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, accounts, expected):
        expected_sorted = sorted([e[0:1] + sorted(e[1:]) for e in expected])
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.accountsMerge(accounts)
                result_sorted = sorted([r[0:1] + sorted(r[1:]) for r in result])
                self.assertEqual(expected_sorted, result_sorted)

    def test_example1(self):
        self.verify(
            [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
             ["John", "johnsmith@mail.com", "john00@mail.com"],
             ["Mary", "mary@mail.com"],
             ["John", "johnnybravo@mail.com"]],
            [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
             ["Mary", "mary@mail.com"],
             ["John", "johnnybravo@mail.com"]]
        )

    def test_example2(self):
        self.verify(
            [["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
             ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
             ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
             ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
             ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]],
            [["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
             ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
             ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
             ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
             ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"]]
        )

    def test_single_account(self):
        self.verify(
            [["Alice", "a@m.co"]],
            [["Alice", "a@m.co"]]
        )

    def test_all_merge(self):
        """Three accounts all connected via shared emails."""
        self.verify(
            [["Bob", "b1@m.co", "b2@m.co"],
             ["Bob", "b2@m.co", "b3@m.co"],
             ["Bob", "b3@m.co", "b4@m.co"]],
            [["Bob", "b1@m.co", "b2@m.co", "b3@m.co", "b4@m.co"]]
        )

    def test_same_name_no_merge(self):
        """Same name but no shared emails — should not merge."""
        self.verify(
            [["Tom", "t1@m.co"], ["Tom", "t2@m.co"]],
            [["Tom", "t1@m.co"], ["Tom", "t2@m.co"]]
        )

    def test_chain_merge(self):
        """Accounts form a chain: 1-2 share email, 2-3 share email."""
        self.verify(
            [["Ann", "a@m.co", "b@m.co"],
             ["Ann", "b@m.co", "c@m.co"],
             ["Ann", "c@m.co", "d@m.co"]],
            [["Ann", "a@m.co", "b@m.co", "c@m.co", "d@m.co"]]
        )

    def test_multiple_emails_single_account(self):
        self.verify(
            [["Zoe", "z1@m.co", "z2@m.co", "z3@m.co", "z4@m.co"]],
            [["Zoe", "z1@m.co", "z2@m.co", "z3@m.co", "z4@m.co"]]
        )

    def test_duplicate_emails_in_account(self):
        self.verify(
            [["Dan", "d@m.co", "d@m.co"]],
            [["Dan", "d@m.co"]]
        )
