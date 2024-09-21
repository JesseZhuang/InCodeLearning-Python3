"""leet code 279, medium"""

import math


class Solution1:
    """2617ms, 16.61mb"""

    def __init__(self):
        self.dp = [0]

    def numSquares(self, n: int) -> int:
        dp = self.dp
        while len(dp) <= n:
            m = len(dp)
            i, nex = 1, math.inf
            while i * i <= m:
                nex = min(nex, dp[m - i * i] + 1)
                i += 1
            dp.append(nex)

        return dp[n]


class Solution2:
    """43ms, 16.32mb"""

    def numSquares(self, n: int) -> int:
        """43ms, 16.3Mb """
        # 4^a(8b+7)
        sr = int(math.sqrt(n))
        if sr * sr == n:
            return 1
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        i = 1
        while i * i <= n:
            sq = i * i
            base = int(math.sqrt(n - sq))
            if base * base + sq == n:
                return 2
            i += 1
        return 3
