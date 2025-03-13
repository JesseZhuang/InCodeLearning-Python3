"""leet 3151, easy"""


class Solution:
    """todo editorial"""

    def isArraySpecial(self, nums):
        # Iterate through indexes 0 to n - 1
        for index in range(len(nums) - 1):

            # Compare the parities using bitwise operations
            if ((nums[index] & 1) ^ (nums[index + 1] & 1)) == 0:
                # If the two adjacent numbers have the same parity, return False
                return False

        # Return True if no pair of adjacent numbers with the same parity are found
        return True
