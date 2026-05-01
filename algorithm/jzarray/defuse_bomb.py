"""LeetCode 1652 Defuse the Bomb"""


class Solution:
    """Rolling sum (similar to Rabin-Karp). O(n) time, O(1) space (excluding result)."""

    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        res = [0] * n
        if k == 0:
            return res
        start, end = 1, k  # index [1, k]
        if k < 0:  # index [n-|k|, n-1]
            start = n - abs(k)
            end = n - 1
        s = sum(code[i] for i in range(start, end + 1))
        for i in range(n):
            res[i] = s
            s -= code[start % n]
            start += 1
            end += 1
            s += code[end % n]
        return res
