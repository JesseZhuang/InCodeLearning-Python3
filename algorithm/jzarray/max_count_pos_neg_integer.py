"""leet 2529, easy"""


class Solution:
    """todo editorial"""

    # Return the first index where the value is equal to or greater than zero.
    def lower_bound(self, nums):
        start, end = 0, len(nums) - 1
        index = len(nums)

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] < 0:
                start = mid + 1
            else:
                end = mid - 1
                index = mid

        return index

    # Return the first index where the value is greater than zero.
    def upper_bound(self, nums):
        start, end = 0, len(nums) - 1
        index = len(nums)

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] <= 0:
                start = mid + 1
            else:
                end = mid - 1
                index = mid

        return index

    def maximumCount(self, nums):
        # All integers from the first non-zero to last will be positive
        # integers.
        positiveCount = len(nums) - self.upper_bound(nums)
        # All integers from index 0 to index before the first zero index
        # will be negative.
        negativeCount = self.lower_bound(nums)

        return max(positiveCount, negativeCount)
