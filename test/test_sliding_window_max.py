import unittest

from algorithm.deq.sliding_window_max import Solution, Solution2


class TestSlidingWindowMax(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution(), Solution2()]

    def test_example1(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        for sol in self.solutions:
            self.assertEqual([3, 3, 5, 5, 6, 7], sol.maxSlidingWindow(nums, 3))

    def test_example2(self):
        for sol in self.solutions:
            self.assertEqual([1], sol.maxSlidingWindow([1], 1))

    def test_k_equals_length(self):
        nums = [4, 2, 7, 1]
        for sol in self.solutions:
            self.assertEqual([7], sol.maxSlidingWindow(nums, 4))

    def test_decreasing(self):
        nums = [9, 8, 7, 6, 5]
        for sol in self.solutions:
            self.assertEqual([9, 8, 7], sol.maxSlidingWindow(nums, 3))

    def test_increasing(self):
        nums = [1, 2, 3, 4, 5]
        for sol in self.solutions:
            self.assertEqual([3, 4, 5], sol.maxSlidingWindow(nums, 3))

    def test_all_same(self):
        nums = [3, 3, 3, 3]
        for sol in self.solutions:
            self.assertEqual([3, 3], sol.maxSlidingWindow(nums, 3))

    def test_negative_values(self):
        nums = [-7, -8, 7, 5, 7, 1, 6, 0]
        for sol in self.solutions:
            self.assertEqual([7, 7, 7, 7, 7, 6], sol.maxSlidingWindow(nums, 3))

    def test_underflow_case(self):
        nums = [9, 10, 9, -7, -4, -8, 2, -6]
        for sol in self.solutions:
            self.assertEqual([10, 10, 9, 2], sol.maxSlidingWindow(nums, 5))


if __name__ == '__main__':
    unittest.main()
