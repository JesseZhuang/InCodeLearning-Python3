"""323. Number of Connected Components in an Undirected Graph

You have a graph of n nodes. You are given an integer n and an array edges
where edges[i] = [ai, bi] indicates that there is an edge between ai and bi
in the graph.

Return the number of connected components in the graph.

Constraints:
- 1 <= n <= 2000
- 1 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai <= bi < n
- ai != bi
- There are no repeated edges.
"""


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        """Union-Find approach.

        Complexity: Time O(n + e * alpha(n)) ≈ O(n + e), Space O(n).
        """
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:  # O(alpha(n)) amortized with path compression
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:  # union by rank
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True

        components = n
        for a, b in edges:  # O(e) edges
            if union(a, b):
                components -= 1
        return components


class Solution2:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        """DFS approach.

        Complexity: Time O(n + e), Space O(n + e) for adjacency list + visited set.
        """
        adj = [[] for _ in range(n)]  # O(n + e) space
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        components = 0

        def dfs(node):
            stack = [node]
            while stack:  # O(n + e) total across all calls
                cur = stack.pop()
                for neighbor in adj[cur]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

        for i in range(n):  # O(n)
            if i not in visited:
                visited.add(i)
                dfs(i)
                components += 1

        return components
