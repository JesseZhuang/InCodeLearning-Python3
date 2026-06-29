from collections import Counter


class Solution:
    """lc 2131 Longest Palindrome by Concatenating Two Letter Words.

    Greedy with hash map counting.
    Time O(n), Space O(n) where n = len(words).
    """

    def longestPalindrome(self, words: list[str]) -> int:
        count = Counter(words)  # O(n) space
        length = 0
        has_center = False

        for word, freq in count.items():  # O(n) unique words
            rev = word[1] + word[0]
            if word == rev:
                # Palindromic word like "aa", "bb"
                pairs = freq // 2  # O(1)
                length += pairs * 4
                if freq % 2 == 1:
                    has_center = True
            elif word < rev and rev in count:
                # Non-palindromic pair like "ab"/"ba"
                pairs = min(freq, count[rev])  # O(1)
                length += pairs * 4

        if has_center:
            length += 2

        return length
