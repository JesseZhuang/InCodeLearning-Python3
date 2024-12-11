"""leet 2779, medium"""


class Solution:
    """todo editorial"""

    def maximumBeauty(self, nums: list[int], k: int) -> int:
        # If there's only one element, the maximum beauty is 1
        if len(nums) == 1:
            return 1

        max_value = max(nums)  # Find the maximum value in nums
        count = [0] * (max_value + 1)  # Array to track count changes

        # Update the count array for the range [val - k, val + k]
        for num in nums:
            count[max(num - k, 0)] += 1  # Increment at the start of the range
            if num + k + 1 <= max_value:
                count[num + k + 1] -= 1  # Decrement after the range

        max_beauty = 0
        current_sum = 0  # Tracks the running sum of counts

        # Calculate the prefix sum and find the maximum beauty
        for val in count:
            current_sum += val
            max_beauty = max(max_beauty, current_sum)

        return max_beauty
