"""leet code 465, hard, lint code 707"""
import sys
from typing import (
    List,
)


class Solution:
    """
    @param edges: a directed graph where each edge is represented by a tuple
    @return: the number of edges
    """

    def balance_graph(self, edges: List[List[int]]) -> int:
        bal = dict()
        for e in edges:
            bal[e[0]] = bal.get(e[0], 0) - e[2]
            bal[e[1]] = bal.get(e[1], 0) + e[2]
        non_zero = []
        for n in bal.values():
            if n: non_zero.append(n)
        m = len(non_zero)
        f = [sys.maxsize] * (1 << m)
        f[0] = 0
        for i in range(1, 1 << m):
            total = 0  # total balances in this subset
            for j in range(0, m):
                if (i >> j) & 1 == 1: total += non_zero[j]
            if total == 0:
                f[i] = i.bit_count() - 1
                j = (i - 1) & i
                while j > 0:
                    f[i] = min(f[i], f[j] + f[j ^ i])
                    j = (j - 1) & i
        return f[1 << m - 1]
