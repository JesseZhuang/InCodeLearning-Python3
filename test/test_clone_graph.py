import unittest

from algorithm.graph.clone_graph import Solution
from algorithm.jzstruct.graph_node import Node


def build_graph(adj_list):
    """Build graph from adjacency list (1-indexed). Returns node with val=1 or None."""
    if not adj_list:
        return None
    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}
    for i, neighbors in enumerate(adj_list):
        for n in neighbors:
            nodes[i + 1].neighbors.append(nodes[n])
    return nodes[1]


def graph_to_adj_list(node):
    """Convert graph starting from node to sorted adjacency list."""
    if not node:
        return []
    visited = {}
    queue = [node]
    visited[node.val] = node
    while queue:
        cur = queue.pop(0)
        for n in cur.neighbors:
            if n.val not in visited:
                visited[n.val] = n
                queue.append(n)
    result = []
    for v in sorted(visited.keys()):
        result.append(sorted(n.val for n in visited[v].neighbors))
    return result


class TestCloneGraph(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        self.methods = [self.sol.cloneGraph, self.sol.cloneGraphBFS, self.sol.cloneGraphBFSDQ]

    def verify(self, adj_list):
        for method in self.methods:
            with self.subTest(method=method.__name__):
                node = build_graph(adj_list)
                clone = method(node)
                if not adj_list:
                    self.assertIsNone(clone)
                    continue
                self.assertIsNotNone(clone)
                self.assertIsNot(clone, node)
                self.assertEqual(clone.val, node.val)
                clone_adj = graph_to_adj_list(clone)
                expected = [sorted(neighbors) for neighbors in adj_list]
                self.assertEqual(expected, clone_adj)

    def test_example1(self):
        self.verify([[2, 4], [1, 3], [2, 4], [1, 3]])

    def test_example2_single_node(self):
        self.verify([[]])

    def test_example3_empty(self):
        self.verify([])

    def test_two_nodes(self):
        self.verify([[2], [1]])

    def test_linear(self):
        self.verify([[2], [1, 3], [2]])

    def test_fully_connected(self):
        self.verify([[2, 3, 4], [1, 3, 4], [1, 2, 4], [1, 2, 3]])
