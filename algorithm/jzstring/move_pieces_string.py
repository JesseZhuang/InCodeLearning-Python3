"""leet 2337, medium"""


class Solution:
    """todo editorial, n, 1. 176 ms, 17.8 mb"""

    def canChange(self, start: str, target: str) -> bool:
        start_length = len(start)
        # pointers for start string and target string
        start_index, target_index = (0, 0)

        while start_index < start_length or target_index < start_length:
            # skip underscores in start
            while start_index < start_length and start[start_index] == "_":
                start_index += 1

            # skip underscores in target
            while target_index < start_length and target[target_index] == "_":
                target_index += 1

            # if one string exhausted, both strings should be exhausted
            if start_index == start_length or target_index == start_length:
                return (
                        start_index == start_length and target_index == start_length
                )

            # check if the pieces match and follow movement rules
            if (
                    start[start_index] != target[target_index]
                    or (start[start_index] == "L" and start_index < target_index)
                    or (start[start_index] == "R" and start_index > target_index)
            ):
                return False

            start_index += 1
            target_index += 1

        # if all conditions satisfied, return true
        return True
