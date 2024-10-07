"""leet code 729, medium"""
from sortedcontainers import SortedDict


class MyCalendar:
    """202ms, 18.01mb"""
    __slots__ = "calendar"

    def __init__(self):
        self.calendar = SortedDict()

    def book(self, start: int, end: int) -> bool:
        c = self.calendar
        # floor bisect_right then -1, using bisect_left if -1, will miss equal; ceiling bisect_left, no need +1
        prev, nex = c.bisect_right(start) - 1, c.bisect_left(start)  # bisect returns index in [0,len]
        if (prev >= 0 and c.peekitem(prev)[1] > start) or \
                (nex < len(c) and end > c.peekitem(nex)[0]): return False
        c[start] = end
        return True


class MyCalendar2:

    def __init__(self):
        self.booked = SortedDict()

    def book(self, start: int, end: int) -> bool:
        b = self.booked
        nex = b.bisect_left(start)  # ceiling
        pre = nex - 1
        if (pre >= 0 and b.peekitem(pre)[1] > start) or \
                (nex < len(b) and b.peekitem(nex)[0] < end): return False
        b[start] = end
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
