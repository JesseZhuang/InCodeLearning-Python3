"""leet 2206, easy"""
from collections import Counter


class Solution:
    """todo editorial"""

    def divideArray(self, nums: list[int]) -> bool:
        # Count the frequency of each number using Counter
        frequency = Counter(nums)

        # Check if each number appears even number of times
        return all(count % 2 == 0 for count in frequency.values())
