import unittest

from algorithm.stack.validate_stack_sequences import Solution


class TestValidateStackSequences(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def verify(self, pushed, popped, expected):
        for solution in self.solutions:
            with self.subTest(solution=solution.__class__.__name__):
                self.assertEqual(expected, solution.validateStackSequences(pushed, popped))

    def test_example_valid(self):
        self.verify([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True)

    def test_example_invalid(self):
        self.verify([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False)

    def test_single_element(self):
        self.verify([0], [0], True)

    def test_pop_each_push(self):
        self.verify([0, 1, 2, 3], [0, 1, 2, 3], True)

    def test_push_all_before_popping(self):
        self.verify([0, 1, 2, 3], [3, 2, 1, 0], True)

    def test_impossible_interleaving(self):
        self.verify([1, 2, 3], [3, 1, 2], False)

    def test_maximum_length(self):
        pushed = list(range(1000))
        popped = pushed[::-1]
        self.verify(pushed, popped, True)
        popped[-2], popped[-1] = popped[-1], popped[-2]
        self.verify(pushed, popped, False)


if __name__ == '__main__':
    unittest.main()
