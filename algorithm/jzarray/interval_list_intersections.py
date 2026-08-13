"""leet 986, medium, tags: array, two pointers."""


class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        res = []
        i = j = 0  # O(1) space
        while i < len(firstList) and j < len(secondList):  # O(m+n)
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi:
                res.append([lo, hi])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return res  # Time O(m+n), Space O(1) excluding output
