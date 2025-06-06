"""leet 1399, easy"""
from collections import Counter


class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashMap = Counter()
        for i in range(1, n + 1):
            key = sum([int(x) for x in str(i)])
            hashMap[key] += 1
        maxValue = max(hashMap.values())
        count = sum(1 for v in hashMap.values() if v == maxValue)
        return count
