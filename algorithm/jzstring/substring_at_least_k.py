"""lint code 1375, medium"""

from collections import defaultdict


class Solution:
    """
    385ms, 5.27mb
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """

    def k_distinct_characters(self, s: str, k: int) -> int:
        char_cnt = defaultdict(int)
        res, r, n = 0, 0, len(s)
        for l in range(n):
            while r < n and len(char_cnt) < k:
                char_cnt[s[r]] += 1
                r += 1
            if len(char_cnt) == k: res += n - r + 1
            ch = s[l]
            cnt = char_cnt[ch]
            if cnt == 1:
                del char_cnt[ch]
            else:
                char_cnt[ch] -= 1
        return res
