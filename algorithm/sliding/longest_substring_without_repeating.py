"""LeetCode 3 medium, longest substring without repeating characters."""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Sliding window with hash map storing last seen index.

        Slide right pointer one step at a time. When a duplicate is found,
        jump left pointer past the previous occurrence.
        """
        last_seen: dict[str, int] = {}
        left = 0
        res = 0
        for right, ch in enumerate(s):  # O(n) — single pass
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1  # O(1) jump
            last_seen[ch] = right
            res = max(res, right - left + 1)
        return res  # Time O(n), Space O(min(n, m)) where m is charset size

    def lengthOfLongestSubstring2(self, s: str) -> int:
        """Sliding window with hash set, shrink one step at a time."""
        seen: set[str] = set()
        left = 0
        res = 0
        for right in range(len(s)):  # O(n) outer
            while s[right] in seen:  # O(n) total across all iterations
                seen.discard(s[left])
                left += 1
            seen.add(s[right])
            res = max(res, right - left + 1)
        return res  # Time O(n), Space O(min(n, m))
