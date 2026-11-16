"""leet 1358, medium"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Track last position of a, b, c
        last_pos = [-1] * 3
        total = 0

        for pos in range(len(s)):  # O(n) time
            # Update last position of current character
            last_pos[ord(s[pos]) - ord("a")] = pos

            # Add count of valid substrings ending at current position
            # If any character is missing, min will be -1
            # Else min gives leftmost required character position
            total += 1 + min(last_pos)

        return total  # O(1) auxiliary space


class Solution2:
    def numberOfSubstrings(self, s: str) -> int:
        counts = [0] * 3  # O(1) auxiliary space
        left = total = 0

        for right, char in enumerate(s):  # O(n) time; each left index advances once
            counts[ord(char) - ord("a")] += 1

            # Shrink until this window no longer contains all three characters.
            while counts[0] and counts[1] and counts[2]:
                left_char = s[left]
                counts[ord(left_char) - ord("a")] -= 1
                left += 1

            # Every start before left still forms a valid substring ending at right.
            total += left

        return total  # O(1) auxiliary space
