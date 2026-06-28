import unittest

from algorithm.graph.course_schedule_ii import Solution


class TestCourseScheduleII(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def is_valid_order(self, order, num_courses, prerequisites):
        if len(order) != num_courses:
            return False
        pos = {v: i for i, v in enumerate(order)}
        if len(pos) != num_courses:
            return False
        for course, prereq in prerequisites:
            if pos[prereq] >= pos[course]:
                return False
        return True

    def verify(self, num_courses, prerequisites, has_order):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                result = sol.findOrder(num_courses, prerequisites)
                if has_order:
                    self.assertTrue(
                        self.is_valid_order(result, num_courses, prerequisites),
                        f"Invalid order: {result}"
                    )
                else:
                    self.assertEqual(result, [])

    def test_example1(self):
        self.verify(2, [[1, 0]], True)

    def test_example2(self):
        self.verify(4, [[1, 0], [2, 0], [3, 1], [3, 2]], True)

    def test_cycle(self):
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

    def test_all_depend_on_one(self):
        self.verify(5, [[1, 0], [2, 0], [3, 0], [4, 0]], True)

    def test_large_chain(self):
        n = 2000
        prereqs = [[i, i - 1] for i in range(1, n)]
        self.verify(n, prereqs, True)

    def test_large_cycle(self):
        n = 2000
        prereqs = [[i, i - 1] for i in range(1, n)] + [[0, n - 1]]
        self.verify(n, prereqs, False)
