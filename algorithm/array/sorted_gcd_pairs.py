"""leet code 3312, weekly 418 Q4"""
from bisect import bisect_right
from typing import List


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        m = max(nums)
        p = []
        cp = [False] * (m + 1)
        for i in range(2, m + 1):
            if cp[i] == False:
                p.append(i)
                for j in range(i, m + 1, i):
                    cp[j] = True
        count = [0] * (m + 1)
        for a in nums:
            count[a] += 1
        for pi in p:
            for j in range(m // pi, 0, -1):
                count[j] += count[j * pi]
        for i in range(m + 1):
            count[i] = count[i] * (count[i] - 1) // 2
        for pi in p:
            for j in range(0, m // pi + 1):
                count[j] -= count[j * pi]
        for i in range(1, m + 1):
            count[i] += count[i - 1]
        return [bisect_right(count, q) for q in queries]
