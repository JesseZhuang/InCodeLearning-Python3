"""leet 2116, medium"""


class Solution:
    """todo editorial"""

    def canBeValid(self, s: str, locked: str) -> bool:
        length = len(s)
        # If length of string is odd, return false.
        if length % 2 == 1:
            return False
        open_brackets = 0
        unlocked_count = 0
        # Iterate through the string to handle '(' and ')'.
        for i in range(length):
            if locked[i] == "0":
                unlocked_count += 1
            elif s[i] == "(":
                open_brackets += 1
            elif s[i] == ")":
                if open_brackets > 0:
                    open_brackets -= 1
                elif unlocked_count > 0:
                    unlocked_count -= 1
                else:
                    return False

        # Match remaining open brackets with unlocked characters.
        balance_count = 0
        for i in range(length - 1, -1, -1):
            if locked[i] == "0":
                balance_count -= 1
                unlocked_count -= 1
            elif s[i] == "(":
                balance_count += 1
                open_brackets -= 1
            elif s[i] == ")":
                balance_count -= 1
            if balance_count > 0:
                return False
            if unlocked_count == 0 and open_brackets == 0:
                break

        if open_brackets > 0:
            return False

        return True
