import unittest

from algorithm.hash.find_unique_binary_string import Solution


class TestFindUniqueBinaryString(unittest.TestCase):
    def _assert_valid(self, nums, ans):
        self.assertEqual(len(ans), len(nums))
        self.assertNotIn(ans, nums)

    def test_diagonal_solution(self):
        s = Solution()
        cases = [
            ["01", "10"],
            ["00", "01"],
            ["111", "011", "001"],
            ["0"],
            ["1"],
        ]
        for nums in cases:
            with self.subTest(nums=nums):
                ans = s.findDifferentBinaryString(nums)
                self._assert_valid(nums, ans)

    def test_set_enumeration_solution(self):
        s = Solution()
        cases = [
            ["01", "10"],
            ["00", "01"],
            ["111", "011", "001"],
            ["0"],
            ["1"],
        ]
        for nums in cases:
            with self.subTest(nums=nums):
                ans = s.findDifferentBinaryStringSet(nums)
                self._assert_valid(nums, ans)


if __name__ == "__main__":
    unittest.main()
