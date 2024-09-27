"""leet code 729, medium"""
from sortedcontainers import SortedDict


class MyCalendar:
    """202ms, 18.01mb"""
    __slots__ = "calendar"

    def __init__(self):
        self.calendar = SortedDict()

    def book(self, start: int, end: int) -> bool:
        c = self.calendar
        prev, nex = c.bisect_right(start), c.bisect_left(start)  # bisect returns index in [0,len]
        if (prev > 0 and c.peekitem(prev - 1)[1] > start) or \
                (nex < len(c) and end > c.peekitem(nex)[0]): return False
        c[start] = end
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
