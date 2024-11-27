"""leet code 670, medium"""


class Solution:
    """n,1"""

    def maximumSwap(self, num: int) -> int:
        hd = hi = 0
        ld = li = 0
        cur_hd, cur_hi = -1, 0
        i, res = 1, num
        while num:  # iterate through digits from right to left
            digit = num % 10
            if digit > cur_hd:
                cur_hd, cur_hi = digit, i
            elif digit < cur_hd:
                hd, hi = cur_hd, cur_hi
                ld, li = digit, i
            i *= 10
            num //= 10
        res += hd * (li - hi) + ld * (hi - li)
        return res


class Solution2:
    """n, n"""

    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        max_id, l, r = n - 1, -1, -1
        for i in range(max_id - 1, -1, -1):
            if s[i] > s[max_id]:
                max_id = i
            elif s[i] < s[max_id]:
                l, r = i, max_id
        if l == -1: return num
        s[l], s[r] = s[r], s[l]
        return int(''.join(s))
