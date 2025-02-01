from unittest import TestCase

from algorithm.heap.meeting_rooms_s import roomsNeeded


class Test(TestCase):
    def test_rooms_needed(self):
        test_cases = [
            ([[1, 4], [2, 5], [6, 8], [1, 3], [3, 6]], 2, 2),
            ([[1, 4], [2, 5], [6, 8], [1, 3], [3, 6]], 1, 3),
            ([[1, 4], [2, 5], [6, 8], [1, 3], [3, 6]], 3, 1),
            ([[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]], 3, 2),
            ([[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]], 2, 3),
        ]
        for meetings, k, exp in test_cases:
            self.assertEqual(exp, roomsNeeded(meetings, k))
