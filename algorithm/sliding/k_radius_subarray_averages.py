"""LeetCode 2090, medium: K Radius Subarray Averages."""


def _average_toward_zero(total: int, width: int) -> int:
    """Divide like Java/C++ integer division, truncating negative values toward zero."""
    return total // width if total >= 0 else -((-total) // width)


class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        width = 2 * k + 1
        averages = [-1] * n
        if width > n:
            return averages

        window_sum = sum(nums[:width])
        averages[k] = _average_toward_zero(window_sum, width)
        # O(n) time: each window update adds and removes one value.
        for right in range(width, n):
            window_sum += nums[right] - nums[right - width]
            averages[right - k] = _average_toward_zero(window_sum, width)

        return averages

    def getAveragesByPrefixSum(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        width = 2 * k + 1
        averages = [-1] * n
        if width > n:
            return averages

        prefix = [0] * (n + 1)
        # O(n) time to build prefixes; O(n) extra space for range-sum queries.
        for index, value in enumerate(nums):
            prefix[index + 1] = prefix[index] + value

        for center in range(k, n - k):
            window_sum = prefix[center + k + 1] - prefix[center - k]
            averages[center] = _average_toward_zero(window_sum, width)

        return averages
