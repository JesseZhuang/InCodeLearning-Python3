import unittest
from functools import lru_cache
from itertools import product

from algorithm.dp.questions_brainpower import Solution


class TestQuestionsBrainpower(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_examples(self):
        cases = [
            ([[3, 2], [4, 3], [4, 4], [2, 5]], 5),
            ([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], 7),
        ]
        for questions, expected in cases:
            for solution in self.solutions:
                with self.subTest(questions=questions):
                    self.assertEqual(expected, solution.mostPoints(questions))

    def test_single_question_and_jump_outside_array(self):
        for solution in self.solutions:
            self.assertEqual(100_000, solution.mostPoints([[100_000, 100_000]]))
            self.assertEqual(5, solution.mostPoints([[5, 100_000], [1, 1]]))

    def test_take_or_skip(self):
        for solution in self.solutions:
            self.assertEqual(100, solution.mostPoints([[1, 1], [100, 1], [1, 1]]))
            self.assertEqual(12, solution.mostPoints([[5, 1], [1, 1], [7, 1]]))

    def test_small_cases_against_exhaustive_search(self):
        @lru_cache(None)
        def exhaustive(questions, index):
            if index >= len(questions):
                return 0
            points, brainpower = questions[index]
            return max(
                exhaustive(questions, index + 1),
                points + exhaustive(questions, index + brainpower + 1),
            )

        for length in range(1, 5):
            for items in product(((1, 1), (2, 1), (3, 2), (4, 4)), repeat=length):
                questions = [list(item) for item in items]
                expected = exhaustive(items, 0)
                for solution in self.solutions:
                    with self.subTest(questions=questions):
                        self.assertEqual(expected, solution.mostPoints(questions))

    def test_maximum_length_and_64_bit_total(self):
        questions = [[100_000, 1] for _ in range(100_000)]
        for solution in self.solutions:
            self.assertEqual(5_000_000_000, solution.mostPoints(questions))


if __name__ == "__main__":
    unittest.main()
