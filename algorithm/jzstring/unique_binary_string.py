"""leet 1980, medium"""


class Solution:
    """todo editorial"""

    def findDifferentBinaryString(self, nums: list[str]) -> str:
        ans = []
        for i in range(len(nums)):
            curr = nums[i][i]
            ans.append("1" if curr == "0" else "0")

        return "".join(ans)
