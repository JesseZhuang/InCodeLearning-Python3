"""
biweekly 140, Q4, hard
return the smallest starting index of s that the substring starting at that index is almost equal to pattern.
if no such index exists, return -1.

Constraints:
1. 1 <= word2.length < word1.length <= 3 * 10^5, n,m
2. word1 and word2 consist only of lowercase English letters
"""


class Solution1:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def calc_z(s):
            # 计算字符串 s 的 z 函数
            n = len(s)
            z = [0] * n
            l, r = 0, 0
            for i in range(1, n):
                if i <= r:
                    z[i] = min(z[i - l], r - i + 1)
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    l, r = i, i + z[i]
                    z[i] += 1
            z[0] = n
            return z

        n = len(pattern)
        z1 = calc_z(pattern + s)[n:]
        z2 = calc_z(pattern[::-1] + s[::-1])[n:][::-1]
        # print(z1)
        # print(z2)
        i = 0
        while True:
            if i + n - 1 >= len(s):
                return -1
            # print(i, i + n - 1)
            if min(n, z1[i]) + min(n, z2[i + n - 1]) >= n - 1:
                return i
            i += 1


# zfunc
def zfunc(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0  # [l, r)
    for i in range(1, n):
        if i < r: z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]: z[i] += 1
        if i + z[i] > r: l, r = i, i + z[i]
    return z


class Solution2:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        m, n = len(s), len(pattern)
        z1 = zfunc(pattern + s)
        z2 = zfunc(pattern[::-1] + s[::-1])
        for i in range(m):
            if i + n > m: break
            c1 = z1[i + n]
            if c1 >= n: return i
            j = i + n - 1
            c2 = z2[m - j - 1 + n]
            if c1 + c2 == n - 1: return i
        return -1
