"""leet 1760, medium"""


class Solution:
    """todo editorial, 890 ms, 29.6 mb"""

    def minimumSize(self, nums, max_operations):
        # Binary search bounds
        left = 1
        right = max(nums)

        # Perform binary search to find the optimal max_balls_in_bag
        while left < right:
            middle = (left + right) // 2

            # Check if a valid distribution is possible with the current middle value
            if self._is_possible(middle, nums, max_operations):
                # If possible, try a smaller value (shift right to middle)
                right = middle
            else:
                # If not possible, try a larger value (shift left to middle + 1)
                left = middle + 1

        # Return the smallest possible value for max_balls_in_bag
        return left

    # Helper function to check if a distribution is possible for a given max_balls_in_bag
    def _is_possible(self, max_balls_in_bag, nums, max_operations):
        total_operations = 0

        # Iterate through each bag in the array
        for num in nums:
            # Calculate the number of operations needed to split this bag
            operations = math.ceil(num / max_balls_in_bag) - 1
            total_operations += operations

            # If total operations exceed max_operations, return False
            if total_operations > max_operations:
                return False

        # We can split the balls within the allowed operations, return True
        return True
