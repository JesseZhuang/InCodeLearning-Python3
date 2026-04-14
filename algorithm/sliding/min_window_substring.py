"""leet 76, hard, tags: hash table, string, sliding window."""


class Solution:
    """sliding window with count tracking. O(m+n) time, O(128) space."""

    def minWindow(self, s: str, t: str) -> str:
        cnt = [0] * 128
        for c in t:
            cnt[ord(c)] += 1  # O(n)
        not_found, left, min_l, min_r = len(t), 0, 0, len(s) + 1
        for right in range(len(s)):  # O(m), each char visited at most twice (right and left)
            cnt[ord(s[right])] -= 1
            if cnt[ord(s[right])] >= 0:
                not_found -= 1
            while not_found == 0:
                if right - left + 1 < min_r - min_l:
                    min_l, min_r = left, right + 1
                cnt[ord(s[left])] += 1
                if cnt[ord(s[left])] > 0:
                    not_found += 1
                left += 1
        return "" if min_r == len(s) + 1 else s[min_l:min_r]
