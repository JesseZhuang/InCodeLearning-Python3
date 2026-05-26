import unittest

from algorithm.graph.network_delay_time import Solution, Solution2


class TestNetworkDelayTime(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        for sol in self.solutions:
            self.assertEqual(2, sol.networkDelayTime(times, 4, 2))

    def test_example2(self):
        times = [[1, 2, 1]]
        for sol in self.solutions:
            self.assertEqual(1, sol.networkDelayTime(times, 2, 1))

    def test_unreachable(self):
        times = [[1, 2, 1]]
        for sol in self.solutions:
            self.assertEqual(-1, sol.networkDelayTime(times, 2, 2))

    def test_single_node(self):
        for sol in self.solutions:
            self.assertEqual(0, sol.networkDelayTime([], 1, 1))

    def test_multiple_paths(self):
        # 1->2 cost 1, 1->3 cost 4, 2->3 cost 2 => shortest to 3 is 1+2=3
        times = [[1, 2, 1], [1, 3, 4], [2, 3, 2]]
        for sol in self.solutions:
            self.assertEqual(3, sol.networkDelayTime(times, 3, 1))

    def test_all_zero_weight(self):
        times = [[1, 2, 0], [2, 3, 0], [3, 4, 0]]
        for sol in self.solutions:
            self.assertEqual(0, sol.networkDelayTime(times, 4, 1))

    def test_disconnected(self):
        # node 3 is unreachable from node 1
        times = [[1, 2, 1], [3, 2, 1]]
        for sol in self.solutions:
            self.assertEqual(-1, sol.networkDelayTime(times, 3, 1))


if __name__ == '__main__':
    unittest.main()
