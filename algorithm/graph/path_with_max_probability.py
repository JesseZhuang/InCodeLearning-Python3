import heapq
from collections import defaultdict


class Solution:
    """Modified Dijkstra with max-heap. O((V+E)logV) time, O(V+E) space."""

    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float],
                       start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (u, v), prob in zip(edges, succProb):  # O(E)
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        max_prob = [0.0] * n  # O(V)
        max_prob[start_node] = 1.0
        pq = [(-1.0, start_node)]  # max-heap via negation
        while pq:  # O((V+E)logV)
            neg_prob, node = heapq.heappop(pq)  # O(logV)
            cur_prob = -neg_prob
            if node == end_node:
                return cur_prob
            if cur_prob < max_prob[node]:
                continue
            for neighbor, edge_prob in graph[node]:  # O(degree) per node
                new_prob = cur_prob * edge_prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))  # O(logV)
        return 0.0


class Solution2:
    """Bellman-Ford relaxation. O(V*E) time, O(V) space."""

    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float],
                       start_node: int, end_node: int) -> float:
        max_prob = [0.0] * n  # O(V)
        max_prob[start_node] = 1.0
        for _ in range(n - 1):  # O(V) iterations
            updated = False
            for (u, v), prob in zip(edges, succProb):  # O(E) per iteration
                if max_prob[u] * prob > max_prob[v]:
                    max_prob[v] = max_prob[u] * prob
                    updated = True
                if max_prob[v] * prob > max_prob[u]:
                    max_prob[u] = max_prob[v] * prob
                    updated = True
            if not updated:
                break
        return max_prob[end_node]
