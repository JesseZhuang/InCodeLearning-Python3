from collections import defaultdict


class Solution:
    """Hierholzer's algorithm (recursive DFS) — Eulerian path in directed graph."""

    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph: dict[str, list[str]] = defaultdict(list)
        for src, dst in tickets:  # O(E)
            graph[src].append(dst)
        for src in graph:  # O(E log E) sort each adjacency list in reverse for pop()
            graph[src].sort(reverse=True)

        route: list[str] = []

        def dfs(airport: str) -> None:
            while graph[airport]:  # O(E) total across all calls
                dfs(graph[airport].pop())
            route.append(airport)

        dfs("JFK")
        return route[::-1]  # O(E)


class Solution2:
    """Hierholzer's algorithm (iterative stack) — avoids recursion limit."""

    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph: dict[str, list[str]] = defaultdict(list)
        for src, dst in tickets:  # O(E)
            graph[src].append(dst)
        for src in graph:  # O(E log E)
            graph[src].sort(reverse=True)

        stack: list[str] = ["JFK"]
        route: list[str] = []
        while stack:  # O(E)
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            route.append(stack.pop())
        return route[::-1]  # O(E)
