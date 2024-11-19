"""leet code 1055, medium, lint code 3652"""
import math


class Solution:
    """
    @param s: Source string
    @param target: Target string
    @return: Number of subsequences that can be spliced into target
    """

    def shortest_way(self, s: str, target: str) -> int:
        """62ms, 5.05mb"""
        m, n = map(len, (s, target))
        res = j = 0
        while j < n:
            found, i = False, 0
            while i < m and j < n:
                if s[i] == target[j]:
                    j += 1
                    found = True
                i += 1
            if not found: return -1
            res += 1
        return res


class Solution2:
    def shortest_way(self, s: str, tar: str) -> int:
        if any(c not in s for c in tar):
            return -1
        res, n = 0, len(s)
        for c in tar:
            while c != s[res % n]:
                res += 1
        return math.ceil((res + 1) / n)  # res//n + 1
