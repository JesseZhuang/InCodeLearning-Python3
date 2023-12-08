'''leet code 295, hard'''


from heapq import heappop, heappush


class MedianFinder:
    '''403ms, 38Mb.'''

    def __init__(self):
        self.left, self.right = [], []  # max, min heaps
        self.odd = False

    def addNum(self, num: int) -> None:
        if self.odd:
            heappush(self.right, num)
            heappush(self.left, -heappop(self.right))
        else:
            heappush(self.left, -num)
            heappush(self.right, -heappop(self.left))
        self.odd = not self.odd  # not !self.odd

    def findMedian(self) -> float:
        if self.odd:
            return self.right[0]
        else:
            return (-self.left[0] + self.right[0])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
