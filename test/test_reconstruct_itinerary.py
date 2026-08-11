import unittest

from algorithm.graph.reconstruct_itinerary import Solution, Solution2


class TestReconstructItinerary(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        expected = ["JFK", "MUC", "LHR", "SFO", "SJC"]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.findItinerary(tickets), expected)

    def test_example2(self):
        tickets = [
            ["JFK", "SFO"],
            ["JFK", "ATL"],
            ["SFO", "ATL"],
            ["ATL", "JFK"],
            ["ATL", "SFO"],
        ]
        expected = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.findItinerary(tickets), expected)

    def test_single_ticket(self):
        tickets = [["JFK", "A"]]
        expected = ["JFK", "A"]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.findItinerary(tickets), expected)

    def test_lexical_order(self):
        tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
        expected = ["JFK", "NRT", "JFK", "KUL"]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.findItinerary(tickets), expected)

    def test_multiple_edges_same_pair(self):
        tickets = [["JFK", "A"], ["A", "JFK"], ["JFK", "A"]]
        expected = ["JFK", "A", "JFK", "A"]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.findItinerary(tickets), expected)


if __name__ == "__main__":
    unittest.main()
