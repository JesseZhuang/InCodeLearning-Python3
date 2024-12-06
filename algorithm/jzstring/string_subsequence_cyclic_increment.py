"""leet 2585, medium"""


class Solution:
    """todo editorial, n+m, 1"""

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        str2_index = 0
        length_str1, length_str2 = len(str1), len(str2)

        # Traverse through both strings using a for loop
        for str1_index in range(length_str1):
            if str2_index < length_str2 and (
                    str1[str1_index] == str2[str2_index]
                    or ord(str1[str1_index]) + 1 == ord(str2[str2_index])
                    or ord(str1[str1_index]) - 25 == ord(str2[str2_index])
            ):
                # If match found, move to next character in str2
                str2_index += 1

        # Check if all characters in str2 were matched
        return str2_index == length_str2
