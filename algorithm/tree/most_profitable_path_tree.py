"""leet 2467, medium"""


class Solution:
    """todo editorial"""

    def __init__(self):
        self.tree = []
        self.distance_from_bob = []
        self.n = 0

    def mostProfitablePath(self, edges, bob, amount):
        self.n = len(amount)
        self.tree = [[] for _ in range(self.n)]
        self.distance_from_bob = [0] * self.n

        # Form tree with edges
        for edge in edges:
            self.tree[edge[0]].append(edge[1])
            self.tree[edge[1]].append(edge[0])

        return self.find_paths(0, 0, 0, bob, amount)

    # Depth-first Search
    def find_paths(self, source_node, parent_node, time, bob, amount):
        max_income = 0
        max_child = float("-inf")

        # Find the node distances from Bob
        if source_node == bob:
            self.distance_from_bob[source_node] = 0
        else:
            self.distance_from_bob[source_node] = self.n

        for adjacent_node in self.tree[source_node]:
            if adjacent_node != parent_node:
                max_child = max(
                    max_child,
                    self.find_paths(
                        adjacent_node, source_node, time + 1, bob, amount
                    ),
                )
                self.distance_from_bob[source_node] = min(
                    self.distance_from_bob[source_node],
                    self.distance_from_bob[adjacent_node] + 1,
                )

        # Alice reaches the node first
        if self.distance_from_bob[source_node] > time:
            max_income += amount[source_node]
        # Alice and Bob reach the node at the same time
        elif self.distance_from_bob[source_node] == time:
            max_income += amount[source_node] // 2

        # Return max income of leaf node
        return (
            max_income if max_child == float("-inf") else max_income + max_child
        )
