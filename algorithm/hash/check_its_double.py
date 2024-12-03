"""leet 1346, easy"""


class Solution:
    """0 ms, 17.2 mb"""

    def checkIfExist(self, arr: list[int]) -> bool:
        seen = set()
        for n in arr:
            if 2 * n in seen or (n % 2 == 0 and n // 2 in seen):
                return True
            seen.add(n)
        return False
