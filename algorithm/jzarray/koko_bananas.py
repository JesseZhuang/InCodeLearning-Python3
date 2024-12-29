"""leet 875, medium"""


class Solution:
    """135 ms, 18.8 mb"""

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def feasible(speed) -> bool:
            return sum((p - 1) // speed + 1 for p in piles) <= h

        l, r = 1, max(piles)
        while l < r:
            mid = l + (r - l) // 2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l
