from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        """Prefix sum with hashmap. Count prefix sums where current - goal was seen before."""
        count = 0
        prefix = 0
        freq = defaultdict(int)
        freq[0] = 1  # O(n) space
        for num in nums:  # O(n)
            prefix += num
            count += freq[prefix - goal]
            freq[prefix] += 1
        return count


class Solution2:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        """Sliding window: exactly(goal) = atMost(goal) - atMost(goal - 1). O(1) space."""
        def at_most(k: int) -> int:
            if k < 0:
                return 0
            res = 0
            left = 0
            cur = 0
            for right in range(len(nums)):  # O(n)
                cur += nums[right]
                while cur > k:  # each element enters/leaves at most once, O(n) total
                    cur -= nums[left]
                    left += 1
                res += right - left + 1
            return res

        return at_most(goal) - at_most(goal - 1)
