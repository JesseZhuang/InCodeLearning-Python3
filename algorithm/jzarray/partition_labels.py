"""leet 763, medium"""


class Solution:
    """Greedy with last occurrence. O(n) time, O(1) space."""

    def partitionLabels(self, s: str) -> list[int]:
        last_occurrence = [0] * 26  # O(1) space, 26 letters
        for i, char in enumerate(s):  # O(n)
            last_occurrence[ord(char) - ord("a")] = i

        partition_end = 0
        partition_start = 0
        partition_sizes = []

        for i, char in enumerate(s):  # O(n)
            partition_end = max(
                partition_end, last_occurrence[ord(char) - ord("a")]
            )
            if i == partition_end:
                partition_sizes.append(i - partition_start + 1)
                partition_start = i + 1

        return partition_sizes


class Solution2:
    """Merge intervals. O(n) time, O(1) space."""

    def partitionLabels(self, s: str) -> list[int]:
        first = {}
        last = {}
        for i, ch in enumerate(s):  # O(n)
            if ch not in first:
                first[ch] = i
            last[ch] = i

        # Build and merge intervals for each unique char: at most 26
        intervals = sorted((first[ch], last[ch]) for ch in first)  # O(26 log 26) = O(1)

        result = []
        start, end = intervals[0]
        for s_i, e_i in intervals[1:]:  # O(26) = O(1)
            if s_i <= end:
                end = max(end, e_i)
            else:
                result.append(end - start + 1)
                start, end = s_i, e_i
        result.append(end - start + 1)

        return result
