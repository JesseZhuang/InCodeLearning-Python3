"""leet code 43, medium"""


class Solution:
    """99ms, 16.63mb"""

    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                tmp = res[i + j + 1] + int(num1[i]) * int(num2[j])
                res[i + j] += tmp // 10
                res[i + j + 1] = tmp % 10
        res_s = "".join(map(str, res)).lstrip("0")
        return "0" if not res_s else res_s
