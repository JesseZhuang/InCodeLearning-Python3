"""leet code 38, medium"""


class Solution:
    """7 ms, 16.67 mb"""

    def countAndSay(self, n: int) -> str:
        res = "1"
        while n > 1:
            tmp, i, m = [], 0, len(res)
            while i < m:
                count = 1
                while i + 1 < m and res[i] == res[i + 1]:
                    count += 1
                    i += 1
                tmp.append(str(count))
                tmp.append(res[i])
                i += 1
            res = "".join(tmp)  # 1121->211211
            n -= 1
        return res
