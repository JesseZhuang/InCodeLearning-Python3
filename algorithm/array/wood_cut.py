"""lint code 183, hard, see leet code 1011"""

from typing import (
    List,
)


class Solution:
    """
    @param l: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    def wood_cut(self, l: List[int], k: int) -> int:

        def check(mid: int) -> bool:
            cnt = 0
            for l1 in l: cnt += l1 // mid
            return cnt >= k

        left, res = 1, 0
        r = max(l) if l else 0
        while left <= r:
            mid = left + (r - left) // 2
            if check(mid):
                res = mid
                left = mid + 1
            else:
                r = mid - 1
        return res
