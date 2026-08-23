class Solution:
    """LeetCode 740 Delete and Earn - DP (House Robber on frequency array)"""

    def deleteAndEarn(self, nums: list[int]) -> int:
        max_val = max(nums)
        earn = [0] * (max_val + 1)  # O(max_val) space
        for n in nums:  # O(n)
            earn[n] += n
        # House Robber on earn array: can't pick adjacent values
        prev, curr = 0, 0
        for i in range(1, max_val + 1):  # O(max_val)
            prev, curr = curr, max(curr, prev + earn[i])
        return curr


class Solution2:
    """LeetCode 740 Delete and Earn - Sort + Group DP"""

    def deleteAndEarn(self, nums: list[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        vals = sorted(count.keys())  # O(k log k) where k = distinct values
        prev, curr = 0, 0
        for i, v in enumerate(vals):  # O(k)
            points = v * count[v]
            if i > 0 and vals[i - 1] == v - 1:
                prev, curr = curr, max(curr, prev + points)
            else:
                prev, curr = curr, curr + points
        return curr
