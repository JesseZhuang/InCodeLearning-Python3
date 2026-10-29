import unittest

from algorithm.deq.number_of_students_unable_to_eat_lunch import Solution


class TestNumberOfStudentsUnableToEatLunch(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def assert_unable(self, students, sandwiches, expected):
        for solution in self.solutions:
            with self.subTest(students=students, sandwiches=sandwiches):
                self.assertEqual(expected, solution.countStudents(students, sandwiches))
                self.assertEqual(expected, solution.countStudentsQueue(students, sandwiches))

    def test_examples(self):
        self.assert_unable([1, 1, 0, 0], [0, 1, 0, 1], 0)
        self.assert_unable([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1], 3)

    def test_every_student_eats_same_type(self):
        self.assert_unable([0, 0, 0], [0, 0, 0], 0)
        self.assert_unable([1, 1], [1, 1], 0)

    def test_first_sandwich_has_no_matching_student(self):
        self.assert_unable([0, 0, 0], [1, 0, 0], 3)

    def test_late_exhaustion_leaves_remaining_students(self):
        self.assert_unable([0, 1, 0, 1], [0, 1, 1, 1], 1)

    def test_single_student(self):
        self.assert_unable([0], [0], 0)
        self.assert_unable([0], [1], 1)

    def test_rotations_are_required_before_a_match(self):
        self.assert_unable([1, 1, 0], [0, 1, 1], 0)


if __name__ == "__main__":
    unittest.main()
