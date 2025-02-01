"""leet 2425, medium"""


class Solution:
    """todo editorial"""

    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        # Initialize XOR results for both arrays
        xor1, xor2 = 0, 0

        # Get lengths of both arrays
        len1, len2 = len(nums1), len(nums2)

        # If nums2 length is odd, each element in nums1 appears odd times in final result
        if len2 % 2:
            for num in nums1:
                xor1 ^= num

        # If nums1 length is odd, each element in nums2 appears odd times in final result
        if len1 % 2:
            for num in nums2:
                xor2 ^= num

        # Return XOR of both results
        return xor1 ^ xor2
