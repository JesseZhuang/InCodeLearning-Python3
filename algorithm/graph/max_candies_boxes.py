"""leet code 1298, hard"""

from collections import deque
from typing import List


class Solution:
    """BFS. O(n^2) time (keys can repeat across boxes), O(n) space."""

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]],
                   containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        has_box = [False] * n
        opened = [False] * n
        has_key = list(status)  # open boxes are as good as having a key
        res = 0
        q = deque()
        for b in initialBoxes:
            has_box[b] = True
            if has_key[b]:
                q.append(b)
                opened[b] = True
        while q:
            box = q.popleft()
            res += candies[box]
            for k in keys[box]:
                if not has_key[k]:
                    has_key[k] = True
                    if has_box[k] and not opened[k]:
                        opened[k] = True
                        q.append(k)
            for b in containedBoxes[box]:
                has_box[b] = True
                if not opened[b] and has_key[b]:
                    opened[b] = True
                    q.append(b)
        return res
