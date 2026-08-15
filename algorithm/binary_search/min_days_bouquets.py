class Solution:
    def minDays(self, bloom_day: list[int], m: int, k: int) -> int:
        """Binary search on answer. O(n * log(max_day)) time, O(1) space."""
        n = len(bloom_day)
        if m * k > n:  # impossible
            return -1

        def can_make(days: int) -> bool:
            bouquets, flowers = 0, 0
            for d in bloom_day:  # O(n)
                if d <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m

        lo, hi = min(bloom_day), max(bloom_day)  # O(n)
        while lo <= hi:  # O(log(max_day))
            mid = (lo + hi) // 2
            if can_make(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
