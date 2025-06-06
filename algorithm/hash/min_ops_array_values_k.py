"""leet 3375, easy"""


class Solution:
    """badly written question, 69 ms, 17.9 mb"""

    def minOperations(self, nums: list[int], k: int) -> int:
        st = set()
        for x in nums:
            if x < k:
                return -1
            elif x > k:
                st.add(x)
        return len(st)
