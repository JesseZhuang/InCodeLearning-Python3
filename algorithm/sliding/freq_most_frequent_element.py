"""leet 1838, medium, tags: array, binary search, greedy, sliding window, sorting, prefix sum."""


class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        """sliding window, O(n log n) time for sort, O(n) space."""
        nums.sort()  # O(n log n)
        res, window_sum, left = 1, 0, 0
        for right in range(len(nums)):  # O(n)
            window_sum += nums[right]
            # cost to make all elements in [left, right] equal to nums[right]
            while nums[right] * (right - left + 1) - window_sum > k:  # O(1) amortized
                window_sum -= nums[left]
                left += 1
            res = max(res, right - left + 1)
        return res


class Solution2:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        """binary search + prefix sum, O(n log n) time, O(n) space."""
        nums.sort()  # O(n log n)
        prefix = [0] * (len(nums) + 1)
        for i, v in enumerate(nums):  # O(n) prefix sum
            prefix[i + 1] = prefix[i] + v

        def can_make_freq(size: int) -> bool:
            """check if we can make any window of `size` elements all equal."""
            for i in range(size - 1, len(nums)):  # O(n) scan all windows of this size
                window_sum = prefix[i + 1] - prefix[i - size + 1]
                cost = nums[i] * size - window_sum
                if cost <= k:
                    return True
            return False

        lo, hi = 1, len(nums)  # O(log n) binary search
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_make_freq(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
