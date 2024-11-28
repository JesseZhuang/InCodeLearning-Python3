"""leet code 3210, easy"""


class Solution:
    """31ms, 16.62mb"""

    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        res = []
        for i in range(n):
            res.append(s[(i + k) % n])
        return "".join(res)
