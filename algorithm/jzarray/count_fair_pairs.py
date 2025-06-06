"""leet 2563, medium"""


class Solution:
    """todo editorial"""

    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.lower_bound(nums, upper + 1) - self.lower_bound(nums, lower)

    # Calculate the number of pairs with sum less than `value`.
    def lower_bound(self, nums: list[int], value: int) -> int:
        left = 0
        right = len(nums) - 1
        result = 0
        while left < right:
            sum = nums[left] + nums[right]
            # If sum is less than value, add the size of window to result and move to the
            # next index.
            if sum < value:
                result += right - left
                left += 1
            else:
                # Otherwise, shift the right pointer backwards, until we get a valid window.
                right -= 1
        return result
