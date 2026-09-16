class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        """Sliding window. O(n) time, O(1) space."""
        mx = max(nums)
        res, cnt, left = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == mx:
                cnt += 1
            while cnt >= k:
                if nums[left] == mx:
                    cnt -= 1
                left += 1
            res += left  # all starting indices [0, left) form valid subarrays ending at right
        return res


class Solution2:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        """Binary search on prefix count. O(n log n) time, O(n) space."""
        from bisect import bisect_left
        mx = max(nums)
        positions = [i for i, v in enumerate(nums) if v == mx]
        res = 0
        for right in range(len(nums)):
            idx = bisect_left(positions, right + 1)  # how many max elements in [0, right]
            if idx >= k:
                res += positions[idx - k] + 1  # earliest start so that [start, right] has >= k max elements
        return res
