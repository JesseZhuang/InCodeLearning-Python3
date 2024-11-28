"""leet code 731, medium"""
from typing import List


class MyCalendarTwo:
    __slots__ = "booked", "d_booked"

    def __init__(self):
        self.booked = []
        self.d_booked = []

    def book(self, start: int, end: int) -> bool:

        def overlap(s: int, e: int) -> bool:
            return max(s, start) < min(end, e)

        def getOverlap(s: int, e: int) -> List[int]:
            return [max(s, start), min(e, end)]

        print("---\n", start, end)
        for s, e in self.d_booked:
            print("d", s, e)
            if overlap(s, e): return False
        for s, e in self.booked:
            print("s", s, e)
            if overlap(s, e): self.d_booked.append(getOverlap(s, e))
        self.booked.append([start, end])
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
