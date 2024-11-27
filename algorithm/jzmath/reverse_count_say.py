"""companies: pinterest"""


class Solution:

    def reverseCountSay(self, s):
        res, n = [], len(s)
        for i in range(0, n, 2):
            cnt = int(s[i])
            ch = s[i + 1]
            res.extend([ch] * cnt)
        return ''.join(res)
