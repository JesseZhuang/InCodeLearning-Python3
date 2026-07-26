from collections import defaultdict, deque


class Solution:
    """BFS — build weighted directed graph, find path product between query nodes."""

    def calcEquation(
        self,
        equations: list[list[str]],
        values: list[float],
        queries: list[list[str]],
    ) -> list[float]:
        graph: dict[str, list[tuple[str, float]]] = defaultdict(list)
        for (a, b), v in zip(equations, values):  # O(E) build adjacency list
            graph[a].append((b, v))
            graph[b].append((a, 1.0 / v))

        def bfs(src: str, dst: str) -> float:
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            visited: set[str] = {src}
            queue: deque[tuple[str, float]] = deque([(src, 1.0)])
            while queue:  # O(V + E)
                node, product = queue.popleft()
                for neighbor, weight in graph[node]:
                    if neighbor == dst:
                        return product * weight
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, product * weight))
            return -1.0

        return [bfs(a, b) for a, b in queries]  # O(Q * (V + E))


class Solution2:
    """Union-Find with weighted edges — path compression maintains ratio to root."""

    def calcEquation(
        self,
        equations: list[list[str]],
        values: list[float],
        queries: list[list[str]],
    ) -> list[float]:
        parent: dict[str, str] = {}
        rank: dict[str, int] = {}
        weight: dict[str, float] = {}  # weight[x] = x / root(x)

        def find(x: str) -> str:  # O(α(n)) amortized with path compression
            if x != parent[x]:
                root = find(parent[x])
                weight[x] *= weight[parent[x]]
                parent[x] = root
            return parent[x]

        def union(a: str, b: str, val: float) -> None:
            if a not in parent:
                parent[a], rank[a], weight[a] = a, 0, 1.0
            if b not in parent:
                parent[b], rank[b], weight[b] = b, 0, 1.0
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            # w = ra / rb = val * weight[b] / weight[a]
            w = val * weight[b] / weight[a]
            if rank[ra] < rank[rb]:
                parent[ra] = rb
                weight[ra] = w  # ra / new_root(rb) = ra/rb = w
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
                weight[rb] = 1.0 / w  # rb / new_root(ra) = rb/ra = 1/w
            else:
                parent[rb] = ra
                weight[rb] = 1.0 / w
                rank[ra] += 1

        for (a, b), v in zip(equations, values):  # O(E * α(n))
            union(a, b, v)

        results: list[float] = []
        for a, b in queries:  # O(Q * α(n))
            if a not in parent or b not in parent:
                results.append(-1.0)
            elif find(a) != find(b):
                results.append(-1.0)
            else:
                results.append(weight[a] / weight[b])
        return results
