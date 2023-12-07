'''leet code 279 medium'''


import math


class Solution:
    def numSquares1(self, n: int) -> int:
        '''2866ms, 16.4Mb'''
        dp = [0]
        while len(dp) <= n:
            m = len(dp)
            i, sq = 1, math.inf
            while i*i <= m:
                sq = min(sq, dp[m-i*i]+1)
                i += 1
            dp.append(sq)
        return dp[n]

    def numSquares(self, n: int) -> int:
        '''43ms, 16.3Mb '''
        # 4^a(8b+7)
        sr = int(math.sqrt(n))
        if sr*sr == n:
            return 1
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        i = 1
        while i*i <= n:
            sq = i*i
            base = int(math.sqrt(n-sq))
            if base*base+sq == n:
                return 2
            i += 1
        return 3
