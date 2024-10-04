from typing import List


class BITtree:
    """aka Fenwick tree"""

    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def __init__(self, arr: List[int]):
        l = len(arr) + 1
        self.tree = [0]
        for a in arr: self.tree.append(a)
        for i in range(1, l):
            p = i + (i & -i)
            if p < l: self.tree[p] += self.tree[i]

    def update(self, i: int, delta: int) -> None:
        i += 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i

    def getSum(self, i: int) -> int:
        i += 1
        res = 0
        while i:
            res += self.tree[i]
            i -= i & -i
        return res

    def rsq(self, lo: int, hi: int) -> int:
        return self.getSum(hi) - self.getSum(lo - 1)
