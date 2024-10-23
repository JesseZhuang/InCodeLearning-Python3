"""leet code 900, medium"""
from bisect import bisect_left
from typing import List


class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.sum_cnt, self.num = list(), list()
        self.cur, self.low = 0, 0
        i, sum = 0, 0
        while i < len(encoding):
            c, num = encoding[i], encoding[i + 1]
            i += 2
            if c == 0:
                continue
            sum += c
            self.sum_cnt.append(sum)
            self.num.append(num)

    def next(self, n: int) -> int:
        self.cur += n
        i = bisect_left(self.sum_cnt, self.cur)
        return self.num[i] if i < len(self.num) else -1

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
