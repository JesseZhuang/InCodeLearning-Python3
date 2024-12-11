"""leet 810, lint 1007, hard"""
import operator
from functools import reduce


class Solution(object):
    """todo editorial, 41 ms, 17.37 mb"""

    def xorGame(self, nums):
        return reduce(operator.xor, nums) == 0 or len(nums) % 2 == 0
