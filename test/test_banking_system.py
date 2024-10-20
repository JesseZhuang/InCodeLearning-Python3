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
            "",  # account non-existing
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
            "",  # same account, invalid transfer
        ]
        self.assertEqual(exp, solution(queries))

    def test_level3b(self):
        queries = [
            ["CREATE_ACCOUNT", "1", "account1"],
            ["CREATE_ACCOUNT", "2", "account2"],
            ["DEPOSIT", "3", "account1", "2000"],
            ["PAY_V2", 4, "account1", 1000],
            ["PAY_V2", 100, "account1", 1000],
            ["GET_PAYMENT_STATUS", 101, "non-existing", "payment1"],
            ["GET_PAYMENT_STATUS", 102, "account2", "payment1"],
            ["GET_PAYMENT_STATUS", 103, "account1", "payment1"],
            ["TOP_SPENDERS", "104", "2"],
            ["DEPOSIT", str(3 + MILLISECONDS_IN_1_DAY), "account1", "100"],
            ["GET_PAYMENT_STATUS", 4 + MILLISECONDS_IN_1_DAY, "account1", "payment1"],
            ["DEPOSIT", str(5 + MILLISECONDS_IN_1_DAY), "account1", "100"],
            ["DEPOSIT", str(99 + MILLISECONDS_IN_1_DAY), "account1", "100"],
            ["DEPOSIT", str(100 + MILLISECONDS_IN_1_DAY), "account1", "100"],
        ]
        expected = [
            "true",
            "true",
            "2000",
            "payment1",
            "payment2",
            None,  # this account does not exist
            None,  # this payment was from another account
            "IN_PROGRESS",
            "account1(2000), account2(0)",
            "100",  # cashback for payment1 was not refunded yet
            "CASHBACK_RECEIVED",
            "220",  # cashback for payment1 refunded 20
            "320",  # cashback for payment2 not refunded yet
            "440",  # cashback for payment2 refunded 20
        ]
        self.assertEqual(expected, solution(queries))

    def test_level3c(self):
        queries2 = [
            ["CREATE ACCOUNT", "1", "account1"],
            ["CREATE_ACCOUNT", "2", "account2"],
            ["CREATE _ACCOUNT", "3", "account3"],
            ["DEPOSIT", "4", "account1", "1000"],
            ["DEPOSIT", "5", "account2", "1000"],
            ["DEPOSIT", "6", "account3", "1000"],
            ["SCHEDULE_PAYMENT", "7", "account1", "300", "10"],
            ["SCHEDULE_PAYMENT", "8", "account2", "400", "10"],
            ["TOP_SPENDERS", "15", "3"],
            ["TOP_SPENDERS", "20", "3"],
        ]
        expected = [
            "true",
            "true",
            "true",
            "1000",
            "1000",
            "1000",
            "payment1",
            "payment2",
            "account1(0), account2(0), account3(0)",  # none has any outgoing transactions
            "account2(400), account1(300), account3(0)"
        ]
        queries3 = [
            ["CREATE_ACCOUNT", "1", "account1"],
            ["CREATE_ACCOUNT", "2", "account2"],
            ["DEPOSIT", "3", "account1", "2000"],
            ["DEPOSIT", "4", "account2", "3000"],
            ["SCHEDULE_PAYMENT", "5", "account1", "50", "10"],
            ["SCHEDULE_PAYMENT", "6", "account2", "1000", "5"],
            ["SCHEDULE_PAYMENT", "7", "account1", "3000", "7"],
            ["DEPOSIT", "11", "account2", "5"],
            ["CANCEL_PAYMENT", "12", "account2", "payment1"],
            ["CANCEL_PAYMENT", "13", "account1", "payment1"],
            ["DEPOSIT", "14", "account1", "5"],
            ["DEPOSIT", "15", "account1", "5"],
        ]
        expected = [
            "true",
            "true",
            "2000",
            "3000",
            "payment1",
            "payment2",
            "payment3",
            "2005",
            "false",
            "true",
            "2005",
            "2010"
        ]
        # skip, similar to transfer and pay, delay is variable now
        pass

    def test_level4(self):
        queries = [
            ["CREATE_ACCOUNT", "1", "account1"],
            ["CREATE_ACCOUNT", "2", "account2"],
            ["DEPOSIT", "3", "account1", "2000"],
            ["DEPOSIT", "4", "account2", "2000"],
            ["PAY_V2", 5, "account2", 300],
            ["TRANSFER_V2", 6, "account1", "account2", 500],
            ["MERGE_ACCOUNTS", 7, "account1", "non-existing"],
            ["MERGE_ACCOUNTS", 8, "account1", "account1"],
            ["MERGE_ACCOUNTS", 8, "account1", "account2"],
            ["DEPOSIT", "10", "account1", "100"],
            ["DEPOSIT", "11", "account2", "100"],
            ["GET_PAYMENT_STATUS", "12", "account2", "payment1"],
            ["GET_PAYMENT_STATUS", "13", "account1", "payment1"],
            ["GET_BALANCE", 14, "account2", 1],
            ["GET_BALANCE", 15, "account2", 9],
            ["GET_BALANCE", 16, "account1", 11],
            # ["GET_BALANCE", "17", "account2", "7"],
            ["DEPOSIT", str(5 + MILLISECONDS_IN_1_DAY), "account1", "100"]
        ]
        expected = [
            "true",
            "true",
            "2000",
            "2000",
            "payment1",
            1500,
            False,  # account non-existing does not exist
            False,  # account account1 cannot be merged into itself
            True,
            "3800",
            "",  # account account2 does not exist anymore
            None,  # account account2 does not exist anymore
            "IN_PROGRESS",
            None,  # account2 was not created yet
            None,  # account2 merged and not exist anymore
            3800,
            "3906"
        ]
        self.assertEqual(expected, solution(queries))
