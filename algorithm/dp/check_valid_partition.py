"""LeetCode 2369: Check if There is a Valid Partition For The Array."""


class Solution:
    def validPartition(self, nums: list[int]) -> bool:
        """Rolling prefix DP: O(n) time and O(1) auxiliary space."""
        # Before processing length 3, these are dp[0], dp[1], dp[2].
        three_back, two_back, one_back = True, False, nums[0] == nums[1]
        for length in range(3, len(nums) + 1):  # O(n) constant-work transitions.
            a, b, c = nums[length - 3], nums[length - 2], nums[length - 1]
            pair = two_back and b == c
            triple = three_back and (a == b == c or (a + 1 == b and b + 1 == c))
            current = pair or triple
            three_back, two_back, one_back = two_back, one_back, current
        return one_back
