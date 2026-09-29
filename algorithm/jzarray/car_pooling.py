"""leet code 1094, medium, tags: array, sorting, heap, simulation, prefix sum."""


class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        """Difference array approach."""
        stops = [0] * 1001  # O(1001) space, constraints: 0 <= from < to <= 1000
        for passengers, frm, to in trips:
            stops[frm] += passengers
            stops[to] -= passengers
        cur = 0
        for delta in stops:  # O(1001)
            cur += delta
            if cur > capacity:
                return False
        return True  # Time O(n+1001), Space O(1001) where n = len(trips)


class Solution2:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        """Sorted events sweep line approach."""
        events = []
        for passengers, frm, to in trips:  # O(n)
            events.append((frm, passengers))
            events.append((to, -passengers))
        events.sort()  # O(n log n)
        cur = 0
        for _, delta in events:  # O(n)
            cur += delta
            if cur > capacity:
                return False
        return True  # Time O(n log n), Space O(n)
