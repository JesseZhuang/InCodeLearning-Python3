"""leet code 3309, medium, weekly 418 Q1"""

from itertools import permutations
from typing import List


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        return max(int(''.join(bin(x)[2:] for x in p), 2) for p in permutations(nums))
