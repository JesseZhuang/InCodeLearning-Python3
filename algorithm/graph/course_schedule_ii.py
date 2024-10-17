"""leet code 210, medium"""
import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses
        res = list()

        for e in prerequisites:
            edges[e[1]].append(e[0])
            indeg[e[0]] += 1

        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])

        while q:
            u = q.popleft()
            res.append(u)
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0: q.append(v)

        if len(res) != numCourses: res = list()
        return res
