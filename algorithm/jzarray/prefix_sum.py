"""prefix sum, opposite of difference array"""
from typing import List


class PrefixSum:

    def __init__(self, nums: List[int]):
        """
        O(n) time
        :param nums: input array
        """
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(sums[i - 1] + nums[i])
        self.sums = sums

    def rsq(self, start: int, end: int) -> int:
        """
        range sum query, O(1) time
        :param start: left bound inclusive
        :param end: right bound inclusive
        :return: sum for [start,end]
        """
        if start == 0: return self.sums[end]
        return self.sums[end] - self.sums[start - 1]
