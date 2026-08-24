class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        """Binary search on answer + greedy feasibility check.
        O(n * log(sum - max)) time, O(1) space."""

        def feasible(capacity: int) -> bool:
            day_count, cur = 1, 0
            for w in weights:  # O(n)
                if cur + w > capacity:
                    day_count += 1
                    if day_count > days:
                        return False
                    cur = 0
                cur += w
            return True

        lo, hi = max(weights), sum(weights)  # O(n)
        while lo < hi:  # O(log(sum - max))
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
