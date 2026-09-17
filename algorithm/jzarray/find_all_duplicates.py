"""442. Find All Duplicates in an Array"""


class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        """Negation marking.

        For each value v, negate nums[v-1] as a visited flag.
        If nums[v-1] is already negative, v is a duplicate.
        """
        result = []
        for num in nums:  # O(n)
            idx = abs(num) - 1  # O(1) map value to index
            if nums[idx] < 0:
                result.append(abs(num))
            else:
                nums[idx] = -nums[idx]
        return result  # O(n) time, O(1) space (output excluded)


class Solution2:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        """Cyclic sort.

        Place each value at its correct index (value v at index v-1).
        After sorting, any position where nums[i] != i+1 holds a duplicate.
        """
        n = len(nums)
        i = 0
        while i < n:  # O(n) total swaps, each element placed at most once
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]  # O(1) swap
            else:
                i += 1

        return [nums[i] for i in range(n) if nums[i] != i + 1]  # O(n) scan
        # O(n) time, O(1) space (output excluded)
