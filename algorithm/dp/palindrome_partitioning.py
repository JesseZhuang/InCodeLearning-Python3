"""LeetCode 131 Palindrome Partitioning"""


class Solution:
    """Backtracking with DP palindrome check. O(N*2^N) time, O(N^2) space."""

    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):  # O(N^2) fill palindrome table
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1])
        res = []
        self._dfs(s, 0, [], res, dp)
        return res

    def _dfs(self, s, start, path, res, dp):
        if start == len(s):
            res.append(path[:])
            return
        for end in range(start, len(s)):  # O(2^N) branches total
            if dp[start][end]:
                path.append(s[start:end + 1])
                self._dfs(s, end + 1, path, res, dp)
                path.pop()


class Solution2:
    """Backtracking with inline palindrome check. O(N*2^N) time, O(N) space."""

    def partition(self, s: str) -> list[list[str]]:
        res = []
        self._dfs(s, 0, [], res)
        return res

    def _dfs(self, s, start, path, res):
        if start == len(s):
            res.append(path[:])
            return
        for end in range(start, len(s)):  # O(2^N) branches
            if self._is_palindrome(s, start, end):
                path.append(s[start:end + 1])
                self._dfs(s, end + 1, path, res)
                path.pop()

    def _is_palindrome(self, s, lo, hi):  # O(N) per check
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True
