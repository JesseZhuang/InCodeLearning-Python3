class Solution:
    """LeetCode 567. Permutation in String. Sliding window with match count."""

    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False
        c1, c2 = [0] * 26, [0] * 26
        for i in range(l1):  # O(l1)
            c1[ord(s1[i]) - 97] += 1
            c2[ord(s2[i]) - 97] += 1
        count = sum(1 for i in range(26) if c1[i] == c2[i])
        for i in range(l2 - l1):  # O(l2 - l1), each iteration O(1)
            if count == 26:
                return True
            r = ord(s2[i + l1]) - 97
            c2[r] += 1
            if c2[r] == c1[r]:
                count += 1
            elif c2[r] == c1[r] + 1:
                count -= 1
            l = ord(s2[i]) - 97
            c2[l] -= 1
            if c2[l] == c1[l]:
                count += 1
            elif c2[l] == c1[l] - 1:
                count -= 1
        return count == 26


class Solution2:
    """Sorted comparison approach. O((l2-l1) * l1 * log(l1)) time, O(l1) space."""

    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False
        s1_sorted = sorted(s1)  # O(l1 * log(l1))
        for i in range(l2 - l1 + 1):  # O(l2 - l1) windows, each sort O(l1 * log(l1))
            if sorted(s2[i:i + l1]) == s1_sorted:
                return True
        return False
