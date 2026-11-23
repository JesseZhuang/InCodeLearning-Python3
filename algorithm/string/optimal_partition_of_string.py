class Solution:
    """Greedy partitioning with a set of letters in the current substring."""

    def partitionString(self, s: str) -> int:
        seen = set()
        partitions = 1
        for char in s:  # O(n): each character is visited once.
            if char in seen:  # O(1) expected; at most 26 lowercase letters are stored.
                partitions += 1
                seen.clear()
            seen.add(char)
        return partitions


class Solution2:
    """Greedy partitioning with one bit per lowercase letter."""

    def partitionString(self, s: str) -> int:
        seen = 0
        partitions = 1
        for char in s:  # O(n): each character is visited once.
            bit = 1 << (ord(char) - ord("a"))
            if seen & bit:
                partitions += 1
                seen = 0
            seen |= bit
        return partitions
