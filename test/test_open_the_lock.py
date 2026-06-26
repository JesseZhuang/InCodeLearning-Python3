import unittest

from algorithm.graph.open_the_lock import Solution, SolutionBidirectional


class TestOpenTheLock(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), SolutionBidirectional()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(
                sol.openLock(["0201", "0101", "0102", "1212", "2002"], "0202"), 6
            )

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(
                sol.openLock(["8888"], "0009"), 1
            )

    def test_example3_unreachable(self):
        for sol in self.solutions:
            self.assertEqual(
                sol.openLock(
                    ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"],
                    "8888",
                ),
                -1,
            )

    def test_start_is_deadend(self):
        for sol in self.solutions:
            self.assertEqual(sol.openLock(["0000"], "8888"), -1)

    def test_target_is_start(self):
        for sol in self.solutions:
            self.assertEqual(sol.openLock(["1234"], "0000"), 0)

    def test_single_turn(self):
        for sol in self.solutions:
            self.assertEqual(sol.openLock([], "1000"), 1)
            self.assertEqual(sol.openLock([], "9000"), 1)
            self.assertEqual(sol.openLock([], "0001"), 1)

    def test_wraparound(self):
        for sol in self.solutions:
            self.assertEqual(sol.openLock([], "9999"), 4)

    def test_no_deadends(self):
        for sol in self.solutions:
            self.assertEqual(sol.openLock([], "5555"), 20)


if __name__ == "__main__":
    unittest.main()
