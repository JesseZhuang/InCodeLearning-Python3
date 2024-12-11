"""leet 787, medium"""
import sys


class Solution:
    """todo editorial, bellman-ford"""

    def findCheapestPrice(self, n, flights, src, dst, K):
        distance = [sys.maxsize for i in range(n)]
        distance[src] = 0

        for i in range(0, K + 1):
            dN = list(distance)  # 直接把最短路数组复制一遍, 用副本保存松弛的结果, 也可以保证每一轮迭代最多增加一条边, 不过执行效率略低
            for u, v, c in flights:
                dN[v] = min(dN[v], distance[u] + c)
            distance = dN

        if distance[dst] != sys.maxsize:
            return distance[dst]
        else:
            return -1
