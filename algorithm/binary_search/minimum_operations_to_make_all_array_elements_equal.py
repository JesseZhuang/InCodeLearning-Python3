from bisect import bisect_left


class Solution:
    def minOperations(self, nums, queries):
        """Return the adjustment cost for each target query.

        Sorting and prefix-sum construction take O(n log n) time; each of m
        queries takes O(log n), for O((n + m) log n) total time and O(n)
        extra space.
        """
        ordered = sorted(nums)
        prefix = [0]
        for value in ordered:
            prefix.append(prefix[-1] + value)

        total = prefix[-1]
        result = []
        for target in queries:
            split = bisect_left(ordered, target)
            left_cost = target * split - prefix[split]
            right_cost = total - prefix[split] - target * (len(ordered) - split)
            result.append(left_cost + right_cost)

        return result
