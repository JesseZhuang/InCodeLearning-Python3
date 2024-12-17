"""leet 2762, medium"""


class Solution:
    """two pointers, todo editorial"""

    def continuousSubarrays(self, nums: list[int]) -> int:
        right = left = 0
        window_len = total = 0

        # Initialize window with first element
        cur_min = cur_max = nums[right]

        for right in range(len(nums)):
            # Update min and max for current window
            cur_min = min(cur_min, nums[right])
            cur_max = max(cur_max, nums[right])

            # If window condition breaks (diff > 2)
            if cur_max - cur_min > 2:
                # Add subarrays from previous valid window
                window_len = right - left
                total += window_len * (window_len + 1) // 2

                # Start new window at current position
                left = right
                cur_min = cur_max = nums[right]

                # Expand left boundary while maintaining condition
                while left > 0 and abs(nums[right] - nums[left - 1]) <= 2:
                    left -= 1
                    cur_min = min(cur_min, nums[left])
                    cur_max = max(cur_max, nums[left])

                # Remove overcounted subarrays if left boundary expanded
                if left < right:
                    window_len = right - left
                    total -= window_len * (window_len + 1) // 2

        # Add subarrays from final window
        window_len = right - left + 1
        total += window_len * (window_len + 1) // 2

        return total
