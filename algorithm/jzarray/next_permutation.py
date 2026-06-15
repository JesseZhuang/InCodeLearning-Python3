"""31. Next Permutation https://leetcode.com/problems/next-permutation/"""


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """Modify nums in-place to the next lexicographically greater permutation."""
        n = len(nums)
        # Step 1: find pivot — rightmost element smaller than its successor, O(n)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            # Step 2: find rightmost element larger than pivot, O(n)
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # Step 3: reverse suffix after pivot position, O(n)
        # Total: O(n) time, O(1) space
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
