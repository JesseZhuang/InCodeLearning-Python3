"""
code signal: banking system
Requirements
Your task is to implement a simplified version of a banking system. Plan your design according to the level
specifications below:
• Level 1: The banking system should support creating new accounts and depositing money into and withdrawing/paying
 money from accounts.
• Level 2: The banking system should support ranking accounts based on the total value of transactions.
• Level 3: The banking system should support scheduling transfers and checking the scheduled transfer status.
• Level 4: The banking system should support merging two accounts while retaining the balances and transaction
histories of the original accounts.
To move to the next level, you should pass all the tests at the current level.
Note
You will receive a list of queries to the system, and the final output should be an array of strings representing
the returned values of all queries. Each query will only call one operation.
All queries will have a timestamp parameter — a string field timestamp in milliseconds. It is
guaranteed that all timestamps are unique and are in a range from 1 to 10^9.
Queries will be given in the order of strictly increasing timestamps.

Level 1:
1, CREATE_ACCOUNT<timestamp><accountId>, returns true if not present and create account, false otherwise
2, DEPOSIT <timestamp><accountId><amount>, deposit given amount of money to the specific account. returns a string
representing total money in the account (balance). If account does not exist, return empty string.
3, PAY <timestamp> <accountId> <amount>, withdraw from the account. returns a string representing account balance
after processing the query. If account does not exist or insufficient fund, return empty string.
Level 2:
The banking system should support ranking accounts based on total number of transactions.
1, TOP_ACTIVITY <timestamp> <n> return the top n accounts with the highest total value of transactions in descending
order. A string representing an array of accounts and transaction values in this format
"<accountId1>(<transactionValue1>)".
* Total value of transactions is defined as the sum of all transactions for an account (regardless of how the
 transaction affects account balance), including the amount of money deposited, withdrawn,
 and/or successfully transferred (transfers will be introduced on level 3, so you can ignore them for now).
* If less than n accounts exist in the system, return all active accounts (in the described format).
Level 3
The banking system should allow scheduling payments and checking the status of scheduled payments.
1, TRANSFER <timestamp> <sourceAccountId> ‹targetAccountId> <amount> - should initiate a transfer between accounts.
The given amount of money should be withdrawn from the source account sourceAccountId and held until the transfer
 is accepted by the target account targetAccountId, or until the transfer expires. The withheld money is added
 back to the source account's balance if the transfer expires. After the query is processed:
• Returns an empty string if sourceAccountId is equal to targetAccountId.
• Returns an empty string if sourceAccountId or targetAccountId doesn't exist.
• Returns an empty string if the source account sourceAccountId has insufficient funds to perform the transfer.
• The expiration period is 24 hours, which is equal to 24 • 60 • 60 • 1000 = 86400000 milliseconds.
A transfer expires at the beginning of the next millisecond after the expiration period ends.
• A valid TransFer should return a string containing a unique transfer ID in the following format
"transfer[ordinal number of the transfer]", e.g., "transfer1","transfer2", etc.
• For transfers, transaction history for source and target accounts is only updated when the transfer is accepted.
• Transfers count toward the total value of transactions of both source and target accounts.

2, ACCEPT_TRANSFER ‹timestamp> <accountId> <transferId> - Should accept the transfer with the given transferId.
• Returns "true" if the transfer was successfully accepted or "false" otherwise.
• Returns "false" if a transfer with transferId does not exist, was already accepted, or has expired.
• Returns "false" if the given accountId was not the target account for the transfer.

Level 3 （Variant)
The system should allow scheduling payments and checking the status of scheduled payments.
• Optional<String> schedulePaymentint timestamp, String accountId, int amount, int delay) - should schedule a payment
 which will be performed at timestamp + delay . Returns a string with a unique identifier for the scheduled payment
 in the following format: "payment [ordinal number of the scheduled payment across all accounts] - e.g., "paymenti",
 "payment2", etc. If accountId doesn't exist, should return Optional. empty. The payment is skipped if the specified
  account has insufficient funds when the payment is performed. Additional conditions:
• Successful payments should be considered outgoing transactions and included when ranking accounts using the
 operation.
• Scheduled payments should be processed before any other transactions at the given timestamp.
• If an account needs to perform several scheduled payments simultaneously, they should be processed in order of
 creation - e.g., "payment1" should be processed before "payment2"
• boolean cancelPayment(int timestamp, String accountId, String paymentId) - should cancel the scheduled payment
with paymentId. Returns true if the scheduled payment is successfully canceled. If paymentId does not exist or
was already canceled, or if accountId is different from the source account for the scheduled payment, returns false.
 Note that scheduled payments must be performed before any cancelPayment operations at the given timestamp.

Variants:
- Level 3: schedule payment, cancel payment
- support payment, user get cashback after 24 hours of spending
- level 4: merge two accounts, need to merge accounts in the transfer system too. The banking system should support
 merging two accounts while retaining both accounts' balance and transaction histories.
- get balance, need to support timestamp, get the history balance of the specified account at a given timeAt
"""
from typing import Dict, Type, Self

from sortedcontainers import SortedList

MILLISECONDS_IN_1_DAY = 86400000
FALSE = "false"
TRUE = "true"


