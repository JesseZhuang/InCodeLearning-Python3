"""LeetCode 1653: minimum deletions to make a string balanced."""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        """One-pass DP; O(n) time and O(1) auxiliary space."""
        deletions = 0
        b_count = 0

        for char in s:  # O(n) time; each character is processed once.
            if char == "a":
                # Keep this 'a' by deleting earlier 'b's, or delete this 'a'.
                deletions = min(deletions + 1, b_count)
            else:
                b_count += 1

        return deletions

    def minimumDeletionsBySplit(self, s: str) -> int:
        """Return the minimum deletions by checking every balanced split."""
        n = len(s)
        suffix_a = [0] * (n + 1)  # O(n) auxiliary space.
        for index in range(n - 1, -1, -1):  # O(n) time to count suffix 'a's.
            suffix_a[index] = suffix_a[index + 1] + (s[index] == "a")

        minimum = suffix_a[0]  # Split before the first character.
        prefix_b = 0
        for split in range(1, n + 1):  # O(n) time to scan all split points.
            if s[split - 1] == "b":
                prefix_b += 1
            minimum = min(minimum, prefix_b + suffix_a[split])

        return minimum
