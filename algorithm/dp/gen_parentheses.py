"""leet code 22, medium, tags: string, dynamic programming, backtracking."""


class Solution:
    """backtracking. n-th Catalan number 1/(n+1)*(2n choose n), O(4^n/sqrt(n)) time and space."""

    def generateParenthesis(self, n: int) -> list[str]:
        res: list[str] = []

        def backtrack(cur: list[str], left: int, right: int) -> None:
            if len(cur) == 2 * n:  # O(n) per valid string copy
                res.append(''.join(cur))
                return
            if left < n:  # can still open
                cur.append('(')
                backtrack(cur, left + 1, right)
                cur.pop()
            if right < left:  # can close without mismatch
                cur.append(')')
                backtrack(cur, left, right + 1)
                cur.pop()

        backtrack([], 0, 0)
        return res


class Solution2:
    """DP decomposition. f(n) = (f(i))f(n-1-i) for i in [0,n). O(4^n/sqrt(n)) time and space."""

    def generateParenthesis(self, n: int) -> list[str]:
        dp: list[list[str]] = [[] for _ in range(n + 1)]
        dp[0] = ['']
        for k in range(1, n + 1):  # O(Catalan(n)) total combinations
            for i in range(k):  # split: i pairs inside, k-1-i pairs outside
                for left in dp[i]:
                    for right in dp[k - 1 - i]:
                        dp[k].append(f'({left}){right}')
        return dp[n]
