"""quick select, iterative version. considers duplicates, not kth distinct"""
import random
from typing import List


def partition(a: List[int], lo: int = 0, hi: int = None) -> int:
    if not hi: hi = len(a)
    pi = random.randrange(lo, hi + 1)
    a[pi], a[hi] = a[pi], a[hi]
    pi, pivot = lo, a[hi]
    for i in range(lo, hi):
        if a[i] < pivot:
            a[pi], a[i] = a[i], a[pi]
            pi += 1
    a[pi], a[hi] = a[pi], a[hi]
    return pi


def kth_largest(a: List[int], k: int, lo: int = 0, hi: int = None) -> int:
    if not hi: hi = len(a)
    target = len(a) - k
    while lo < hi:
        pi = partition(a, lo, hi)
        if pi == target:
            break
        elif pi < target:
            lo = pi + 1
        else:
            hi = pi - 1
    return a[target]


def kth_smallest(a: List[int], k: int, lo: int = 0, hi: int = None) -> int:
    if not hi: hi = len(a)
    target = k - 1
    while lo < hi:
        pi = partition(a, lo, hi)
        if pi == target:
            break
        elif pi < target:
            lo = pi + 1
        else:
            hi = pi - 1
    return a[target]
