"""leet 2560, medium"""


class Solution:
    """todo editorial"""

    def minCapability(self, nums, k):
        # Store the maximum nums value in maxReward.
        min_reward, max_reward = 1, max(nums)
        total_houses = len(nums)

        # Use binary search to find the minimum reward possible.
        while min_reward < max_reward:
            mid_reward = (min_reward + max_reward) // 2
            possible_thefts = 0

            index = 0
            while index < total_houses:
                if nums[index] <= mid_reward:
                    possible_thefts += 1
                    index += 2  # Skip the next house to maintain the non-adjacent condition
                else:
                    index += 1

            if possible_thefts >= k:
                max_reward = mid_reward
            else:
                min_reward = mid_reward + 1

        return min_reward
