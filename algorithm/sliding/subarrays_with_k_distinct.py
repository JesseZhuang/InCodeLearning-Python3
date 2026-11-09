class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        """Count subarrays with exactly k distinct values in O(n) expected time and O(n) space."""
        return self._count_at_most_k(nums, k) - self._count_at_most_k(nums, k - 1)

    @staticmethod
    def _count_at_most_k(nums: list[int], k: int) -> int:
        if k == 0:
            return 0

        frequencies: dict[int, int] = {}
        left = 0
        total = 0

        for right, value in enumerate(nums):  # O(n) right-boundary advances
            frequencies[value] = frequencies.get(value, 0) + 1

            # Each left-boundary advance removes one item, so all shrinking is O(n) total.
            while len(frequencies) > k:
                left_value = nums[left]
                frequencies[left_value] -= 1
                if frequencies[left_value] == 0:
                    del frequencies[left_value]
                left += 1

            total += right - left + 1  # every start in [left, right] is valid

        return total
