"""leet 423, medium"""
from collections import Counter


class Solution:
    """11 ms, 18.28 mb"""

    def originalDigits(self, s):
        cnt = Counter(s)  # O(n)
        d_s = ["zero", "two", "four", "six", "eight", "one", "three", "five", "seven", "nine"]
        d = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
        cnts = [Counter(d) for d in d_s]
        d_cnt = [0] * 10
        for it, c in enumerate(cnts):  # O(5*10)
            k = min(cnt[x] // c[x] for x in c)
            for i in c.keys(): c[i] *= k
            cnt -= c
            d_cnt[d[it]] = k
        return "".join(str(i) * d_cnt[i] for i in range(10))  # O(10)


class Solution2:
    """10 ms, 18.24 mb"""

    def originalDigits(self, s: str) -> str:
        cnt = Counter(s)  # O(n)
        res = [0 for _ in range(10)]
        # map, get even count
        res[0] = cnt['z']
        res[2] = cnt['w']
        res[4] = cnt['u']
        res[6] = cnt['x']
        res[8] = cnt['g']
        # get odd count
        res[1] = cnt['o'] - (res[0] + res[2] + res[4])
        res[3] = cnt['r'] - (res[0] + res[4])
        res[5] = cnt['f'] - res[4]
        res[7] = cnt['s'] - res[6]
        res[9] = cnt['i'] - (res[5] + res[6] + res[8])
        return ''.join(str(i) * c for i, c in enumerate(res))
