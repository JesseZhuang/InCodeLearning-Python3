import unittest

from algorithm.jzarray.gas_station import Solution, Solution2


class TestGasStation(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        for sol in self.solutions:
            self.assertEqual(3, sol.canCompleteCircuit(gas, cost))

    def test_example2(self):
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        for sol in self.solutions:
            self.assertEqual(-1, sol.canCompleteCircuit(gas, cost))

    def test_single_station_pass(self):
        gas = [5]
        cost = [3]
        for sol in self.solutions:
            self.assertEqual(0, sol.canCompleteCircuit(gas, cost))

    def test_single_station_fail(self):
        gas = [3]
        cost = [5]
        for sol in self.solutions:
            self.assertEqual(-1, sol.canCompleteCircuit(gas, cost))

    def test_single_station_exact(self):
        gas = [4]
        cost = [4]
        for sol in self.solutions:
            self.assertEqual(0, sol.canCompleteCircuit(gas, cost))

    def test_all_zeros(self):
        gas = [0, 0, 0]
        cost = [0, 0, 0]
        for sol in self.solutions:
            self.assertEqual(0, sol.canCompleteCircuit(gas, cost))

    def test_start_at_last(self):
        gas = [3, 1, 1]
        cost = [1, 2, 2]
        for sol in self.solutions:
            self.assertEqual(0, sol.canCompleteCircuit(gas, cost))

    def test_large_values(self):
        gas = [10000, 0, 0, 0]
        cost = [0, 5000, 3000, 2000]
        for sol in self.solutions:
            self.assertEqual(0, sol.canCompleteCircuit(gas, cost))


if __name__ == '__main__':
    unittest.main()
