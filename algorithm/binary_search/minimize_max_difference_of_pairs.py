class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        """Sort + Binary search on answer + Greedy. O(n log n + n log M) time, O(1) space.
        M = max(nums) - min(nums)."""
        if p == 0:
            return 0
        nums.sort()  # O(n log n)
        n = len(nums)

        def can_form(threshold: int) -> bool:
            count, i = 0, 0
            while i < n - 1:  # O(n) greedy scan
                if nums[i + 1] - nums[i] <= threshold:
                    count += 1
                    i += 2  # use both elements in a pair
                else:
                    i += 1
                if count >= p:
                    return True
            return count >= p

        lo, hi = 0, nums[-1] - nums[0]  # O(log M) search range
        while lo < hi:
            mid = (lo + hi) // 2
            if can_form(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
