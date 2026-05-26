"""287. Find the Duplicate Number"""


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """Floyd's cycle detection (tortoise and hare).

        Treat nums as a linked list where index i points to nums[i].
        Since there's a duplicate, a cycle must exist.
        """
        # Phase 1: find intersection point in cycle - O(n)
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]       # O(1) per step
            fast = nums[nums[fast]] # O(1) per step
            if slow == fast:
                break

        # Phase 2: find entrance to cycle - O(n)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow  # Total: O(n) time, O(1) space


class Solution2:
    def findDuplicate(self, nums: list[int]) -> int:
        """Binary search on value range.

        For a candidate mid, count numbers <= mid.
        If count > mid, duplicate is in [lo, mid].
        """
        lo, hi = 1, len(nums) - 1  # value range [1, n]
        while lo < hi:  # O(log n) iterations
            mid = (lo + hi) // 2
            # O(n) count per iteration
            count = sum(1 for x in nums if x <= mid)
            if count > mid:
                hi = mid
            else:
                lo = mid + 1

        return lo  # Total: O(n log n) time, O(1) space
