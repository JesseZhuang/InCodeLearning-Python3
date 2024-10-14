import unittest

from algorithm.ood.banking_system import solution, MILLISECONDS_IN_1_DAY


class TestBankingSystem(unittest.TestCase):

    def test_level1(self):
        queries = [
            ["CREATE_ACCOUNT", "1", "account1"],
            ["CREATE_ACCOUNT", "2", "account1"],
            ["CREATE_ACCOUNT", "3", "account2"],
            ["DEPOSIT", "4", "non-existing", "2700"],
            ["DEPOSIT", "5", "account1", "2700"],
            ["PAY", "6", "non-existing", "2700"],
            ["PAY", "7", "account1", "2701"],
            ["PAY", "8", "account1", "200"]
        ]
        expected = [
            "true",
            "false",
            "true",
            "",
            "2700",
            "",
            "",
            "2500"
        ]
        self.assertEqual(expected, solution(queries))

    def test_level2(self):
        queries = [
            ["CREATE_ACCOUNT", "1", "account1"],
            ["CREATE_ACCOUNT", "2", "account2"],
            ["CREATE_ACCOUNT", "3", "account3"],
            ["DEPOSIT", "4", "account1", "2000"],
            ["DEPOSIT", "5", "account2", "3000"],
            ["DEPOSIT", "6", "account3", "4000"],
            ["TOP_ACTIVITY", "7", "3"],
            ["PAY", "8", "account1", "1500"],
            ["PAY", "9", "account2", "250"],
            ["DEPOSIT", "10", "account3", "250"],
            ["TOP_ACTIVITY", "11", "3"]]
        expected = [
            "true",
            "true",
            "true",
            "2000",
            "3000",
            "4000",
            "account3(4000), account2(3000), account1(2000)",
            "500",
            "2750",
            "4250",
            "account3(4250), account1(3500), account2(3250)"
        ]
        self.assertEqual(expected, solution(queries))

    def test_level3(self):
        queries = [
            ["CREATE_ACCOUNT", "1", "account1"],
            ["CREATE_ACCOUNT", "2", "account2"],
            ["DEPOSIT", "3", "account1", "2000"],
            ["DEPOSIT", "4", "account2", "3000"],
            ["TRANSFER", "5", "account1", "account2", "5000"],
            ["TRANSFER", "16", "account1", "account2", "1000"],
            ["ACCEPT_TRANSFER", "20", "account1", "transfer1"],
            ["ACCEPT_TRANSFER", "21", "non-existing", "transfer1"],
            ["ACCEPT_TRANSFER", "22", "account1", "transfer2"],
            ["ACCEPT_TRANSFER", "25", "account2", "transfer1"],
            ["ACCEPT_TRANSFER", "30", "account2", "transfer1"],
            ["TRANSFER", "40", "account1", "account2", "1000"],
            ["ACCEPT_TRANSFER", str(45 + MILLISECONDS_IN_1_DAY), "account2", "transfer2"],
            ["TRANSFER", str(50 + MILLISECONDS_IN_1_DAY), "account1", "account1", "1000"]
        ]
        exp = [
            "true",
            "true",
            "2000",
            "3000",
            "",
            "transfer1",
            "false",
            "false",
            "false",
            "true",
            "false",
            "transfer2",
            "false",
            ""
        ]
        self.assertEqual(exp, solution(queries))
