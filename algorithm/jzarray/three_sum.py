"""leet 15, medium, tags: array, two pointers, sorting."""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Sort + two pointers approach.

        Time O(n^2): sort O(n log n) + nested loop O(n^2).
        Space O(1) excluding output (sort is in-place).
        """
        nums.sort()  # O(n log n)
        res = []
        for i in range(len(nums) - 2):  # O(n) outer loop
            if nums[i] > 0:
                break  # remaining elements are all positive, no valid triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate for first element
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:  # O(n) two-pointer scan per i, total O(n^2)
                s = nums[i] + nums[lo] + nums[hi]
                if s < 0:
                    lo += 1
                elif s > 0:
                    hi -= 1
                else:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1  # skip duplicate for second element
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1  # skip duplicate for third element
        return res


class Solution2:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Hash set approach.

        Time O(n^2): for each element, scan remaining with a set lookup O(1).
        Space O(n) for the seen set.
        """
        nums.sort()  # O(n log n), needed only for deduplication of results
        res = []
        for i in range(len(nums) - 2):  # O(n) outer loop
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate for first element
            seen = set()  # O(n) space
            j = i + 1
            while j < len(nums):  # O(n) inner loop, total O(n^2)
                complement = -nums[i] - nums[j]
                if complement in seen:  # O(1) hash lookup
                    res.append([nums[i], complement, nums[j]])
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1  # skip duplicate for third element
                seen.add(nums[j])
                j += 1
        return res
