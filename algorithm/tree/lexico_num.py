"""leet code 386, medium"""
from typing import List


class Solution1:
    """72ms, 22.25mb"""

    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        cur = 1
        for i in range(0, n):
            res.append(cur)
            if cur * 10 <= n:
                cur *= 10
            else:
                while cur % 10 == 9 or cur >= n: cur //= 10
                cur += 1
        return res


class Solution2:
    """93ms, 24.9mb"""

    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(start: int) -> None:
            if start > n: return
            res.append(start)
            for nd in range(0, 10):
                next = start * 10 + nd
                if next <= n:
                    dfs(next)
                else:
                    break

        for i in range(1, 10): dfs(i)
        return res
