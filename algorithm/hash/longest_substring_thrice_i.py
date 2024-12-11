"""leet 2981, medium"""


class Solution:
    """todo editorial 23 ms, 17.5 mb"""

    def maximumLength(self, s: str) -> int:
        # Create a dictionary (equivalent of map in Python) to store the count of all substrings
        count = {}
        for start in range(len(s)):
            curr_string = (
                []
            )  # Use a list to store the characters of the current substring
            for end in range(start, len(s)):
                # If the string is empty, or the current character is equal to
                # the previously added character, then append it to the list.
                # Otherwise, break the iteration.
                if not curr_string or curr_string[-1] == s[end]:
                    curr_string.append(s[end])
                    curr_to_string = "".join(
                        curr_string
                    )  # Convert the list to a string
                    if curr_to_string in count:
                        count[curr_to_string] += 1
                    else:
                        count[curr_to_string] = 1
                else:
                    break

        # Create a variable ans to store the longest length of substring with
        # frequency at least 3.
        ans = 0
        for str, freq in count.items():
            if freq >= 3 and len(str) > ans:
                ans = len(str)

        if ans == 0:
            return -1
        return ans
