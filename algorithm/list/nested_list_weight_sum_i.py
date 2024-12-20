# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from typing import Self


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self) -> int | None:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self) -> list[Self] | None:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class Solution:
    """780 ms, 7.28 mb"""

    def depthSum(self, nil: list[NestedInteger]) -> int:
        # nil: nested integer list, d: depth
        def dfs(nil: list[NestedInteger], d):
            res = 0
            for i in nil:
                if i.isInteger():
                    res += i.getInteger() * d
                else:
                    res += dfs(i.getList(), d + 1)
            return res

        return dfs(nil, 1)
