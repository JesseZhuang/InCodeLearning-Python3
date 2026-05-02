import unittest

from algorithm.deq.asteroid_collision import Solution


class TestAsteroidCollision(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def verify(self, asteroids, expected):
        for sol in self.solutions:
            with self.subTest(sol=sol.__class__.__name__):
                self.assertEqual(expected, sol.asteroidCollision(asteroids))

    def test_example1(self):
        self.verify([5, 10, -5], [5, 10])

    def test_example2(self):
        self.verify([8, -8], [])

    def test_example3(self):
        self.verify([10, 2, -5], [10])

    def test_all_positive(self):
        self.verify([1, 2, 3], [1, 2, 3])

    def test_all_negative(self):
        self.verify([-1, -2, -3], [-1, -2, -3])

    def test_single(self):
        self.verify([1], [1])
        self.verify([-1], [-1])

    def test_large_destroys_many(self):
        self.verify([1, 2, 3, -10], [-10])

    def test_negative_then_positive(self):
        self.verify([-2, -1, 1, 2], [-2, -1, 1, 2])

    def test_chain_collisions(self):
        self.verify([10, -5, -10], [])

    def test_alternating(self):
        self.verify([1, -1, 2, -2], [])

    def test_surviving_mix(self):
        self.verify([-2, 1, -1, 2], [-2, 2])
