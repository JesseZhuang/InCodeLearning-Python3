"""LeetCode 424 medium, longest repeating character replacement."""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Sliding window with frequency count.

        Maintain a window where (window_len - max_freq) <= k.
        When this invariant breaks, shrink from left.
        """
        count: dict[str, int] = {}
        left = 0
        max_freq = 0
        res = 0
        for right in range(len(s)):  # O(n)
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])  # O(1)
            while (right - left + 1) - max_freq > k:  # O(n) total shrinks
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res  # Time O(n), Space O(26) = O(1)

    def characterReplacement2(self, s: str, k: int) -> int:
        """Binary search on answer length + sliding window check.

        Binary search for the largest window size L such that some window
        of size L has at least (L - k) occurrences of one character.
        """
        def can_achieve(length: int) -> bool:
            count: dict[str, int] = {}
            for i in range(len(s)):  # O(n) per check
                count[s[i]] = count.get(s[i], 0) + 1
                if i >= length:
                    count[s[i - length]] -= 1
                if i >= length - 1:
                    if max(count.values()) >= length - k:  # O(26) = O(1)
                        return True
            return False

        lo, hi = 1, len(s)  # O(log n) binary search iterations
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_achieve(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo  # Time O(n log n), Space O(26) = O(1)
