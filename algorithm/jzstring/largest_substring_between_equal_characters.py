"""LeetCode 1624: Largest Substring Between Two Equal Characters."""


class Solution:
    """Track each character's first position while scanning the string.

    Time O(n), where n is the length of ``s``. Space O(1), since lowercase
    English letters bound the first-position table to 26 entries.
    """

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_index: dict[str, int] = {}
        longest = -1

        for index, char in enumerate(s):  # O(n) total iterations
            if char in first_index:
                longest = max(longest, index - first_index[char] - 1)
            else:
                first_index[char] = index

        return longest
