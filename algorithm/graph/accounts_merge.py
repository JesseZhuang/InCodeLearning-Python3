"""leet code 721, medium, tags: array, hash table, string, depth-first search, breadth-first search, union find,
sorting."""

from collections import defaultdict
from typing import List


class Solution:
    """Union-Find (rank + path compression). O(nk*α(nk) + nk*log(nk)) time, O(nk) space."""

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        rank = {}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1

        email_to_name = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                    rank[email] = 0
                email_to_name[email] = name
                union(account[1], email)

        groups = defaultdict(list)
        for email in parent:
            groups[find(email)].append(email)

        return [[email_to_name[root]] + sorted(emails) for root, emails in groups.items()]


class Solution2:
    """DFS. O(nk*log(nk)) time, O(nk) space."""

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        email_to_name = {}
        for account in accounts:
            name = account[0]
            first = account[1]
            for email in account[1:]:
                graph[first].add(email)
                graph[email].add(first)
                email_to_name[email] = name

        visited = set()

        def dfs(node, component):
            visited.add(node)
            component.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        res = []
        for email in graph:
            if email not in visited:
                component = []
                dfs(email, component)
                res.append([email_to_name[email]] + sorted(component))
        return res
