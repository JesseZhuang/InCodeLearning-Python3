"""leet 2685, medium"""


class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.size = [1] * n

    def _find(self, node):
        # Find root of component with path compression
        if self.parent[node] == -1:
            return node
        self.parent[node] = self._find(self.parent[node])
        return self.parent[node]

    def _union(self, node_1, node_2):
        # Union by size
        root_1 = self._find(node_1)
        root_2 = self._find(node_2)

        if root_1 == root_2:
            return

        # Merge smaller component into larger one
        if self.size[root_1] > self.size[root_2]:
            self.parent[root_2] = root_1
            self.size[root_1] += self.size[root_2]
        else:
            self.parent[root_1] = root_2
            self.size[root_2] += self.size[root_1]


class Solution:
    """todo editorial"""

    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        # Initialize Union Find and edge counter
        dsu = UnionFind(n)
        edge_count = {}

        # Connect components using edges
        for edge in edges:
            dsu._union(edge[0], edge[1])

        # Count edges in each component
        for edge in edges:
            root = dsu._find(edge[0])
            edge_count[root] = edge_count.get(root, 0) + 1

        # Check if each component is complete
        complete_count = 0
        for vertex in range(n):
            if dsu._find(vertex) == vertex:  # If vertex is root
                node_count = dsu.size[vertex]
                expected_edges = (node_count * (node_count - 1)) // 2
                if edge_count.get(vertex, 0) == expected_edges:
                    complete_count += 1

        return complete_count
