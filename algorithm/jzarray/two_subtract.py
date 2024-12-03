"""
companies: salesforce
"""
from collections import Counter


def two_subtract(A: list[int], T: int) -> int:
    """todo similar, gfg count all pairs with absolution diff, leet 532"""
    cnt, res = Counter(A), 0
    for v in cnt:
        look = v + T
        if look not in cnt: continue
        res += cnt[look] * cnt[v]
    return res
