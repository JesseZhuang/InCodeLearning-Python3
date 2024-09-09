"""leet code 2402, hard"""
from heapq import heappop, heappush
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        used, unused, cnt = [], list(range(n)), [0] * n
        meetings.sort()  # sort by start time

        for start, end in meetings:
            while used and used[0][0] <= start:
                _, room = heappop(used)
                heappush(unused, room)
            if unused:
                room = heappop(unused)
                heappush(used, (end, room))
            else:
                release, room = heappop(used)
                heappush(used, (release + end - start, room))
            cnt[room] += 1

        return cnt.index(max(cnt))
