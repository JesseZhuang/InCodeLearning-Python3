"""LeetCode 139, medium, tags: dynamic programming, hash table, string, trie, memoization."""

from collections import deque


class Solution:
    """DP with hash set."""

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)  # O(n) space
        dp[0] = True
        word_set = set(wordDict)  # O(m*k) space
        for i in range(1, n + 1):  # O(n)
            for j in range(i):  # O(n)
                if dp[j] and s[j:i] in word_set:  # O(k) substring
                    dp[i] = True
                    break
        return dp[n]


class Solution2:
    """BFS."""

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        visited = [False] * n
        q = deque([0])
        word_set = set(wordDict)  # O(m*k) space
        while q:  # O(n)
            start = q.popleft()
            if visited[start]:
                continue
            for end in range(start + 1, n + 1):  # O(n)
                if s[start:end] in word_set:  # O(k) substring
                    if end == n:
                        return True
                    q.append(end)
            visited[start] = True
        return False
