"""leet code 347, medium"""
from collections import Counter
from typing import List


class Solution1:
    """91ms, 22.1mb"""

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        cnt_nums = [[] for _ in range(len(nums) + 1)]
        for num in counts:
            cnt_nums[counts[num]].append(num)
        # return list(chain.from_iterable(buk))[-k:]
        res, j = [], 0
        for i in range(len(nums), 0, -1):
            for num in cnt_nums[i]:
                res.append(num)
                j += 1
                if j == k: return res
        return res


class Solution3:
    """apparently the question is not intended to use this library method"""

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x[0] for x in Counter(nums).most_common(k)]
