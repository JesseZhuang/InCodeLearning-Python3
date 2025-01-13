"""leet 2559, medium"""


class Solution(object):
    """11 ms, 49.6 mb"""

    def vowelStrings(self, words, queries):
        psa, s, vowels = [0], 0, 'aeiou'
        for w in words:
            if w[0] in vowels and w[-1] in vowels:
                s += 1
            psa.append(s)
        res = []
        for l, r in queries:
            res.append(psa[r + 1] - psa[l])
        return res
