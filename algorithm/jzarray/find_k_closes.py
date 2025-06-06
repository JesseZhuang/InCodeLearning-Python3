"""leet 658, medium"""


class Solution:
    """0 ms, 18.95 mb. @lee215"""

    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        l, r = 0, len(arr) - k
        while l < r:
            mid = l + (r - l) // 2
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
        return arr[l:l + k]
