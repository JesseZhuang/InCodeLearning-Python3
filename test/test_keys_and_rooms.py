import unittest

from algorithm.graph.keys_and_rooms import Solution


class TestKeysAndRooms(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        rooms = [[1], [2], [3], []]
        for sol in self.solutions:
            self.assertTrue(sol.canVisitAllRooms(rooms))
            self.assertTrue(sol.canVisitAllRoomsBFS(rooms))

    def test_example2(self):
        rooms = [[1, 3], [3, 0, 1], [2], [0]]
        for sol in self.solutions:
            self.assertFalse(sol.canVisitAllRooms(rooms))
            self.assertFalse(sol.canVisitAllRoomsBFS(rooms))

    def test_single_room(self):
        rooms = [[]]
        for sol in self.solutions:
            self.assertTrue(sol.canVisitAllRooms(rooms))
            self.assertTrue(sol.canVisitAllRoomsBFS(rooms))

    def test_all_keys_in_first_room(self):
        rooms = [[1, 2, 3], [], [], []]
        for sol in self.solutions:
            self.assertTrue(sol.canVisitAllRooms(rooms))
            self.assertTrue(sol.canVisitAllRoomsBFS(rooms))

    def test_chain(self):
        rooms = [[1], [2], [3], [4], []]
        for sol in self.solutions:
            self.assertTrue(sol.canVisitAllRooms(rooms))
            self.assertTrue(sol.canVisitAllRoomsBFS(rooms))

    def test_isolated_last_room(self):
        rooms = [[1], [2], [], []]
        for sol in self.solutions:
            self.assertFalse(sol.canVisitAllRooms(rooms))
            self.assertFalse(sol.canVisitAllRoomsBFS(rooms))

    def test_duplicate_keys(self):
        rooms = [[1, 1, 1], [2], [3], []]
        for sol in self.solutions:
            self.assertTrue(sol.canVisitAllRooms(rooms))
            self.assertTrue(sol.canVisitAllRoomsBFS(rooms))

    def test_cycle_without_full_coverage(self):
        rooms = [[1], [0], [3], [2]]
        for sol in self.solutions:
            self.assertFalse(sol.canVisitAllRooms(rooms))
            self.assertFalse(sol.canVisitAllRoomsBFS(rooms))


if __name__ == '__main__':
    unittest.main()
