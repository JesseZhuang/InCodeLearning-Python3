import unittest

from algorithm.deq.min_stack import MinStack, MinStackSingleStack


class TestMinStack(unittest.TestCase):
    def setUp(self):
        self.solutions = [MinStack, MinStackSingleStack]

    def verify(self, operations, args, expected):
        for cls in self.solutions:
            with self.subTest(sol=cls.__name__):
                obj = None
                for op, arg, exp in zip(operations, args, expected):
                    if op == "MinStack":
                        obj = cls()
                    elif op == "push":
                        obj.push(arg[0])
                    elif op == "pop":
                        obj.pop()
                    elif op == "top":
                        self.assertEqual(exp, obj.top())
                    elif op == "getMin":
                        self.assertEqual(exp, obj.getMin())

    def test_example1(self):
        """LeetCode example 1."""
        self.verify(
            ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
            [[], [-2], [0], [-3], [], [], [], []],
            [None, None, None, None, -3, None, 0, -2],
        )

    def test_single_element(self):
        self.verify(
            ["MinStack", "push", "top", "getMin"],
            [[], [42], [], []],
            [None, None, 42, 42],
        )

    def test_all_same(self):
        self.verify(
            ["MinStack", "push", "push", "push", "getMin", "pop", "getMin"],
            [[], [5], [5], [5], [], [], []],
            [None, None, None, None, 5, None, 5],
        )

    def test_decreasing_then_pop(self):
        self.verify(
            ["MinStack", "push", "push", "push", "getMin", "pop", "getMin", "pop", "getMin"],
            [[], [3], [2], [1], [], [], [], [], []],
            [None, None, None, None, 1, None, 2, None, 3],
        )

    def test_negative_values(self):
        self.verify(
            ["MinStack", "push", "push", "getMin", "push", "getMin", "pop", "getMin"],
            [[], [-1], [-2], [], [0], [], [], []],
            [None, None, None, -2, None, -2, None, -2],
        )

    def test_large_then_small(self):
        self.verify(
            ["MinStack", "push", "push", "getMin", "pop", "getMin"],
            [[], [1000], [-1000], [], [], []],
            [None, None, None, -1000, None, 1000],
        )
