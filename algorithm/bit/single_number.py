class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """XOR cancels each paired value. Time O(n), extra space O(1)."""
        result = 0
        for value in nums:
            result ^= value
        return result


class Solution2:
    def singleNumber(self, nums: list[int]) -> int:
        """Toggle values in a set. Expected time O(n), extra space O(n)."""
        seen = set()
        for value in nums:
            if value in seen:
                seen.remove(value)
            else:
                seen.add(value)
        return next(iter(seen))
