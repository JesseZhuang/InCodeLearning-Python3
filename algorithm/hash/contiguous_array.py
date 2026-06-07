class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        """Prefix sum with hashmap. Treat 0 as -1, track earliest index of each prefix sum."""
        prefix_map = {0: -1}  # O(n) space
        max_len = 0
        count = 0
        for i, num in enumerate(nums):  # O(n)
            count += 1 if num == 1 else -1
            if count in prefix_map:
                max_len = max(max_len, i - prefix_map[count])
            else:
                prefix_map[count] = i
        return max_len
