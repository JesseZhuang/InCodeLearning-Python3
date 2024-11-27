"""
companies: salesforce
"""
from collections import Counter


def two_subtract(A: list[int], T: int) -> int:
    cnt, res = Counter(A), 0
    for v in cnt:
        look = v + T
        if look not in cnt: continue
        res += cnt[look] * cnt[v]
    return res
