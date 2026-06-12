"""LeetCode 380, medium, tags: array, hash table, math, design, randomized."""

import random


class RandomizedSet:
    """HashMap + ArrayList, swap-to-end removal.

    Each operation is average O(1) time, O(n) space for n elements stored.
    """

    def __init__(self):
        self.vals = []
        self.val_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_index:  # O(1) hash lookup
            return False
        self.val_index[val] = len(self.vals)
        self.vals.append(val)  # O(1) amortized append
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_index:  # O(1) hash lookup
            return False
        i = self.val_index[val]
        last = self.vals[-1]
        self.vals[i] = last  # O(1) swap last element into removed slot
        self.val_index[last] = i
        self.vals.pop()  # O(1) pop from end
        del self.val_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)  # O(1) random index access
