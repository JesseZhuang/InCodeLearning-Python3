"""leet code 465, hard, lint code 707"""
import sys
from collections import defaultdict
from typing import List


class Solution1:
    """note: test in lint code python 2, bit_count need to count in enumeration above"""

    def balance_graph(self, edges: List[List[int]]) -> int:
        """
        @param edges: a directed graph where each edge is represented by a tuple
        @return: the number of edges
        """
        bal = defaultdict(int)
        for f, t, amount in edges:
            bal[f] -= amount
            bal[t] += amount
        non_zero = [b for b in bal.values() if b != 0]
        n = len(non_zero)
        f = [sys.maxsize] * (1 << n)  # python2 sys.maxint, python3 sys.maxsize, or inf
        f[0] = 0
        for i in range(1, 1 << n):
            total = 0  # total balances in this subset
            for j, x in enumerate(non_zero):
                if i >> j & 1:
                    total += x
            if total == 0:
                f[i] = i.bit_count() - 1  # bit_count() needs python 3.10
                j = (i - 1) & i
                while j > 0:
                    f[i] = min(f[i], f[j] + f[j ^ i])
                    j = (j - 1) & i
        return f[-1]  # f[(1<<n)-1]


class Solution2:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance_map = defaultdict(int)
        for transaction in transactions:
            u, v, amount = transaction
            balance_map[u] -= amount
            balance_map[v] += amount
        # Step 2: Collect non-zero balances only
        balances = [balance for balance in balance_map.values() if balance != 0]
        balances.sort(reverse=True)

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
