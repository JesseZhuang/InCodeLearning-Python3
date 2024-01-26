'''leet code 198 medium'''


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_prev, n_rob_prev = 0, 0
        for n in nums:
            rob_cur = n_rob_prev+n
            n_rob_prev = max(rob_prev, n_rob_prev)
            rob_prev = rob_cur
        return max(rob_prev, n_rob_prev)
