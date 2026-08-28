import unittest

from algorithm.binary_search.flowers_in_full_bloom import Solution, Solution2


class TestFlowersInFullBloom(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        flowers = [[1, 6], [3, 7], [9, 12], [4, 13]]
        people = [2, 3, 7, 11]
        for sol in self.solutions:
            self.assertEqual(sol.fullBloomFlowers(flowers, people), [1, 2, 2, 2])

    def test_example2(self):
        flowers = [[1, 10], [3, 3]]
        people = [3, 3, 2]
        for sol in self.solutions:
            self.assertEqual(sol.fullBloomFlowers(flowers, people), [2, 2, 1])

    def test_single_flower_single_person_inside(self):
        flowers = [[5, 10]]
        people = [7]
        for sol in self.solutions:
            self.assertEqual(sol.fullBloomFlowers(flowers, people), [1])

    def test_single_flower_single_person_outside(self):
        flowers = [[5, 10]]
        people = [11]
        for sol in self.solutions:
            self.assertEqual(sol.fullBloomFlowers(flowers, people), [0])

    def test_person_at_boundary(self):
        flowers = [[1, 5], [5, 10]]
        people = [5]
        for sol in self.solutions:
            self.assertEqual(sol.fullBloomFlowers(flowers, people), [2])

    def test_no_flowers_blooming(self):
        flowers = [[1, 2], [3, 4]]
        people = [5, 6]
        for sol in self.solutions:
            self.assertEqual(sol.fullBloomFlowers(flowers, people), [0, 0])

    def test_all_flowers_blooming(self):
        flowers = [[1, 10], [2, 10], [3, 10]]
        people = [5]
        for sol in self.solutions:
            self.assertEqual(sol.fullBloomFlowers(flowers, people), [3])

    def test_person_before_all_flowers(self):
        flowers = [[5, 10], [6, 12]]
        people = [1]
        for sol in self.solutions:
            self.assertEqual(sol.fullBloomFlowers(flowers, people), [0])

    def test_large_range(self):
        flowers = [[1, 1000000000]]
        people = [1, 500000000, 1000000000, 1000000001]
        for sol in self.solutions:
            self.assertEqual(sol.fullBloomFlowers(flowers, people), [1, 1, 1, 0])

    def test_duplicate_people_times(self):
        flowers = [[1, 3], [2, 5]]
        people = [2, 2, 2]
        for sol in self.solutions:
            self.assertEqual(sol.fullBloomFlowers(flowers, people), [2, 2, 2])


if __name__ == "__main__":
    unittest.main()
