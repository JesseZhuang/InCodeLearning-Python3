"""leet code 465, hard, lint code 707"""
import sys
from collections import defaultdict
from typing import List


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance_map = defaultdict(int)
        for transaction in transactions:
            u, v, amount = transaction
            balance_map[u] -= amount
            balance_map[v] += amount
        # Step 2: Collect non-zero balances only
        balances = [balance for balance in balance_map.values() if balance != 0]

        # Step 3: Use DFS with backtracking to minimize transactions
        def dfs(start: int) -> int:
            while start < len(balances) and balances[start] == 0:
                start += 1
            # Base case: All balances settled
            if start == len(balances):
                return 0
            res = float('inf')
            # Try to settle balances[start] with each subsequent balance
            for i in range(start + 1, len(balances)):
                if balances[i] * balances[start] < 0:  # Opposite signs only
                    # Settle balances[start] with balances[i]
                    balances[i] += balances[start]
                    # Recur to settle the next balance and count this transaction
                    res = min(res, 1 + dfs(start + 1))
                    # Backtrack to previous state
                    balances[i] -= balances[start]
                    # Optimization: Stop if an exact zero balance is found
                    if balances[i] + balances[start] == 0:
                        break
            return res

        return dfs(0)


class Solution2:

    def balance_graph(self, edges: List[List[int]]) -> int:
        """
        @param edges: a directed graph where each edge is represented by a tuple
        @return: the number of edges
        """
        bal = dict()
        for e in edges:
            bal[e[0]] = bal.get(e[0], 0) - e[2]
            bal[e[1]] = bal.get(e[1], 0) + e[2]
        non_zero = [b for b in bal.values() if b != 0]
        m = len(non_zero)
        f = [sys.maxsize] * (1 << m)
        f[0] = 0
        for i in range(1, 1 << m):
            total = 0  # total balances in this subset
            for j in range(0, m):
                if (i >> j) & 1 == 1:
                    total += non_zero[j]
            if total == 0:
                f[i] = i.bit_count() - 1
                j = (i - 1) & i
                while j > 0:
                    f[i] = min(f[i], f[j] + f[j ^ i])
                    j = (j - 1) & i
        return f[1 << m - 1]
