import unittest

from algorithm.jzstring.task_scheduler import Solution, Solution2, Solution3


class TestTaskScheduler(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2(), Solution3()]

    def test_example1(self):
        for sol in self.solutions:
            self.assertEqual(8, sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2))

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual(6, sol.leastInterval(["A", "C", "A", "B", "D", "B"], 1))

    def test_example3(self):
        for sol in self.solutions:
            self.assertEqual(10, sol.leastInterval(["A", "A", "A", "B", "B", "B"], 3))

    def test_no_cooling(self):
        for sol in self.solutions:
            self.assertEqual(3, sol.leastInterval(["A", "B", "C"], 0))

    def test_single_task(self):
        for sol in self.solutions:
            self.assertEqual(1, sol.leastInterval(["A"], 2))

    def test_all_same_task(self):
        for sol in self.solutions:
            self.assertEqual(7, sol.leastInterval(["A", "A", "A"], 2))

    def test_many_unique_tasks(self):
        for sol in self.solutions:
            self.assertEqual(26, sol.leastInterval(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 100))

    def test_high_cooling_two_tasks(self):
        for sol in self.solutions:
            self.assertEqual(5, sol.leastInterval(["A", "A", "B"], 3))


if __name__ == '__main__':
    unittest.main()
