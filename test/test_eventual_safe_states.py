import unittest

from algorithm.graph.eventual_safe_states import Solution


class TestEventualSafeStates(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        self.methods = [self.sol.eventualSafeNodes, self.sol.eventualSafeNodesBFS]

    def verify(self, graph, expected):
        for method in self.methods:
            with self.subTest(method=method.__name__):
                self.assertEqual(method(graph), expected)

    def test_example1(self):
        self.verify([[1, 2], [2, 3], [5], [0], [5], [], []], [2, 4, 5, 6])

    def test_example2(self):
        self.verify([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []], [4])

    def test_all_terminal(self):
        self.verify([[], [], []], [0, 1, 2])

    def test_single_node(self):
        self.verify([[]], [0])

    def test_self_loop(self):
        self.verify([[0]], [])

    def test_two_node_cycle(self):
        self.verify([[1], [0]], [])

    def test_chain_to_terminal(self):
        self.verify([[1], [2], []], [0, 1, 2])

    def test_mixed_safe_and_cycle(self):
        # 0->1->2->0 (cycle), 3->4->[] (safe chain)
        self.verify([[1], [2], [0], [4], []], [3, 4])

    def test_node_leading_to_both_safe_and_cycle(self):
        # 0->1 (cycle 1->2->1), 0->3 (safe 3->[])
        # 0 is NOT safe because path 0->1->2->1... never terminates
        self.verify([[1, 3], [2], [1], []], [3])

    def test_large_linear(self):
        n = 100
        graph = [[i + 1] for i in range(n - 1)] + [[]]
        self.verify(graph, list(range(n)))
