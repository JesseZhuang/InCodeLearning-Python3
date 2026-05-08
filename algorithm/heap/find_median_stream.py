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


class MedianFinderSorted:
    '''Using SortedList (balanced BST). O(log n) add, O(1) find median.'''

    def __init__(self):
        from sortedcontainers import SortedList
        self.sl = SortedList()

    def addNum(self, num: int) -> None:
        self.sl.add(num)  # O(log n)

    def findMedian(self) -> float:
        n = len(self.sl)
        mid = n // 2
        if n % 2 == 1:
            return self.sl[mid]  # O(1) index access
        else:
            return (self.sl[mid - 1] + self.sl[mid]) / 2.0
