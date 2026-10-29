"""LeetCode 1700, easy. Tags: array, queue, simulation, counting."""


class Solution:
    """Count preferences instead of physically rotating the student queue."""

    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        remaining = [0, 0]
        for student in students:  # O(n) time, O(1) extra space.
            remaining[student] += 1

        for sandwich in sandwiches:  # O(n) time overall.
            if remaining[sandwich] == 0:
                return remaining[1 - sandwich]
            remaining[sandwich] -= 1

        return 0

    def countStudentsQueue(self, students: list[int], sandwiches: list[int]) -> int:
        """Simulate queue rotations directly in O(n^2) time and O(n) space."""
        queue = list(students)
        sandwich_index = 0
        rotations_without_eating = 0

        while queue and rotations_without_eating < len(queue):
            if queue[0] == sandwiches[sandwich_index]:
                queue.pop(0)
                sandwich_index += 1
                rotations_without_eating = 0
            else:
                queue.append(queue.pop(0))
                rotations_without_eating += 1

        return len(queue)
