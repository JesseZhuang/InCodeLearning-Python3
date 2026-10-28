"""LeetCode 1963: Minimum Number of Swaps to Make the String Balanced."""


class Solution:
    def minSwaps(self, s: str) -> int:
        """Return the minimum swaps in O(n) time and O(1) extra space."""
        unmatched_open = 0
        for bracket in s:  # O(n): each bracket is examined once.
            if bracket == "[":
                unmatched_open += 1
            elif unmatched_open:
                unmatched_open -= 1

        return (unmatched_open + 1) // 2
