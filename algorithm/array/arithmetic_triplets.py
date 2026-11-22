class Solution:
    def arithmeticTriplets(self, nums, diff):
        values = set(nums)  # O(n) space for average O(1) membership checks.
        count = 0
        for value in nums:  # O(n) expected time; each value is checked once.
            if value + diff in values and value + 2 * diff in values:
                count += 1
        return count
