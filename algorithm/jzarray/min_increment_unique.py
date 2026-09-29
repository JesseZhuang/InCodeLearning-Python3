"""LeetCode 945 Minimum Increment to Make Array Unique"""


class Solution:
    """Sort + Greedy. O(n log n) time, O(sort) space.

    Sort the array. Scan left to right. If current <= previous,
    increment current to previous + 1, accumulate the cost.
    """

    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()  # O(n log n)
        res = 0
        for i in range(1, len(nums)):  # O(n)
            if nums[i] <= nums[i - 1]:
                target = nums[i - 1] + 1
                res += target - nums[i]
                nums[i] = target
        return res


class Solution2:
    """Counting sort. O(n + max_val) time, O(n + max_val) space.

    Count frequencies and sweep forward. When a slot has count > 1,
    push count - 1 to the next slot.
    """

    def minIncrementForUnique(self, nums: list[int]) -> int:
        if not nums:
            return 0
        max_val = max(nums) + len(nums)  # upper bound after pushes
        count = [0] * (max_val + 1)
        for v in nums:  # O(n)
            count[v] += 1
        res = 0
        for i in range(max_val):  # O(n + max_val)
            if count[i] > 1:
                extra = count[i] - 1
                count[i + 1] += extra
                res += extra
        return res
