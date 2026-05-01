import unittest

from algorithm.graph.critical_coonection import Solution


class TestCriticalConnection(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        result = self.sol.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]])
        self.assertEqual([[1, 3]], result)

    def test_example2(self):
        result = self.sol.criticalConnections(2, [[0, 1]])
        self.assertEqual([[0, 1]], result)


if __name__ == '__main__':
    unittest.main()
