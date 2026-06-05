from collections import defaultdict, deque


class Solution:
    """787. Cheapest Flights Within K Stops

    Bellman-Ford variant: relax all edges up to k+1 times.
    Time O((k+1) * E), Space O(n).
    """

    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        prices = [INF] * n
        prices[src] = 0

        for _ in range(k + 1):  # O(k+1) rounds
            tmp = prices[:]
            for u, v, w in flights:  # O(E) edges per round
                if prices[u] != INF and prices[u] + w < tmp[v]:
                    tmp[v] = prices[u] + w
            prices = tmp

        return prices[dst] if prices[dst] != INF else -1


class Solution2:
    """787. Cheapest Flights Within K Stops

    BFS with pruning: level-order BFS where level = number of stops.
    Time O((k+1) * E), Space O(n + E).
    """

    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        INF = float("inf")
        dist = [INF] * n
        dist[src] = 0
        q = deque([(src, 0)])  # (node, cost)
        stops = 0

        while q and stops <= k:
            for _ in range(len(q)):  # O(level width)
                node, cost = q.popleft()
                for nei, w in graph[node]:  # O(edges from node)
                    new_cost = cost + w
                    if new_cost < dist[nei]:
                        dist[nei] = new_cost
                        q.append((nei, new_cost))
            stops += 1

        return dist[dst] if dist[dst] != INF else -1
