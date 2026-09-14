from collections import defaultdict


class Solution:
    # lc 904, sliding window + hash map, O(n) time, O(1) space (at most 3 keys).
    def totalFruit(self, fruits: list[int]) -> int:
        cnt, left, res = defaultdict(int), 0, 0
        for right, f in enumerate(fruits):  # O(n), each element enters/exits window once
            cnt[f] += 1
            while len(cnt) > 2:  # shrink until at most 2 types
                lf = fruits[left]
                cnt[lf] -= 1
                if cnt[lf] == 0:
                    del cnt[lf]
                left += 1
            res = max(res, right - left + 1)
        return res


class Solution2:
    # lc 904, track last two types, O(n) time, O(1) space.
    def totalFruit(self, fruits: list[int]) -> int:
        res = cur = count_b = 0
        a = b = -1
        for f in fruits:
            if f == a or f == b:
                cur += 1
            else:
                cur = count_b + 1  # reset: keep only consecutive run of b + this new fruit
            if f == b:
                count_b += 1
            else:
                count_b = 1
                a, b = b, f
            res = max(res, cur)
        return res
