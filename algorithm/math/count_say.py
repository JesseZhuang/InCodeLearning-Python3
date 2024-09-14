"""leet code 38, medium"""


class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        while n > 1:
            nex = []
            i = 0  ## 1121->211211
            while i < len(res):
                count = 1
                while i + 1 < len(res) and res[i] == res[i + 1]:
                    count += 1
                    i += 1
                nex.append(str(count))
                nex.append(res[i])
                i += 1
            res = "".join(nex)
            n -= 1
        return res
