import unittest

from algorithm.graph.shortest_alternating_paths import Solution


class TestShortestAlternatingPaths(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_same_color_edges_cannot_be_used_consecutively(self):
        for solution in self.solutions:
            self.assertEqual(
                solution.shortestAlternatingPaths(3, [[0, 1], [1, 2]], []),
                [0, 1, -1],
            )

    def test_path_can_start_with_either_color_and_alternate(self):
        for solution in self.solutions:
            self.assertEqual(
                solution.shortestAlternatingPaths(3, [[1, 2]], [[0, 1]]),
                [0, 1, 2],
            )

    def test_visited_state_includes_the_last_edge_color(self):
        red_edges = [[0, 1], [1, 2]]
        blue_edges = [[0, 1], [1, 3]]
        for solution in self.solutions:
            self.assertEqual(
                solution.shortestAlternatingPaths(4, red_edges, blue_edges),
                [0, 1, 2, 2],
            )

    def test_single_node_duplicate_edges_and_cycle(self):
        for solution in self.solutions:
            self.assertEqual(solution.shortestAlternatingPaths(1, [], []), [0])
            self.assertEqual(
                solution.shortestAlternatingPaths(
                    3,
                    [[0, 1], [0, 1], [2, 0]],
                    [[1, 2], [2, 0]],
                ),
                [0, 1, 2],
            )


if __name__ == "__main__":
    unittest.main()
