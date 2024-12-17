"""leet 1792, medium"""
from heapq import heappush, heappop


class Solution:
    """todo editorial"""

    def maxAverageRatio(
            self, classes: list[list[int]], extraStudents: int
    ) -> float:
        # Lambda to calculate the gain of adding an extra student
        def _calculate_gain(passes, total_students):
            return (passes + 1) / (total_students + 1) - passes / total_students

        # Max heap to store (-gain, passes, total_students)
        max_heap = []
        for passes, total_students in classes:
            gain = _calculate_gain(passes, total_students)
            heappush(max_heap, (-gain, passes, total_students))

        # Distribute extra students
        for _ in range(extraStudents):
            current_gain, passes, total_students = heappop(max_heap)
            heappush(
                max_heap,
                (
                    -_calculate_gain(passes + 1, total_students + 1),
                    passes + 1,
                    total_students + 1,
                ),
            )

        # Calculate the final average pass ratio
        total_pass_ratio = 0
        while max_heap:
            _, passes, total_students = heapq.heappop(max_heap)
            total_pass_ratio += passes / total_students
        return total_pass_ratio / len(classes)
