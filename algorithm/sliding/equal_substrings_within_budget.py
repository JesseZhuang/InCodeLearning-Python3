"""LeetCode 1208, medium, tags: string, sliding window."""


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """Sliding window, O(n) time and O(1) extra space."""
        left = cost = best = 0
        for right in range(len(s)):  # O(n): visit each right endpoint once.
            cost += abs(ord(s[right]) - ord(t[right]))
            while cost > maxCost:  # O(n) amortized: left advances at most n times overall.
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            best = max(best, right - left + 1)
        return best
