"""leet 2683 medium"""


class Solution:
    """todo editorial"""

    def doesValidArrayExist(self, derived: list[int]) -> bool:
        return sum(derived) % 2 == 0
