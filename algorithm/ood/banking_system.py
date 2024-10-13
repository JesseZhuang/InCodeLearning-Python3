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

- design deposit system, support create account, deposit and transfer
- support top sender, return top n spenders, transfer A->B is considered spending for A
- design delay transfer operation, make sure the account balance is enough to transfer
- support payment, user get cashback after 24 hours of spending
- merge two accounts, need to merge accounts in the transfer system too
- get balance, need to support timestamp
"""


class Account:

    def __init__(self, timestamp: str, account_id: str):
        self.timestamp = int(timestamp)
        self.account_id = account_id


def solution(queries):
    pass
