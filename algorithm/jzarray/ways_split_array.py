"""leet 2270, medium"""


class Solution:
    """todo editorial"""

    def waysToSplitArray(self, nums: list[int]) -> int:
        # Keep track of sum of elements on left and right sides
        left_sum = right_sum = 0

        # Initially all elements are on right side
        right_sum = sum(nums)

        # Try each possible split position
        count = 0
        for i in range(len(nums) - 1):
            # Move current element from right to left side
            left_sum += nums[i]
            right_sum -= nums[i]

            # Check if this creates a valid split
            if left_sum >= right_sum:
                count += 1

        return count
