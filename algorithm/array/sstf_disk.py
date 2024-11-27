"""
shortest seek time first disk seek algorithm
allow stream of inputs, duplicate
"""
from sortedcontainers import SortedList


class SSTFDisk:
    def __init__(self, start: int):
        self.s = start
        self.pl = SortedList()

    def add(self, positions: list[int]):
        """add positions to queue"""
        self.pl.update(positions)

    def next(self) -> int:
        """next position to seek"""
        if not self.pl:
            raise RuntimeError('no more positions to seek')
        idx = self.pl.bisect_right(self.s)
        if idx == 0:
            self.s = self.pl[0]
        elif idx == len(self.pl):
            self.s = self.pl[-1]
        else:
            dl, dr = self.s - self.pl[idx - 1], self.pl[idx] - self.s
            if dl == dr:  # pick the side has fewer tasks at the moment, may not be the requirement
                nl, nr = idx, len(self.pl) - idx
                self.s = self.pl[idx - 1] if nl < nr else self.pl[idx]
            elif dl > dr:
                self.s = self.pl[idx]
            else:
                self.s = self.pl[idx - 1]
        self.pl.remove(self.s)
        return self.s
