from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """Cyclic sort. Place each value v in [1, n] at index v-1."""
        n = len(nums)
        i = 0
        while i < n:  # O(n) total swaps since each element moves to its final position at most once
            v = nums[i]
            if 1 <= v <= n and nums[v - 1] != v:
                nums[i], nums[v - 1] = nums[v - 1], v  # O(1) space, in-place swap
            else:
                i += 1
        for i in range(n):  # O(n)
            if nums[i] != i + 1:
                return i + 1
        return n + 1

    def firstMissingPositive2(self, nums: List[int]) -> int:
        """Index marking with negation. Uses the array itself as a hash set."""
        n = len(nums)
        # Step 1: replace non-positive and >n values with n+1 (a sentinel)
        for i in range(n):  # O(n)
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        # Step 2: for each value v in [1,n], mark index v-1 as negative
        for i in range(n):  # O(n)
            v = abs(nums[i])
            if v <= n:
                nums[v - 1] = -abs(nums[v - 1])  # O(1) space
        # Step 3: first positive index means that index+1 is missing
        for i in range(n):  # O(n)
            if nums[i] > 0:
                return i + 1
        return n + 1
