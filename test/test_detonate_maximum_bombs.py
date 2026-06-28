import unittest

from algorithm.graph.detonate_maximum_bombs import Solution, Solution2


class TestDetonateMaximumBombs(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        bombs = [[2, 1, 3], [6, 1, 4]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.maximumDetonation(bombs), 2)

    def test_example2(self):
        bombs = [[1, 1, 5], [10, 10, 5]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.maximumDetonation(bombs), 1)

    def test_example3(self):
        bombs = [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.maximumDetonation(bombs), 5)

    def test_single_bomb(self):
        bombs = [[0, 0, 1]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.maximumDetonation(bombs), 1)

    def test_no_chain(self):
        bombs = [[1, 1, 1], [100, 100, 1], [200, 200, 1]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.maximumDetonation(bombs), 1)

    def test_one_directional(self):
        # bomb 0 has large radius reaching bomb 1, but bomb 1 cannot reach bomb 0
        bombs = [[0, 0, 10], [5, 0, 1]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.maximumDetonation(bombs), 2)
                # starting from bomb 1 can only detonate itself
                # but starting from bomb 0 detonates both

    def test_exact_boundary(self):
        # distance = 5, radius = 5, should reach (on boundary)
        bombs = [[0, 0, 5], [3, 4, 1]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.maximumDetonation(bombs), 2)

    def test_chain_reaction(self):
        # chain: 0 -> 1 -> 2, but 0 cannot directly reach 2
        bombs = [[0, 0, 2], [1, 0, 2], [3, 0, 1]]
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(sol.maximumDetonation(bombs), 3)


if __name__ == '__main__':
    unittest.main()
