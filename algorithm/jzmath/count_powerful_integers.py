"""leet 2999, hard"""


class Solution:
    """todo editorial"""

    def numberOfPowerfulInt(
            self, start: int, finish: int, limit: int, s: str
    ) -> int:
        start_ = str(start - 1)
        finish_ = str(finish)
        return self.calculate(finish_, s, limit) - self.calculate(
            start_, s, limit
        )

    def calculate(self, x: str, s: str, limit: int) -> int:
        if len(x) < len(s):
            return 0
        if len(x) == len(s):
            return 1 if x >= s else 0

        suffix = x[len(x) - len(s):]
        count = 0
        pre_len = len(x) - len(s)

        for i in range(pre_len):
            if limit < int(x[i]):
                count += (limit + 1) ** (pre_len - i)
                return count
            count += int(x[i]) * (limit + 1) ** (pre_len - 1 - i)

        if suffix >= s:
            count += 1

        return count
