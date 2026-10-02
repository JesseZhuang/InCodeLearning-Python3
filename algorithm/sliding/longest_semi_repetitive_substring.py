"""LeetCode 2730: find the longest substring with at most one equal adjacent pair."""


class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = 0
        equal_pairs = 0
        longest = 0

        for right in range(len(s)):  # O(n) time; each character enters the window once.
            if right > 0 and s[right] == s[right - 1]:
                equal_pairs += 1

            while equal_pairs > 1:  # O(n) total; left advances at most n times.
                if s[left] == s[left + 1]:
                    equal_pairs -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest
