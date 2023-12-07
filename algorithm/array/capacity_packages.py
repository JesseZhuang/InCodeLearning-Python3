'''leet code 1011, medium'''


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''554ms, 22.28Mb'''
        max_w, sum = 0, 0
        for w in weights:
            if w > max_w:
                max_w = w
            sum += w
        lo, hi = max_w, sum
        while lo < hi:
            mid = lo+(hi-lo)//2
            count, cur = 1, 0
            for w in weights:
                if cur+w > mid:
                    count += 1
                    if count > days:
                        break
                    cur = 0
                cur += w
            if count > days:
                lo = mid+1
            else:
                hi = mid
        return lo
