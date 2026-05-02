import unittest

from algorithm.graph.course_schedule import Solution, Solution2


class TestCourseSchedule(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def verify(self, n, prerequisites, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.canFinish(n, prerequisites))

    def test_example1(self):
        self.verify(2, [[1, 0]], True)

    def test_example2(self):
        self.verify(2, [[1, 0], [0, 1]], False)

    def test_no_prerequisites(self):
        self.verify(3, [], True)

    def test_single_course(self):
        self.verify(1, [], True)

    def test_chain(self):
        self.verify(4, [[1, 0], [2, 1], [3, 2]], True)

    def test_cycle_in_chain(self):
        self.verify(4, [[1, 0], [2, 1], [3, 2], [0, 3]], False)

    def test_disconnected(self):
        self.verify(4, [[1, 0], [3, 2]], True)

    def test_diamond(self):
        self.verify(4, [[1, 0], [2, 0], [3, 1], [3, 2]], True)

    def test_self_loop(self):
        self.verify(2, [[0, 0]], False)

    def test_large_no_cycle(self):
        n = 2000
        prereqs = [[i, i - 1] for i in range(1, n)]
        self.verify(n, prereqs, True)

    def test_large_with_cycle(self):
        n = 2000
        prereqs = [[i, i - 1] for i in range(1, n)] + [[0, n - 1]]
        self.verify(n, prereqs, False)

    def test_all_depend_on_one(self):
        self.verify(5, [[1, 0], [2, 0], [3, 0], [4, 0]], True)

    def test_multiple_components_one_cycle(self):
        self.verify(6, [[1, 0], [3, 2], [2, 3], [5, 4]], False)
