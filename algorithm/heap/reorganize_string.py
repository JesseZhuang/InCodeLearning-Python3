"""leet code 767, medium"""

import heapq
from collections import Counter, defaultdict


class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = defaultdict(int)
        max_c, max_cnt, n = None, 0, len(s)
        for c in s:
            counts[c] += 1
            if counts[c] > max_cnt:
                max_c, max_cnt = c, counts[c]
        if max_cnt > (n + 1) // 2:
            return ''
        i = 0
        res = [''] * n
        while counts[max_c] > 0:
            res[i] = max_c
            i += 2
            counts[max_c] -= 1
        for c in counts:
            while counts[c] > 0:
                if i > n - 1:
                    i = 1
                res[i] = c
                i += 2
                counts[c] -= 1

        return ''.join(res)


class Solution2:
    def reorganizeString(self, s: str) -> str:
        # Counter returns a Counter object, most_common() returns a list
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


class Solution3:
    def reorganizeString(self, s: str) -> str:
        """36ms, 16.62mb"""
        counter = Counter(s)
        char_cnt = [(-counter[c], c) for c in counter]
        heapq.heapify(char_cnt)
        if -char_cnt[0][0] > (len(s) + 1) // 2: return ""

        res, prev = [], None
        while char_cnt:
            _, c = heapq.heappop(char_cnt)
            res.append(c)
            counter[c] -= 1
            if prev and counter[prev] > 0: heapq.heappush(char_cnt, (-counter[prev], prev))
            prev = c
        return "".join(res)
