"""leet 763, medium"""


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # Stores the last index of each character in 's'
        last_occurrence = [0] * 26
        for i, char in enumerate(s):
            last_occurrence[ord(char) - ord("a")] = i

        partition_end = 0
        partition_start = 0
        partition_sizes = []

        for i, char in enumerate(s):
            partition_end = max(
                partition_end, last_occurrence[ord(char) - ord("a")]
            )
            # End of the current partition
            if i == partition_end:
                partition_sizes.append(i - partition_start + 1)
                partition_start = i + 1

        return partition_sizes
