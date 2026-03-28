"""leet code 638, medium"""

from functools import lru_cache
from typing import List


class Solution:
    """DFS + memoization.

    State = remaining needs (as tuple for hashing). At each state, try
    every valid offer and recurse. lru_cache guarantees each distinct
    needs-tuple is computed exactly once.
    """

    # 47ms, 19.74mb
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        special = [s for s in special if sum(s[i] * price[i] for i in range(n)) > s[-1]]

        # memo table holds up to m^n entries (m = max need, n = number of items)
        # each entry key is an n-tuple → total memo space: O(n * m^n)
        @lru_cache(maxsize=None)
        def dfs(needs):
            # base: buy everything at individual prices, O(n)
            res = sum(needs[i] * price[i] for i in range(n))
            # try each of k offers, O(n) work per offer to build updated tuple
            for offer in special:
                updated = tuple(needs[i] - offer[i] for i in range(n))
                if all(u >= 0 for u in updated):
                    res = min(res, offer[-1] + dfs(updated))
            # total time: O(n * k) per state × O(m^n) states = O(n * k * m^n)
            return res

        return dfs(tuple(needs))


class Solution2:
    """Backtracking without memoization.

    Process offers one by one (by index). For each offer, try using it
    0, 1, 2, … times before moving to the next offer. This avoids
    duplicate combinations (e.g. offer A then B vs B then A) by fixing
    the order. No memo table — space is only the recursion stack.
    """

    # 23ms, 19.65mb
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        special = [s for s in special if sum(s[i] * price[i] for i in range(n)) > s[-1]]

        # max recursion depth = k (number of offers), each frame stores O(n) needs list
        # total extra space: O(k * n)
        def dfs(idx, needs):
            # past last offer — buy all remaining items at individual prices, O(n)
            if idx == len(special):
                return sum(needs[i] * price[i] for i in range(n))
            # skip this offer entirely (use it 0 times)
            res = dfs(idx + 1, needs)
            updated = list(needs)
            times = 0
            # try applying offer[idx] repeatedly: 1 time, 2 times, …
            # loop runs at most m = max(needs) / min(offer qty) iterations
            while True:
                updated = [updated[i] - special[idx][i] for i in range(n)]  # O(n) per iteration
                if any(u < 0 for u in updated):  # exceeded some need, stop
                    break
                times += 1
                res = min(res, special[idx][-1] * times + dfs(idx + 1, updated))
            return res

        return dfs(0, needs)
