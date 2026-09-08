"""leet 1004, medium, tags: array, binary search, sliding window, prefix sum."""


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        """sliding window, O(n) time, O(1) space."""
        left, zeros = 0, 0
        res = 0
        for right in range(len(nums)):  # O(n)
            if nums[right] == 0:
                zeros += 1
            while zeros > k:  # O(1) amortized, left moves at most n total
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right - left + 1)
        return res


class Solution2:
    def longestOnes(self, nums: list[int], k: int) -> int:
        """binary search + prefix sum, O(n log n) time, O(n) space."""
        n = len(nums)
        # prefix[i] = number of zeros in nums[0..i)
        prefix = [0] * (n + 1)
        for i in range(n):  # O(n)
            prefix[i + 1] = prefix[i] + (1 if nums[i] == 0 else 0)

        def feasible(size: int) -> bool:
            """check if any window of `size` has at most k zeros."""
            for i in range(size, n + 1):  # O(n)
                zeros_in_window = prefix[i] - prefix[i - size]
                if zeros_in_window <= k:
                    return True
            return False

        lo, hi = 0, n  # O(log n) binary search on answer
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
