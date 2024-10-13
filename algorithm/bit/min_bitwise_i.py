"""biweeky 141 Q1 and Q2"""
from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            ans = -1
            for k in range(30, -1, -1):  # 10,-1,-1 for Q1, constraints nums[i] value
                mask = 1 << k
                if n & mask == 0: continue
                t = n ^ mask
                if t | (t + 1) == n:
                    ans = t
                    break
            res.append(ans)
        return res
