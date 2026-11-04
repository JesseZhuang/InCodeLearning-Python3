import unittest

from algorithm.jzarray.lex_max_valid_sequence import Solution


class TestLexMaxValidSequence(unittest.TestCase):

    def setUp(self):
        self.solutions = [Solution()]

    def test_small_inputs_return_lexicographically_largest_sequences(self):
        expected_by_n = {
            1: [1],
            2: [2, 1, 2],
            3: [3, 1, 2, 3, 2],
            4: [4, 2, 3, 2, 4, 3, 1],
            5: [5, 3, 1, 4, 3, 5, 2, 4, 2],
        }

        for solution in self.solutions:
            for n, expected in expected_by_n.items():
                with self.subTest(n=n):
                    self.assertEqual(
                        expected, solution.constructDistancedSequence(n)
                    )

    def test_results_are_valid_across_constraint_range(self):
        for solution in self.solutions:
            for n in range(1, 21):
                with self.subTest(n=n):
                    sequence = solution.constructDistancedSequence(n)

                    self.assertEqual(2 * n - 1, len(sequence))
                    self.assertEqual(set(range(1, n + 1)), set(sequence))
                    for number in range(1, n + 1):
                        positions = [
                            i for i, value in enumerate(sequence) if value == number
                        ]
                        expected_count = 1 if number == 1 else 2
                        self.assertEqual(expected_count, len(positions), number)
                        if number > 1:
                            self.assertEqual(
                                number, positions[1] - positions[0], number
                            )


if __name__ == '__main__':
    unittest.main()
