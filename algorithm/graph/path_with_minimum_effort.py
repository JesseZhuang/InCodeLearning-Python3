import heapq


class Solution:
    """Dijkstra. O(m*n*log(m*n)) time, O(m*n) space."""

    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]  # (effort, row, col)
        while heap:
            effort, r, c = heapq.heappop(heap)
            if r == rows - 1 and c == cols - 1:
                return effort
            if effort > dist[r][c]:
                continue
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))
        return 0


class Solution2:
    """Binary search + BFS. O(m*n*log(max_height)) time, O(m*n) space."""

    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        from collections import deque
        rows, cols = len(heights), len(heights[0])

        def can_reach(threshold: int) -> bool:
            visited = [[False] * cols for _ in range(rows)]
            visited[0][0] = True
            queue = deque([(0, 0)])
            while queue:
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return True
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                        if abs(heights[r][c] - heights[nr][nc]) <= threshold:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
            return False

        lo, hi = 0, 10**6  # O(log(max_height))
        while lo < hi:
            mid = (lo + hi) // 2
            if can_reach(mid):  # O(m*n) BFS
                hi = mid
            else:
                lo = mid + 1
        return lo
