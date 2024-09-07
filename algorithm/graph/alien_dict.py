"""lint code 892, hard, leet code 269"""
import heapq
from typing import List


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alien_order(self, words: List[str]) -> str:
        # Write your code here
        return self.topological(self.build_graph(words))

    def build_graph(self, words):
        graph = dict()  # char -> (chars)
        n = len(words)
        for w in words:
            for c in w: graph[c] = set()
        for i in range(1, n):
            a, b = words[i - 1], words[i]
            j = 0
            while j < len(a) and j < len(b) and a[j] == b[j]: j += 1
            if j == len(a): continue
            if j >= len(b): return None  # ["abc", "ab"] case
            graph[a[j]].add(b[j])
        return graph

    def topological(self, graph):
        if graph is None: return ""
        in_dg = dict()  # in degrees
        for v in graph: in_dg[v] = 0
        for v in graph:
            for w in graph[v]:
                in_dg[w] += 1
        pq = []
        for c in in_dg:
            if in_dg[c] == 0: pq.append(c)
        heapq.heapify(pq)
        count, res = 0, []
        while pq:
            v = heapq.heappop(pq)
            count += 1
            res.append(v)
            for w in graph[v]:
                in_dg[w] -= 1
                if in_dg[w] == 0: heapq.heappush(pq, w)

        return "" if count != len(graph) else "".join(res)
