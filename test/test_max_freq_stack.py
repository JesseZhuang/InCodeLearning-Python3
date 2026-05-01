import unittest

from algorithm.deq.max_freq_stack import FreqStack


class TestFreqStack(unittest.TestCase):
    def setUp(self):
        self.solutions = [FreqStack]

    def verify(self, operations, args, expected):
        for cls in self.solutions:
            with self.subTest(sol=cls.__name__):
                obj = None
                for op, arg, exp in zip(operations, args, expected):
                    if op == "FreqStack":
                        obj = cls()
                    elif op == "push":
                        obj.push(arg[0])
                    elif op == "pop":
                        self.assertEqual(exp, obj.pop())

    def test_example1(self):
        """LeetCode example 1."""
        self.verify(
            ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"],
            [[], [5], [7], [5], [7], [4], [5], [], [], [], []],
            [None, None, None, None, None, None, None, 5, 7, 5, 4],
        )

    def test_single_element(self):
        """Single push then pop."""
        self.verify(
            ["FreqStack", "push", "pop"],
            [[], [1], []],
            [None, None, 1],
        )

    def test_all_same(self):
        """All same elements, pop returns them in push order (LIFO at same freq)."""
        self.verify(
            ["FreqStack", "push", "push", "push", "pop", "pop", "pop"],
            [[], [3], [3], [3], [], [], []],
            [None, None, None, None, 3, 3, 3],
        )

    def test_interleaved(self):
        """Push and pop interleaved."""
        self.verify(
            ["FreqStack", "push", "push", "pop", "push", "push", "pop", "pop"],
            [[], [1], [1], [], [1], [2], [], [], []],
            [None, None, None, 1, None, None, 1, 2],
        )


if __name__ == "__main__":
    unittest.main()