class Account:

    def __init__(self, ts: int, acct_id: str):
        self.ts = ts
        self.acct_id = acct_id
        self.balance: int = 0
        self.tr_v: int = 0
        self.log: SortedList[BalLog] = SortedList(key=lambda x: x.ts)
        self.log.add(BalLog(ts, self, 0, "create", 0))

    def pay(self, ts: int, amount: int):
        if self.balance < amount:
            return ""
        self.balance -= amount
        self.tr_v += amount
        self.log.add(BalLog(ts, self, amount, "pay", self.balance))
        return f"{self.balance}"

    def deposit(self, ts: int, amount: int):
        self.balance += amount
        self.tr_v += amount
        self.log.add(BalLog(ts, self, amount, "deposit", self.balance))
        return f"{self.balance}"

    def merge(self, ts: int, acct: Type[Self]):
        self.balance += acct.balance
        self.tr_v += acct.tr_v
        self.log.update(acct.log)
        self.log.add(BalLog(ts, self, acct.balance, "merge", self.balance))
        return TRUE

    def balance(self, ts: int) -> int:
        """get balance in any timestamp"""
        id = self.log.bisect_right(BalLog(ts, self, 0, "balance", self.balance)) - 1
        if id < 0: return -1  # before the account was created
        return self.log[id].balance


class Transfer:
    def __init__(self, ts: int, src: Account, target: Account, amount: int):
        self.ts = ts
        self.src = src
        self.target = target
        self.amount = amount


class BalLog:
    def __init__(self, ts: int, acct: Account, amount: int, typ: str, bal: int):
        self.ts = ts
        self.acct = acct
        self.amount = amount  # + for deposit, - for pay
        self.typ = typ
        self.bal = bal


class Bank:
    def __init__(self):
        self.accts: Dict[str, Account] = dict()  # id->acct
        self.c_accts: Dict[str, Account] = dict()  # closed accts
        self.xfer_id: int = 1
        self.p_xfers: Dict[int, Transfer] = dict()  # pending xfers xfer_id:xfer
        self.c_xfers: Dict[int, Transfer] = dict()  # completed

    def create_acct(self, ts: str, acct_id: str) -> str:
        if acct_id in self.accts: return FALSE
        self.accts[acct_id] = Account(int(ts), acct_id)
        return TRUE

    def deposit(self, ts: str, acct_id: str, amount: str) -> str:
        if acct_id not in self.accts: return ""
        return f"{self.accts[acct_id].deposit(int(ts), int(amount))}"

    def pay(self, ts: str, acct_id: str, amount: str) -> str:
        if acct_id not in self.accts: return ""
        return f"{self.accts[acct_id].pay(int(ts), int(amount))}"

    def top(self, ts: str, n: str) -> str:
        accts = list(self.accts.values())
        accts.sort(key=lambda x: x.tr_v, reverse=True)
        return ", ".join([f"{a.acct_id}({a.tr_v})" for a in accts[:int(n)]])

    def xfer(self, ts: str, src_acct_id: str, target_acct_id: str, amount: str) -> str:
        if src_acct_id == target_acct_id or src_acct_id not in self.accts: return ""
        src = self.accts[src_acct_id]
        xfer = Transfer(int(ts), self.accts[src_acct_id],
                        self.accts[target_acct_id], int(amount))
        if src.balance < xfer.amount: return ""
        xfer_id_str = f"transfer{self.xfer_id}"
        self.p_xfers[self.xfer_id] = xfer
        self.xfer_id += 1
        return xfer_id_str

    def ac_xfer(self, ts: str, acct_id: str, xfer_id: str) -> str:
        xfer_id = int(xfer_id[len("transfer"):])
        ts = int(ts)
        if xfer_id not in self.p_xfers: return FALSE
        xfer = self.p_xfers[xfer_id]
        if xfer.target.acct_id != acct_id: return FALSE
        if ts - xfer.ts > MILLISECONDS_IN_1_DAY:
            del self.p_xfers[xfer_id]
            return FALSE
        xfer.src.pay(ts, xfer.amount)
        xfer.target.deposit(ts, xfer.amount)
        self.c_xfers[xfer_id] = xfer
        del self.p_xfers[xfer_id]
        return TRUE

    def merge(self, ts: str, src_acct_id: str, target_acct_id: str) -> str:
        if src_acct_id not in self.accts or target_acct_id not in self.accts:
            return FALSE
        src, target = self.accts[src_acct_id], self.accts[target_acct_id]
        del self.accts[src_acct_id]
        self.c_accts[src_acct_id] = src
        for xfer_id, xfer in self.p_xfers.copy().items():
            if xfer.src.acct_id == src_acct_id:
                if xfer.target.acct_id == target_acct_id:  # target is the account to merge into
                    del self.p_xfers[xfer_id]  # no longer need to transfer or add to completed transfers
                else:
                    self.c_xfers[xfer_id].src = target  # transfer need to start from the new merged account
        return src.merge(int(ts), target)  # -1 or total balance


def solution(queries):
    bank = Bank()
    res = []
    for q in queries:
        match (q[0]):
            case "CREATE_ACCOUNT":
                res.append(bank.create_acct(q[1], q[2]))
            case "DEPOSIT":
                res.append(bank.deposit(q[1], q[2], q[3]))
            case "PAY":
                res.append(bank.pay(q[1], q[2], q[3]))
            case "TOP_ACTIVITY":
                res.append(bank.top(q[1], q[2]))
            case "TRANSFER":
                res.append(bank.xfer(q[1], q[2], q[3], q[4]))
            case "ACCEPT_TRANSFER":
                res.append(bank.ac_xfer(q[1], q[2], q[3]))
            case _:
                res.append("unsupported")
    return res
