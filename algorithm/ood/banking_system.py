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

Level 3  (Variant Java)
The system should allow scheduling payments and checking the status of scheduled payments.
• Optional<String> schedulePayment(int timestamp, String accountId, int amount, int delay) - should schedule a payment
 which will be performed at timestamp + delay . Returns a string with a unique identifier for the scheduled payment
 in the following format: "payment [ordinal number of the scheduled payment across all accounts] - e.g., "payment i",
 "payment2", etc. If accountId doesn't exist, should return Optional.empty. The payment is skipped if the specified
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

Level 3 (Variant-Python)
pay (self, timestamp: int, account_id: str, amount: int) -> str | None
- Should withdraw the given amount of money from the specified account. All withdraw transactions provide a 2% cashback
 - 2% of the withdrawn amount (rounded down to the nearest integer) will be refunded to the account 24 hours after
  the withdrawal. If the withdrawal is successful (i.e., the account holds sufficient funds to withdraw
   the given amount), returns a string with a unique identifier for the payment transaction in this format:
    "payment(ordinal number of withdraws from all accounts]" -e.g., "payment1", "payment2", etc.
Additional conditions:
• Returns None if account_id doesn't exist.
• Returns None if account_id has insufficient funds to perform the payment.
• top_spenders should now also account for the total amount of money withdrawn from accounts.
• The waiting period for cashback is 24 hours, equal to 24 * 60 * 60 * 1000 = 86400000 milliseconds
  (the unit for timestamps). So, cashback will be processed at timestamp, timestamp + 86400000 .
• When it's time to process cashback for a withdrawal, the amount must be refunded to the account before any other
  transactions are performed at the relevant timestamp.

get_payment_status (self, timestamp: int, account_id: str, payment: str) -> str | None -
Should return the status of the payment transaction for the given payment.
Specifically:
• Returns None if account_id doesn't exist.
• Returns None if the given payment doesn't exist for the specified account.
• Returns None if the payment transaction was for an account with a different identifier from account_id
• Returns a string representing the payment status: "IN_PROGRESS" or "CASHBACK_RECEIVED".

The system should allow scheduling payments and checking the status of scheduled payments.
• SCHEDULE_PAYMENT < timestamp> < accountId> ‹amount > ‹delay> - should schedule a payment which will be performed
at timestamp + delay. Returns a string with a unique identifier for the scheduled payment in the following format:
"payment [ordinal number of the scheduled payment across all accounts]" - e.g.,
"payment1", "payment2", etc. If account id doesn't exist, should return an empty string. The payment is skipped if the
specified account has insufficient funds when the payment is performed.
Additional conditions:
• Successful payments should be considered outgoing transactions and included when ranking accounts using the
TOP_SPENDERS operation.
• Scheduled payments should be processed before any other transactions at the given timestamp.
• If an account needs to perform several scheduled payments simultaneously, they should be processed in order
 of creation - e.g., "payment1" should be processed before "payment2"

CANCEL_PAYMENT < timestamp> <accountId> <paymentId> - should cancel the scheduled payment with paymentId.
Returns "true" if the scheduled payment is successfully canceled. If payment id does not exist or was already canceled,
 or if account id is different from the source account for the scheduled payment, returns
"false" . Note that scheduled payments must be performed before any CANCEL_PAYMENT operations at the given timestamp.

Level 4

The banking system should support merging two accounts while retaining both accounts' balance and transaction histories

merge_accounts (self, timestamp: int, account_id_1: str, account_id_2: str) -> bool
- Should merge account_id_2 into the account_id_1.
Returns True if accounts were successfully merged, or False otherwise.
Specifically:
• Returns False If account_id_1 is equal to account_id_2.
• Returns False if account_id_1 or account_id_2 doesn't exist.
• All pending cashback refunds for account_id_2 should still be processed, but refunded to account_id_1 instead.
• After the merge, it must be possible to check the status of payment transactions for account_id_2 with payment
identifiers by replacing account_id_2 with account_id_1
• The balance of account_sa_2 should be added to the balance for account_id_1
• top_spenders operations should recognize merged accounts - the total outgoing transactions for merged accounts
should be the sum of all money transferred and/or withdrawn in both accounts.
• account_id_2 should be removed from the system after the merge.

