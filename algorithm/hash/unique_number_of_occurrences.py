from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        # O(n) time and O(n) space.
        occurrences = Counter(arr)
        return len(occurrences) == len(set(occurrences.values()))

    def uniqueOccurrencesByFrequencyArray(self, arr: list[int]) -> bool:
        # O(n + U) time and space, where U is the bounded value range.
        frequencies = [0] * 2001
        for number in arr:
            frequencies[number + 1000] += 1

        used_frequencies = [False] * (len(arr) + 1)
        for frequency in frequencies:
            if frequency == 0:
                continue
            if used_frequencies[frequency]:
                return False
            used_frequencies[frequency] = True
        return True
