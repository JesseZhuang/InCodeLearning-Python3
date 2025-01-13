"""leet 1422, easy"""


class Solution:
    """0 ms, 17.80 mb"""

    def maxScore(self, s: str) -> int:
        res, zero, r1 = 0, 0, s.count('1')
        for i in range(len(s) - 1):
            zero += s[i] == '0'  # zeros count
            r1 -= s[i] == '1'  # remaining ones count
            res = max(res, zero + r1)
        return res
