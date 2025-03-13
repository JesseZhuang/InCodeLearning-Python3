"""leet 2375, medium"""


class Solution:
    """todo editorial"""

    def smallestNumber(self, pattern: str) -> str:
        pattern_length = len(pattern)
        max_so_far = curr_max = temp = 0

        # List to store lengths of decreasing subsequences in the pattern
        arr_D = [0 for _ in range(pattern_length + 2)]

        # Compute the lengths of decreasing subsequences in the pattern
        for pattern_index in range(pattern_length, -1, -1):
            if pattern_index < pattern_length and pattern[pattern_index] == "D":
                # If 'D', increment the length of the decreasing sequence
                arr_D[pattern_index] = arr_D[pattern_index + 1] + 1
        result = ""

        # Build the result string based on the pattern
        for position in range(pattern_length + 1):
            if position < pattern_length and pattern[position] == "I":
                # If 'I', assign the next maximum digit and append it to the
                # result
                max_so_far += 1
                result += str(max_so_far)

                # Update the max digit encountered so far
                max_so_far = max(max_so_far, curr_max)
                # Reset current max for the next iteration
                curr_max = 0

            else:
                # If 'D', calculate the appropriate digit and append it to the
                # result
                temp = 1 + max_so_far + arr_D[position]
                result += str(temp)

                # Update the current max value
                curr_max = max(curr_max, temp)

        return result
