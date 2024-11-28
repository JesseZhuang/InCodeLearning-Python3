"""companies: pinterest"""


class Solution:
    """
    todo, look at other reverse look and say alg
    https://leetcode.com/discuss/interview-question/algorithms/124839/pinterest-reverse-count-and-say
    some does not limit count to single digit
    """

    def reverseCountSay(self, s):
        res, n = [], len(s)
        for i in range(0, n, 2):
            cnt = int(s[i])
            ch = s[i + 1]
            res.extend([ch] * cnt)
        return ''.join(res)
