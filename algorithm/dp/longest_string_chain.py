class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key=len)  # O(n log n)
        dp = {}
        res = 1
        for word in words:  # O(n)
            dp[word] = 1
            for i in range(len(word)):  # O(L)
                predecessor = word[:i] + word[i + 1:]  # O(L) string slice
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
            res = max(res, dp[word])
        return res
