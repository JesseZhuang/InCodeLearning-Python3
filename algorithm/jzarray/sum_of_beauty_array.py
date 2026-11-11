class Solution:

    def sumOfBeauties(self, nums):
        n = len(nums)
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]

        # Build suffix minima in O(n) time using O(n) extra space.
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        total_beauty = 0
        left_max = nums[0]
        # Each inner index is checked once, so this pass is O(n) time.
        for i in range(1, n - 1):
            if left_max < nums[i] < suffix_min[i + 1]:
                total_beauty += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                total_beauty += 1
            left_max = max(left_max, nums[i])

        return total_beauty
