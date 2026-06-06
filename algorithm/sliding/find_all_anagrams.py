"""leet 438, medium, tags: hash table, string, sliding window."""


class Solution:
    """sliding window with fixed size and count array. O(n) time, O(1) space."""

    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        if len(p) > len(s):
            return res
        cnt = [0] * 26
        for c in p:
            cnt[ord(c) - ord('a')] += 1  # O(m)
        for i in range(len(s)):  # O(n), each char enters and leaves window once
            cnt[ord(s[i]) - ord('a')] -= 1
            if i >= len(p):
                cnt[ord(s[i - len(p)]) - ord('a')] += 1
            if all(v == 0 for v in cnt):  # O(26) = O(1)
                res.append(i - len(p) + 1)
        return res


class Solution2:
    """sliding window tracking matches count. O(n) time, O(1) space."""

    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        if len(p) > len(s):
            return res
        cnt = [0] * 26
        for c in p:
            cnt[ord(c) - ord('a')] += 1
        matches = 0
        for i in range(26):  # O(26)
            if cnt[i] == 0:
                matches += 1
        for i in range(len(s)):  # O(n)
            idx = ord(s[i]) - ord('a')
            cnt[idx] -= 1
            if cnt[idx] == 0:
                matches += 1
            elif cnt[idx] == -1:
                matches -= 1
            if i >= len(p):
                idx = ord(s[i - len(p)]) - ord('a')
                cnt[idx] += 1
                if cnt[idx] == 0:
                    matches += 1
                elif cnt[idx] == 1:
                    matches -= 1
            if matches == 26:
                res.append(i - len(p) + 1)
        return res
