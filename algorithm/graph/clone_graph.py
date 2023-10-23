'''leet code 133, medium'''

from typing import Optional

from algorithm.struct.graph_node import Node


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''dfs, O(V+E, N^2) time, O(N) space'''
        val_node = dict()
        return self.dfs(node, val_node)

    def dfs(self, node, val_node):
        if not node:
            return node
        if node.val in val_node:
            return val_node[node.val]
        res = Node(val=node.val)
        val_node[node.val] = res
        for n in node.neighbors:
            res.neighbors.append(self.dfs(n, val_node))
        return res
