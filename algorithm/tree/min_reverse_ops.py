"""leet code 2612, hard"""
from collections import deque
from typing import List

from sortedcontainers import SortedList


class Solution1:
    """1788ms, 39.43mb"""

    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        remaining = [SortedList(), SortedList()]
        banned = set(banned)
        for i in range(n):
            if i != p and i not in banned:
                remaining[i & 1].add(i)

        q = deque()
        q.append(p)
        res = [-1] * n
        res[p] = 0
        while q:
            node = q.popleft()
            lo = max(node - (k - 1), 0)
            lo = 2 * lo + k - 1 - node
            hi = min(node + k - 1, n - 1) - (k - 1)
            hi = 2 * hi + k - 1 - node

            for nei in list(remaining[lo % 2].irange(lo, hi)):
                q.append(nei)
                res[nei] = res[node] + 1
                remaining[lo % 2].remove(nei)

        return res


class Solution2:
    """1059ms, 36.20mb"""

    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        res = [-1] * n
        for node in banned: res[node] = -2  # to speed up iterations
        q = deque([p])
        depth = 0
        res[p] = depth
        step = k - 1

        next_nei_s = [i + 2 for i in range(n)]  # might be out of range, next neighbor to visit

        while q:
            depth += 1
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                lo = max(cur - step, 0)
                hi = min(cur, n - k)  # Inclusive
                lo = 2 * lo + k - 1 - cur
                hi = 2 * hi + k - 1 - cur  # Inclusive
                # set next_nei_s[nei] to hi + 2 for every visited nei.
                post_hi = hi + 2
                nei = lo
                while nei <= hi:
                    next_nei = next_nei_s[nei]
                    next_nei_s[nei] = post_hi
                    if res[nei] == -1:
                        q.append(nei)
                        res[nei] = depth
                    nei = next_nei
        # Mark all banned positions as -1 (see above).
        for node in banned: res[node] = -1
        return res
