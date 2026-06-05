import unittest

from algorithm.graph.cheapest_flights_within_k_stops import Solution, Solution2


class TestCheapestFlights(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        # 0->1->2->3, k=1 means at most 1 stop
        n, flights, src, dst, k = 4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1
        for sol in self.solutions:
            self.assertEqual(sol.findCheapestPrice(n, flights, src, dst, k), 700)

    def test_example2(self):
        n, flights, src, dst, k = 3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1
        for sol in self.solutions:
            self.assertEqual(sol.findCheapestPrice(n, flights, src, dst, k), 200)

    def test_example3(self):
        n, flights, src, dst, k = 3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0
        for sol in self.solutions:
            self.assertEqual(sol.findCheapestPrice(n, flights, src, dst, k), 500)

    def test_no_path(self):
        n, flights, src, dst, k = 3, [[0, 1, 100]], 0, 2, 1
        for sol in self.solutions:
            self.assertEqual(sol.findCheapestPrice(n, flights, src, dst, k), -1)

    def test_direct_flight(self):
        n, flights, src, dst, k = 2, [[0, 1, 50]], 0, 1, 0
        for sol in self.solutions:
            self.assertEqual(sol.findCheapestPrice(n, flights, src, dst, k), 50)

    def test_k_limits_cheaper_path(self):
        # Cheaper path 0->1->2->3 costs 300 (2 stops), but k=1 forces 0->1->3 = 600
        n = 4
        flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [1, 3, 500]]
        for sol in self.solutions:
            self.assertEqual(sol.findCheapestPrice(n, flights, 0, 3, 1), 600)
            self.assertEqual(sol.findCheapestPrice(n, flights, 0, 3, 2), 300)

    def test_single_node(self):
        n, flights, src, dst, k = 1, [], 0, 0, 0
        for sol in self.solutions:
            self.assertEqual(sol.findCheapestPrice(n, flights, src, dst, k), 0)


if __name__ == "__main__":
    unittest.main()
