"""leet 2450 lint 3841 medium"""


class Solution:
    """81 ms, 5.32 mb, todo editorial"""

    def count_distinct_strings(self, s: str, k: int) -> int:
        return pow(2, len(s) - k + 1) % (10 ** 9 + 7)
