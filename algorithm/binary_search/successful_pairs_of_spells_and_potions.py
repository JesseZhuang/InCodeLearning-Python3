from bisect import bisect_left


class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        """Sort + Binary search. O((m+n) log n) time, O(n) space for sorted potions copy.
        For each spell, binary search the smallest potion that forms a successful pair."""
        potions.sort()  # O(n log n)
        n = len(potions)
        res = []
        for spell in spells:  # O(m) iterations
            # need spell * potion >= success, i.e., potion >= ceil(success / spell)
            min_potion = (success + spell - 1) // spell  # ceiling division
            idx = bisect_left(potions, min_potion)  # O(log n)
            res.append(n - idx)
        return res
