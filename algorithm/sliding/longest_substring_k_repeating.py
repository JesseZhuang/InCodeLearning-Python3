"""LeetCode 395 medium, longest substring with at least k repeating characters."""

from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """Divide and conquer — split on characters with freq < k.

        Any character appearing fewer than k times cannot be in any valid
        substring, so it acts as a natural split point.
        """
        if len(s) < k:
            return 0
        freq = Counter(s)
        for ch in freq:  # O(26) unique chars at most
            if freq[ch] < k:
                # ch cannot appear in any valid substring — split on it
                return max(  # O(n) split, recurse on each part
                    self.longestSubstring(part, k)
                    for part in s.split(ch)
                )
        return len(s)  # all chars meet threshold
        # Time O(26·n) = O(n) — at most 26 levels, each scans O(n)
        # Space O(26) = O(1) — recursion depth bounded by alphabet size

    def longestSubstring2(self, s: str, k: int) -> int:
        """Sliding window — enumerate target unique count 1..26.

        For each target number of unique characters, use a two-pointer
        window that expands when unique count <= target and shrinks otherwise.
        """
        n = len(s)
        unique_total = len(set(s))
        res = 0
        for target in range(1, unique_total + 1):  # O(26) targets
            count = [0] * 26
            left = 0
            unique = 0
            at_least_k = 0
            for right in range(n):  # O(n) per target
                idx = ord(s[right]) - ord('a')
                if count[idx] == 0:
                    unique += 1
                count[idx] += 1
                if count[idx] == k:
                    at_least_k += 1
                while unique > target:  # shrink window
                    li = ord(s[left]) - ord('a')
                    if count[li] == k:
                        at_least_k -= 1
                    count[li] -= 1
                    if count[li] == 0:
                        unique -= 1
                    left += 1
                if unique == target == at_least_k:
                    res = max(res, right - left + 1)
        return res
        # Time O(26·n) = O(n), Space O(26) = O(1)
