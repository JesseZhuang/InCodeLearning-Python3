class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1

        left = 0
        window_sum = 0
        longest = -1
        # O(n) time: each index enters and leaves the window once; O(1) extra space.
        for right, value in enumerate(nums):
            window_sum += value
            while window_sum > target:
                window_sum -= nums[left]
                left += 1
            if window_sum == target:
                longest = max(longest, right - left + 1)

        return -1 if longest < 0 else len(nums) - longest


class Solution2:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1

        earliest_index = {0: -1}
        prefix_sum = 0
        longest = 0 if target == 0 else -1
        # O(n) time and O(n) extra space for the earliest index of each prefix sum.
        for index, value in enumerate(nums):
            prefix_sum += value
            needed = prefix_sum - target
            if needed in earliest_index:
                longest = max(longest, index - earliest_index[needed])
            earliest_index.setdefault(prefix_sum, index)

        return -1 if longest < 0 else len(nums) - longest
