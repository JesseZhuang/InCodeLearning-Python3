"""leet code 1980, medium"""

from typing import List


class Solution:
    """Diagonal-flip construction."""

    # 0ms 19.33mb
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        res: List[str] = []
        for i in range(n):
            c = nums[i][i]
            res.append("1" if c == "0" else "0")
        return "".join(res)

    # 0ms 19.17mb
    def findDifferentBinaryStringSet(self, nums: List[str]) -> str:
        """Set + enumeration."""
        n = len(nums)
        seen = set(nums)
        for mask in range(1 << n):
            res = f"{mask:0{n}b}"
            if res not in seen:
                return res
        return ""


def _run_examples() -> None:
    s = Solution()

    # Example 1
    nums1 = ["01", "10"]
    res1 = s.findDifferentBinaryString(nums1)
    assert len(res1) == len(nums1)
    assert res1 not in nums1

    # Example 2
    nums2 = ["00", "01"]
    res2 = s.findDifferentBinaryString(nums2)
    assert len(res2) == len(nums2)
    assert res2 not in nums2

    # Example 3
    nums3 = ["111", "011", "001"]
    res3 = s.findDifferentBinaryString(nums3)
    assert len(res3) == len(nums3)
    assert res3 not in nums3

    # Edge cases: n = 1
    nums4 = ["0"]
    res4 = s.findDifferentBinaryString(nums4)
    assert len(res4) == len(nums4)
    assert res4 not in nums4

    nums5 = ["1"]
    res5 = s.findDifferentBinaryString(nums5)
    assert len(res5) == len(nums5)
    assert res5 not in nums5

    print("All local tests passed.")


if __name__ == "__main__":
    _run_examples()
