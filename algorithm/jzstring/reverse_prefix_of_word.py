"""LeetCode 2000: Reverse Prefix of Word."""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Searching for the first occurrence takes O(n) time.
        right = word.find(ch)
        if right == -1:
            return word

        letters = list(word)
        left = 0
        while left < right:  # At most n/2 swaps: O(n) time.
            letters[left], letters[right] = letters[right], letters[left]
            left += 1
            right -= 1

        # The mutable copy and the returned string each use O(n) space.
        return "".join(letters)
