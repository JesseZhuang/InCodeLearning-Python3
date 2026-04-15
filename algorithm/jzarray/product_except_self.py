"""leet code 238, medium, tags: array, prefix sum."""


class Solution:
    """O(n) time, O(1) extra space (output array not counted)."""

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        prefix = 1
        for i in range(n):  # O(n) build prefix products into res
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):  # O(n) multiply suffix products
            res[i] *= suffix
            suffix *= nums[i]
        return res


class Solution2:
    """O(n) time, O(n) space with separate prefix and suffix arrays."""

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [1] * n  # O(n) space
        suffix = [1] * n  # O(n) space
        for i in range(1, n):  # O(n)
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):  # O(n)
            suffix[i] = suffix[i + 1] * nums[i + 1]
        return [prefix[i] * suffix[i] for i in range(n)]  # O(n)
