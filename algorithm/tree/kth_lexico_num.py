"""leet code 440, hard"""


class Solution:
    """44ms, 16.4mb"""

    def findKthNumber(self, n: int, k: int) -> int:
        def cntSteps(cur: int) -> int:
            res, next = 0, cur + 1
            while cur <= n:
                res += min(n + 1, next) - cur
                cur *= 10
                next *= 10
            return res

        cur = 1
        k -= 1
        while k > 0:
            steps = cntSteps(cur)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur
