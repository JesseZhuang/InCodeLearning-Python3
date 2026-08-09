class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        """Binary search on answer. O(n * log(sum-max)) time, O(1) space."""

        def can_split(target: int) -> bool:
            count, total = 1, 0
            for num in nums:  # O(n)
                total += num
                if total > target:
                    total = num
                    count += 1
                    if count > k:
                        return False
            return True

        lo, hi = max(nums), sum(nums)  # O(n)
        while lo <= hi:  # O(log(sum-max))
            mid = (lo + hi) // 2
            if can_split(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

    def splitArray2(self, nums: list[int], k: int) -> int:
        """DP. O(n^2 * k) time, O(n * k) space."""
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):  # O(n)
            prefix[i + 1] = prefix[i] + nums[i]
        # dp[i][j] = min largest sum splitting nums[0:i] into j parts
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]  # O(n*k) space
        dp[0][0] = 0
        for i in range(1, n + 1):  # O(n)
            for j in range(1, min(i, k) + 1):  # O(k)
                for m in range(j - 1, i):  # O(n), last part is nums[m:i]
                    dp[i][j] = min(dp[i][j], max(dp[m][j - 1], prefix[i] - prefix[m]))
        return dp[n][k]
