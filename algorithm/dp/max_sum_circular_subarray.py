class Solution:
    """918. Maximum Sum Circular Subarray https://leetcode.com/problems/maximum-sum-circular-subarray/"""

    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        """Kadane's for max and min subarrays. O(n) time, O(1) space."""
        total = 0
        max_sum = cur_max = nums[0]
        min_sum = cur_min = nums[0]
        total = nums[0]
        for i in range(1, len(nums)):  # O(n)
            x = nums[i]
            cur_max = max(x, cur_max + x)
            max_sum = max(max_sum, cur_max)
            cur_min = min(x, cur_min + x)
            min_sum = min(min_sum, cur_min)
            total += x
        # If all elements are negative, max_sum is the answer (largest single element).
        if total == min_sum:
            return max_sum
        return max(max_sum, total - min_sum)


class Solution2:
    """918. Maximum Sum Circular Subarray - Monotonic Deque approach."""

    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        """Prefix sum + monotonic deque. O(n) time, O(n) space."""
        from collections import deque
        n = len(nums)
        # Build prefix sum for doubled array, but only need length 2n.
        prefix = [0] * (2 * n + 1)
        for i in range(2 * n):  # O(n)
            prefix[i + 1] = prefix[i] + nums[i % n]
        res = nums[0]
        dq = deque([0])  # O(n) space for the deque
        for j in range(1, 2 * n + 1):  # O(n)
            # Remove indices out of window of size n.
            while dq and dq[0] < j - n:
                dq.popleft()
            res = max(res, prefix[j] - prefix[dq[0]])
            # Maintain increasing deque of prefix sums.
            while dq and prefix[dq[-1]] >= prefix[j]:
                dq.pop()
            dq.append(j)
        return res
