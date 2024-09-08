"""leet code 767, medium"""

import heapq
from collections import Counter


class Solution1:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        char_cnt = [(-counter[c], c) for c in counter]
        heapq.heapify(char_cnt)

        res, prev = [], None
        while char_cnt:
            _, c = heapq.heappop(char_cnt)
            res.append(c)
            counter[c] -= 1
            if prev and counter[prev] > 0: heapq.heappush(char_cnt, (-counter[prev], prev))
            prev = c
        if counter[prev] == 0:
            return "".join(res)
        else:
            return ""


class Solution2:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s).most_common()  # sorting in most_common()
        n = len(s)
        if counts[0][1] > (n + 1) // 2: return ""
        res, i = [""] * n, 0
        for c, cnt in counts:
            for j in range(cnt):
                res[i] = c
                i += 2
                if i >= n: i = 1
        return "".join(res)
