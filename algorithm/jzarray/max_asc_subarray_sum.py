"""leet 1800, easy"""


class Solution:
    """todo editorial"""

    def maxAscendingSum(self, nums: list[int]) -> int:
        maxSum = 0
        currentSubarraySum = nums[0]

        # Loop through the list starting from the second element
        for currentIdx in range(1, len(nums)):
            if nums[currentIdx] <= nums[currentIdx - 1]:
                # If the current element is not greater than the previous one,
                # update maxSum
                maxSum = max(maxSum, currentSubarraySum)
                # Reset the sum for the next ascending subarray
                currentSubarraySum = 0
            currentSubarraySum += nums[currentIdx]

        # Final check after the loop ends to account for the last ascending
        # subarray
        return max(maxSum, currentSubarraySum)
