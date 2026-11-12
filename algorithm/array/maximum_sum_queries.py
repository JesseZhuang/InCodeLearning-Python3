from bisect import bisect_left


class _FenwickMax:
    def __init__(self, size):
        self.tree = [-1] * (size + 1)

    def update(self, index, value):
        # Each point update visits O(log n) Fenwick nodes.
        while index < len(self.tree):
            self.tree[index] = max(self.tree[index], value)
            index += index & -index

    def query(self, index):
        # Each prefix maximum query visits O(log n) Fenwick nodes.
        best = -1
        while index > 0:
            best = max(best, self.tree[index])
            index -= index & -index
        return best


class Solution:
    def maximum_sum_queries(self, nums1, nums2, queries):
        # Sorting points and queries costs O(n log n + q log q).
        points = sorted(
            ((a, b, a + b) for a, b in zip(nums1, nums2)),
            key=lambda point: point[0],
            reverse=True,
        )
        query_order = sorted(
            range(len(queries)), key=lambda i: queries[i][0], reverse=True
        )

        coords = sorted(set(nums2))
        fenwick = _FenwickMax(len(coords))
        answers = [-1] * len(queries)
        point_index = 0

        # Each point is inserted once and each query is answered once, with
        # O(log n) Fenwick work per operation.
        for query_index in query_order:
            min_a, min_b = queries[query_index]
            while point_index < len(points) and points[point_index][0] >= min_a:
                a, b, total = points[point_index]
                # Reversing compressed b-ranks turns b >= min_b into a prefix.
                rank = bisect_left(coords, b)
                fenwick.update(len(coords) - rank, total)
                point_index += 1

            prefix_length = len(coords) - bisect_left(coords, min_b)
            answers[query_index] = fenwick.query(prefix_length)

        # Total time: O(n log n + q log q + (n + q) log n).
        # Auxiliary space: O(n + q) for points, coordinates, and query order.
        return answers
