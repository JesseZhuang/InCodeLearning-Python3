"""leet code 1011, medium"""
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_w, sum_w = 0, 0
        for w in weights:
            max_w = max(w, max_w)
            sum_w += w
        l, r = max_w, sum_w

        def check(mid):
            cnt, cur = 1, 0
            for w in weights:
                if cur + w > mid:
                    cnt += 1
                    if cnt > days: break
                    cur = 0
                cur += w
            return cnt <= days

        res = l
        while l <= r:
            mid = l + (r - l) // 2
            if check(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res


class Solution2:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """199ms, 22.28Mb"""
        max_w, sum_w = 0, 0
        for w in weights:
            if w > max_w:
                max_w = w
            sum_w += w
        lo, hi = max_w, sum_w
        while lo < hi:
            mid = lo + (hi - lo) // 2
            count, cur = 1, 0
            for w in weights:
                if cur + w > mid:
                    count += 1
                    if count > days:
                        break
                    cur = 0
                cur += w
            if count > days:
                lo = mid + 1
            else:
                hi = mid
        return lo
