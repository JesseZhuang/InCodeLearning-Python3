"""
leet 1 variation
companies: salesforce
"""
from collections import defaultdict


def two_sum_print(nums, target):
    cnt = defaultdict(int)
    for n in nums:
        look = target - n
        if look in cnt:
            for i in range(cnt[look]): print(look, n)
        cnt[n] += 1
