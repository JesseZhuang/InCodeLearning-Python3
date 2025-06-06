"""leet 781, medium"""
import collections


class Solution:
    """todo editorial"""

    def numRabbits(self, answers):
        c = collections.Counter()
        res = 0
        for i in answers:
            if c[i] % (i + 1) == 0:
                res += i + 1
            c[i] += 1
        return res
