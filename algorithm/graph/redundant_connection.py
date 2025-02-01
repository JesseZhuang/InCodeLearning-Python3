"""leet 684, medium"""


class Solution:
    """todo editorial"""
    cycle_start = -1

    # Perform the DFS and store a node in the cycle as cycleStart.
    def _DFS(self, src, visited, adj_list, parent):
        visited[src] = True

        for adj in adj_list[src]:
            if not visited[adj]:
                parent[adj] = src
                self._DFS(adj, visited, adj_list, parent)
                # If the node is visited and the parent is different then the
                # node is part of the cycle.
            elif adj != parent[src] and self.cycle_start == -1:
                self.cycle_start = adj
                parent[adj] = src

    def findRedundantConnection(self, edges):
        N = len(edges)

        visited = [False] * N
        parent = [-1] * N

        adj_list = [[] for _ in range(N)]
        for edge in edges:
            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)

        self._DFS(0, visited, adj_list, parent)

        cycle_nodes = {}
        node = self.cycle_start
        # Start from the cycleStart node and backtrack to get all the nodes in
        # the cycle. Mark them all in the map.
        while True:
            cycle_nodes[node] = 1
            node = parent[node]
            if node == self.cycle_start:
                break

        # If both nodes of the edge were marked as cycle nodes then this edge
        # can be removed.
        for i in range(len(edges) - 1, -1, -1):
            if (edges[i][0] - 1) in cycle_nodes and (
                    edges[i][1] - 1
            ) in cycle_nodes:
                return edges[i]

        return []  # This line should theoretically never be reached
