'''leet code 133, medium'''

from collections import deque
from queue import Queue
from typing import Optional

from algorithm.jzstruct.graph_node import Node


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''dfs, O(V+E, N^2) time, O(N) space 43ms, 16.7Mb'''
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

    def cloneGraphBFS(self, node: Optional['Node']) -> Optional['Node']:
        '''42ms, 16.8Mb'''
        if not node:
            return node
        res = Node(node.val)
        q = Queue()
        q.put(node)
        val_node = dict()
        val_node[node.val] = res
        while not q.empty():
            cur = q.get()
            for n in cur.neighbors:
                if n.val not in val_node:
                    q.put(n)
                    val_node[n.val] = Node(n.val)
                val_node[cur.val].neighbors.append(val_node[n.val])
        return res

    def cloneGraphBFSDQ(self, node: Optional['Node']) -> Optional['Node']:
        '''42ms, 16.8Mb'''
        if not node:
            return node
        q = deque()
        q.append(node)
        res = Node(node.val)
        val_node = dict()
        val_node[node.val] = res
        while len(q) > 0:
            cur = q.popleft()
            for n in cur.neighbors:
                if not n.val in val_node:
                    val_node[n.val] = Node(n.val)
                    q.append(n)
                val_node[cur.val].neighbors.append(val_node[n.val])
        return res
