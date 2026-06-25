"""LeetCode 547. Number of Provinces."""

from collections import deque


class Solution:
    """DFS on adjacency matrix."""

    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        count = 0
        for i in range(n):  # O(n)
            if not visited[i]:
                count += 1
                stack = [i]
                while stack:  # O(n) total across all DFS calls
                    node = stack.pop()
                    for j in range(n):  # O(n) neighbors
                        if isConnected[node][j] == 1 and not visited[j]:
                            visited[j] = True
                            stack.append(j)
        return count


class Solution2:
    """Union Find with path compression and union by rank."""

    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:  # O(alpha(n)) amortized
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px  # O(1)
            if rank[px] == rank[py]:
                rank[px] += 1
            return True

        count = n
        for i in range(n):  # O(n)
            for j in range(i + 1, n):  # O(n), together O(n^2)
                if isConnected[i][j] == 1:
                    if union(i, j):
                        count -= 1
        return count
