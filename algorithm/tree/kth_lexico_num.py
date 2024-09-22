"""leet code 440, hard"""


class Solution:
    """44ms, 16.4mb"""

    def findKthNumber(self, n: int, k: int) -> int:
        def cntSteps(p1: int, p2: int) -> int:
            res = 0
            while p1 <= n:
                res += min(n + 1, p2) - p1
                p1 *= 10
                p2 *= 10
            return res

        cur = 1
        k -= 1
        while k > 0:
            steps = cntSteps(cur, cur + 1)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur
