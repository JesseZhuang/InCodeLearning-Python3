"""leet 3223, medium"""
from collections import Counter


class Solution:
    """todo editorial"""

    def minimumLength(self, s: str) -> int:
        # Step 1: Count the frequency of each character in the string
        char_frequency_map = Counter(s)

        # Step 2: Calculate the number of characters to delete
        delete_count = 0
        for frequency in char_frequency_map.values():
            if frequency % 2 == 1:
                # If frequency is odd, delete all except one
                delete_count += frequency - 1
            else:
                # If frequency is even, delete all except two
                delete_count += frequency - 2

        # Step 3: Return the minimum length after deletions
        return len(s) - delete_count
