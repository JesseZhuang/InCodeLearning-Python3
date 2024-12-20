"""leet 691, hard"""
from collections import Counter
from functools import cache
from math import inf


class Solution1:
    """109ms, 18.08 mb"""

    def minStickers(self, stickers: list[str], target: str) -> int:
        scs = preprocess(stickers, target)

        @cache
        def dfs(t):  # target string
            if not t: return 0
            res = inf
            tc = Counter(t)
            for sc in scs:
                if t[0] in sc:  # use this sticker, explore remaining next target
                    nt = "".join(k * v for k, v in (tc - sc).items())
                    res = min(res, 1 + dfs(nt))
            return res

        res = dfs(target)
        return res if res < inf else -1


class Solution2:
    """357 ms, 17.86 mb"""

    def minStickers(self, stickers: list[str], target: str) -> int:
        t, scs = len(target), preprocess(stickers, target)
        m = 1 << t
        stickers = ["".join(sc.elements()) for sc in scs]
        # stickers = ["".join(k * v for k, v in sc.items()) for sc in scs]
        dp = [inf] * m  # dp[i]: min stickers for state i, e.g., i==1, first character is filled
        dp[0] = 0  # empty string
        for j in range(m):  # each state
            if dp[j] == inf: continue
            for s in stickers:  # each sticker
                cur = j
                for ch in s:  # try to use every char in sticker
                    for i, c in enumerate(target):
                        if (cur >> i) & 1: continue  # this character already filled
                        if c == ch:  # fill ith char in target with sticker s
                            cur |= 1 << i
                            break
                dp[cur] = min(dp[cur], dp[j] + 1)
        return dp[-1] if dp[-1] != inf else -1


def preprocess(stickers: list[str], target: str) -> list[Counter]:
    tc = Counter(target)  # target counter
    scs = [Counter(sticker) & tc for sticker in stickers]  # sticker counters
    for i in range(len(scs) - 1, -1, -1):
        if any(scs[i] == scs[i] & scs[j] for j in range(len(scs)) if i != j):
            scs.pop(i)
    return scs
