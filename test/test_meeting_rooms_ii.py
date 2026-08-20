from unittest import TestCase

from algorithm.heap.meeting_rooms_ii import Solution, Solution2


class TestMeetingRoomsII(TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(2, sol.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.minMeetingRooms([[7, 10], [2, 4]]))

    def test_single_meeting(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.minMeetingRooms([[1, 5]]))

    def test_all_overlap(self):
        for sol in self.solutions:
            self.assertEqual(3, sol.minMeetingRooms([[1, 10], [2, 7], [3, 19]]))

    def test_no_overlap(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.minMeetingRooms([[1, 2], [3, 4], [5, 6]]))

    def test_back_to_back(self):
        """End time equals start time of next — should reuse the room."""
        for sol in self.solutions:
            self.assertEqual(1, sol.minMeetingRooms([[1, 5], [5, 10], [10, 15]]))

    def test_all_same_time(self):
        for sol in self.solutions:
            self.assertEqual(4, sol.minMeetingRooms([[1, 2], [1, 2], [1, 2], [1, 2]]))

    def test_large_intervals(self):
        for sol in self.solutions:
            self.assertEqual(2, sol.minMeetingRooms([[0, 1000000], [500000, 1000000]]))
