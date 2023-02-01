'''
lintcode 1250, leetcode 414
no constraints that the integers are positive
'''

from sortedcontainers import SortedSet


class ThirdMax:

    def third_max(self, nums: list[int]) -> int:
        '''third max or max'''
        s = SortedSet()
        for n in nums:
            s.add(n)
            if len(s) > 3:
                s.pop(0)
        return s[0] if len(s) == 3 else s[-1]
