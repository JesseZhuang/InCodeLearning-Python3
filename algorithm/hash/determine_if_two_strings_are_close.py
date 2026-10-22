"""LeetCode 1657, medium, tags: hash table, string, sorting, counting."""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """Compare character sets and frequency multisets.

        Time O(n) for n characters and a fixed 26-letter alphabet.
        Space O(1) for two arrays of 26 counts.
        """
        if len(word1) != len(word2):
            return False

        first_counts = [0] * 26
        second_counts = [0] * 26
        for char in word1:  # O(n)
            first_counts[ord(char) - ord('a')] += 1
        for char in word2:  # O(n)
            second_counts[ord(char) - ord('a')] += 1

        for first, second in zip(first_counts, second_counts):  # O(26)
            if (first == 0) != (second == 0):
                return False

        return sorted(first_counts) == sorted(second_counts)  # O(26 log 26) = O(1)
