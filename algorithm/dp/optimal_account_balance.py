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
        non_zero = [b for b in bal.values() if b]
        n = len(non_zero)
        f = [sys.maxsize] * (1 << n)  # python2 sys.maxint, python3 sys.maxsize, inf, or 1<<29
        f[0] = 0
        for i in range(1, 1 << n):
            total = 0  # total balances in this subset
            for j, x in enumerate(non_zero):
                if i >> j & 1:
                    total += x  # bit_cnt += 1 for py < 3.10
            if total == 0:
                f[i] = i.bit_count() - 1  # bit_count() needs python 3.10
                j = (i - 1) & i
                while j > 0:
                    f[i] = min(f[i], f[j] + f[j ^ i])
                    j = (j - 1) & i
        return f[-1]  # f[(1<<n)-1]


class Solution2:
    """TLE lint code"""

    def minTransfers(self, edges: List[List[int]]) -> int:
        bal = defaultdict(int)
        for u, v, w in edges:
            bal[u] -= w
            bal[v] += w
        # Step 2: Collect non-zero balances only
        non_zero = [b for b in bal.values() if b != 0]
        non_zero.sort(reverse=True)

        # Step 3: Use DFS with backtracking to minimize transactions
        def dfs(start: int) -> int:
            while start < len(non_zero) and non_zero[start] == 0:
                start += 1
            # Base case: All balances settled
            if start == len(non_zero):
                return 0
            res = float('inf')
            # Try to settle balances[start] with subsequent balances
            for i in range(start + 1, len(non_zero)):
                if non_zero[i] * non_zero[start] < 0:  # Opposite signs only
                    # Settle balances[start] with balances[i]
                    non_zero[i] += non_zero[start]
                    # Recur to settle the next balance and count this transaction
                    res = min(res, 1 + dfs(start + 1))
                    # Backtrack to previous state
                    non_zero[i] -= non_zero[start]
                    # Optimization: Stop if an exact zero balance is found
                    if non_zero[i] + non_zero[start] == 0:
                        break
            return res

        return dfs(0)
