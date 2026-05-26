"""leet 743, medium, tags: graph, heap, shortest path, Dijkstra, Bellman-Ford."""
import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """Dijkstra's algorithm. Time O(E log V), Space O(V + E)."""
        graph = defaultdict(list)
        for u, v, w in times:  # O(E)
            graph[u].append((v, w))
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        pq = [(0, k)]  # (distance, node)
        while pq:  # O(E log V) total
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:  # relaxation
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        res = max(dist[1:])  # O(V), skip index 0
        return res if res < float('inf') else -1


class Solution2:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """Bellman-Ford. Time O(V * E), Space O(V)."""
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        for _ in range(n - 1):  # O(V) iterations
            for u, v, w in times:  # O(E) edges
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        res = max(dist[1:])
        return res if res < float('inf') else -1