get_balance(self, timestamp: int, account_id: str, time_at: int) -> int | None
 - Should return the total amount of money in the account account_id at the given timestamp tine_at.
 If the specified account did not exist at a given time time_at, returns None
• If queries have been processed at timestamp time_at, get_balance must reflect the account balance after the query
has been processed.
• If the account was merged into another account, the merged account should inherit its balance history.

Note: Not clear what to return for a get_balance query of a deleted account in the merge. This version returns
the balance by tracing to the target account in the merge.

Variants:
- Level 3: schedule payment, cancel payment
- support payment, user get cashback after 24 hours of spending
- level 4: merge two accounts, need to merge accounts in the transfer system too. The banking system should support
 merging two accounts while retaining both accounts' balance and transaction histories.
- get balance, need to support timestamp, get the history balance of the specified account at a given timeAt
"""
import enum
from bisect import bisect_right
from typing import Dict, Type, Self

from sortedcontainers import SortedList, SortedDict

MILLISECONDS_IN_1_DAY = 86400000
FALSE = "false"
TRUE = "true"


class Account:

    def __init__(self, ts: int, acct_id: str):
        self.ts = ts
        self.acct_id = acct_id
        self.balance: int = 0
        self.activity: int = 0
        self.sent: int = 0
        self.log: SortedList[BalLog] = SortedList(key=lambda x: x.ts)  # or SortedDict(ts, balance)
        self.log.add(BalLog(ts, self, 0, BalLogType.CREATE, 0))

    def pay_v2(self, ts: int, amount: int) -> bool:
        if self.balance < amount:
            return False
        self.balance -= amount
        self.activity += amount
        self.sent += amount
        self.log.add(BalLog(ts, self, amount, BalLogType.PAY_V2, self.balance))
        return True

    def pay(self, ts: int, amount: int):
        if self.balance < amount:
            return ""
        self.balance -= amount
        self.activity += amount
        self.sent += amount
        self.log.add(BalLog(ts, self, amount, BalLogType.PAY, self.balance))
        return f"{self.balance}"

    def deposit(self, ts: int, amount: int):
        self.balance += amount
        self.activity += amount
        self.log.add(BalLog(ts, self, amount, BalLogType.DEPOSIT, self.balance))
        return f"{self.balance}"

    def merge(self, ts: int, acct: Type[Self]):
        self.balance += acct.balance
        self.activity += acct.activity
        self.sent += acct.sent
        self.log.update(acct.log)
        self.log.add(BalLog(ts, self, acct.balance, BalLogType.MERGE_T, self.balance))
        return True

    def get_balance(self, ts: int) -> int | None:
        """get balance in any timestamp"""
        id = bisect_right(self.log, ts, key=lambda log: log.ts) - 1
        if id < 0:
            return None  # before the account was created
        return self.log[id].bal


class Payment:
    def __init__(self, ts: int, acct: Account, payment_id: str, amount: int):
        self.ts = ts
        self.acct = acct
        self.payment_id = payment_id
        self.amount = amount


class Transfer:
    def __init__(self, ts: int, src: Account, target: Account, amount: int):
        self.ts = ts
        self.src = src
        self.target = target
        self.amount = amount


class BalLogType(enum.Enum):
    CREATE = "create"
    PAY = "pay"
    PAY_V2 = "pay_v2"
    DEPOSIT = "deposit"
    MERGE_T = "merge_target"
    MERGE_S = "merge_src"


class BalLog:
    def __init__(self, ts: int, acct: Account, amount: int, typ: BalLogType, bal: int):
        self.ts = ts
        self.acct = acct
        self.amount = amount
        self.typ = typ
        self.bal = bal


class Bank:
    def __init__(self):
        self.accts: Dict[str, Account] = dict()  # id->account
        self.m_accts: Dict[str, Account] = dict()  # accounts merged into another acct, id -> account
        self.xfer_id: int = 1
        self.p_xfers: dict[int, Transfer] = dict()  # pending xfers xfer_id:xfer
        self.c_xfers: Dict[int, Transfer] = dict()  # completed
        self.payment_id: int = 1
        self.payments: SortedDict[str, Payment] = SortedDict()  # queue of payments to process cashback
        self.c_payments: dict[str, Payment] = dict()  # payment_id -> payment
        self.merges: dict[Account, Account] = dict()  # src -> target

    def create_acct(self, ts: str, acct_id: str) -> str:
        if acct_id in self.accts:
            return FALSE
        self.accts[acct_id] = Account(int(ts), acct_id)
        return TRUE

    def deposit(self, ts: str, acct_id: str, amount: str) -> str:
        if acct_id not in self.accts:
            return ""
        return f"{self.accts[acct_id].deposit(int(ts), int(amount))}"

    def pay_v2(self, ts: int, account_id: str, amount: int) -> str | None:
        if account_id not in self.accts:
            return None
        can_pay = self.accts[account_id].pay_v2(ts, amount)
        if not can_pay:
            return None
        p_id_int = self.payment_id
        res = f"payment{p_id_int}"
        self.payment_id += 1
        self.payments[res] = Payment(ts, self.accts[account_id], res, amount)
        return res

    def get_payment_status(self, ts: int, acct_id: str, payment_id: str) -> str | None:
        if acct_id not in self.accts:
            return None
        if payment_id in self.c_payments and acct_id == self.c_payments[payment_id].acct.acct_id:
            return "CASHBACK_RECEIVED"
        if payment_id in self.payments:
            p = self.payments[payment_id]
            if p.acct.acct_id == acct_id:
                return "IN_PROGRESS"
        return None

    def pay(self, ts: str, acct_id: str, amount: str) -> str:
        if acct_id not in self.accts:
            return ""
        return f"{self.accts[acct_id].pay(int(ts), int(amount))}"

    def top(self, ts: str, n: str) -> str:
        accts = list(self.accts.values())
        accts.sort(key=lambda x: x.activity, reverse=True)
        return ", ".join([f"{a.acct_id}({a.activity})" for a in accts[:int(n)]])

    def top_senders(self, ts: str, n: str) -> str:
        accts = list(self.accts.values())
        accts.sort(key=lambda x: x.sent, reverse=True)
        return ", ".join([f"{a.acct_id}({a.sent})" for a in accts[:int(n)]])

    def xfer_v2(self, ts: int, src_acct_id: str, target_acct_id: str, amount: int) -> int | None:
        if src_acct_id == target_acct_id or src_acct_id not in self.accts or target_acct_id not in self.accts:
            return None
        src = self.accts[src_acct_id]
        if src.balance < amount:
            return None
        src, target = self.accts[src_acct_id], self.accts[target_acct_id]
        src.pay_v2(ts, amount)
        target.deposit(ts, amount)
        return src.balance

    def xfer(self, ts: str, src_acct_id: str, target_acct_id: str, amount: str) -> str:
        if src_acct_id == target_acct_id or src_acct_id not in self.accts:
            return ""
        src = self.accts[src_acct_id]
        xfer = Transfer(int(ts), self.accts[src_acct_id],
                        self.accts[target_acct_id], int(amount))
        if src.balance < xfer.amount:
            return ""
        xfer_id_str = f"transfer{self.xfer_id}"
        self.p_xfers[self.xfer_id] = xfer
        self.xfer_id += 1
        return xfer_id_str

    def ac_xfer(self, ts: str, acct_id: str, xfer_id: str) -> str:
        xfer_id = int(xfer_id[len("transfer"):])
        ts = int(ts)
        if xfer_id not in self.p_xfers:
            return FALSE
        xfer = self.p_xfers[xfer_id]
        if xfer.target.acct_id != acct_id:
            return FALSE
        if ts - xfer.ts > MILLISECONDS_IN_1_DAY:
            del self.p_xfers[xfer_id]
            return FALSE
        xfer.src.pay(ts, xfer.amount)
        xfer.target.deposit(ts, xfer.amount)
        self.c_xfers[xfer_id] = xfer
        del self.p_xfers[xfer_id]
        return TRUE

    def cash_back(self, ts: str) -> None:
        pays = self.payments
        while pays and pays.peekitem(0)[1].ts + MILLISECONDS_IN_1_DAY <= int(ts):
            p = pays.popitem(0)[1]
            self.deposit(ts, p.acct.acct_id, str(round(p.amount * 0.02)))
            self.c_payments[p.payment_id] = p

    def merge_accounts(self, ts: int, acct_id1: str, acct_id2: str) -> bool:
        if acct_id2 not in self.accts or acct_id1 not in self.accts or acct_id1 == acct_id2:
            return False
        src, target = self.accts[acct_id2], self.accts[acct_id1]
        del self.accts[acct_id2]
        self.merges[src] = target
        self.m_accts[acct_id2] = src
        src.log.add(BalLog(ts, src, -src.balance, BalLogType.MERGE_S, 0))
        for p in self.payments.values():
            if p.acct.acct_id == acct_id2:
                p.acct = target  # modify payment
        for xfer_id, xfer in self.p_xfers.copy().items():
            if xfer.src.acct_id == acct_id2:
                if xfer.target.acct_id == acct_id1:  # target is the account to merge into
                    del self.p_xfers[xfer_id]  # no longer need to transfer or add to completed transfers
                else:
                    self.c_xfers[xfer_id].src = target  # transfer need to start from the new merged account
        return target.merge(int(ts), src)

    def get_balance(self, ts: int, account_id: str, time_at: int) -> int | None:
        if account_id in self.m_accts:  # account already merged
            acct = self.m_accts[account_id]
            if time_at > acct.log[-1].ts or time_at < acct.log[0].ts:  # after merge or before create
                return None
            # trace to the merged account
            merge_target = self.merges[acct]
            return self.get_balance(ts, merge_target.acct_id, time_at)
        if account_id in self.accts:
            return self.accts[account_id].get_balance(time_at)
        return None


def solution(queries):
    bank = Bank()
    res = []
    for q in queries:
        bank.cash_back(q[1])
        match (q[0]):
            case "CREATE_ACCOUNT":
                res.append(bank.create_acct(q[1], q[2]))
            case "DEPOSIT":
                res.append(bank.deposit(q[1], q[2], q[3]))
            case "PAY":
                res.append(bank.pay(q[1], q[2], q[3]))
            case "PAY_V2":
                res.append(bank.pay_v2(q[1], q[2], q[3]))
            case "GET_PAYMENT_STATUS":
                res.append(bank.get_payment_status(q[1], q[2], q[3]))
            case "TOP_ACTIVITY":
                res.append(bank.top(q[1], q[2]))
            case "TOP_SPENDERS":
                res.append(bank.top_senders(q[1], q[2]))
            case "TRANSFER":
                res.append(bank.xfer(q[1], q[2], q[3], q[4]))
            case "TRANSFER_V2":
                res.append(bank.xfer_v2(q[1], q[2], q[3], q[4]))
            case "ACCEPT_TRANSFER":
                res.append(bank.ac_xfer(q[1], q[2], q[3]))
            case "MERGE_ACCOUNTS":
                res.append(bank.merge_accounts(q[1], q[2], q[3]))
            case "GET_BALANCE":
                res.append(bank.get_balance(q[1], q[2], q[3]))
            case _:
                res.append("unsupported")
    return res
