"""LeetCode 1748: Sum of Unique Elements."""


class Solution:
    def sumOfUnique(self, nums):
        # Counting takes O(n) time; the 101-slot scan is O(U), with U = 101.
        frequencies = [0] * 101
        for number in nums:
            frequencies[number] += 1

        total = 0
        for value, frequency in enumerate(frequencies):
            if frequency == 1:
                total += value
        # Overall: O(n + U) time and O(U) space; U is fixed by the constraints.
        return total

    def sumOfUniqueBySorting(self, nums):
        # Sorting is O(n log n) time and the copy uses O(n) space.
        ordered = sorted(nums)
        total = 0
        start = 0

        # Group scanning is O(n) overall because each value is visited once.
        while start < len(ordered):
            end = start + 1
            while end < len(ordered) and ordered[end] == ordered[start]:
                end += 1
            if end - start == 1:
                total += ordered[start]
            start = end

        return total
