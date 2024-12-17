"""leet 2593, medium"""


class Solution:
    """todo editorial"""

    def findScore(self, nums: list[int]) -> int:
        ans = 0
        sorted = [(num, idx) for idx, num in enumerate(nums)]
        sorted.sort()
        marked = [False] * len(nums)

        for i in range(len(nums)):
            number = sorted[i][0]
            index = sorted[i][1]
            if not marked[index]:
                ans += number
                marked[index] = True
                # mark adjacent elements if they exist
                if index - 1 >= 0:
                    marked[index - 1] = True
                if index + 1 < len(nums):
                    marked[index + 1] = True

        return ans
