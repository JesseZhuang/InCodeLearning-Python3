"""leet code 241, medium"""
from functools import cache
from typing import List


class Solution1:
    """38ms, 16.79mb"""

    def __init__(self):
        self.e = None
        self.dp = None

    def diffWaysToCompute(self, expression: str) -> List[int]:
        self.e = expression
        n = len(expression)
        self.dp = [[[] for _ in range(n)] for _ in range(n)]
        self._init_base_cases()
        for length in range(3, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                self._process_subexpression(start, end)

        return self.dp[0][n - 1]

    def _init_base_cases(self) -> None:
        e, dp = self.e, self.dp
        # Handle base cases: single digits and two-digit numbers
        for i, char in enumerate(e):
            if char.isdigit():
                # Check if it's a two-digit number
                dig1 = ord(char) - ord("0")
                if i + 1 < len(e) and e[i + 1].isdigit():
                    dig2 = ord(e[i + 1]) - ord("0")
                    number = dig1 * 10 + dig2
                    dp[i][i + 1].append(number)
                # Single digit case
                dp[i][i].append(dig1)

    def _process_subexpression(self, start: int, end: int) -> None:
        e, dp = self.e, self.dp
        for split in range(start, end + 1):
            if e[split].isdigit(): continue
            l_res = dp[start][split - 1]
            r_res = dp[split + 1][end]
            self._compute_results(e[split], l_res, r_res, dp[start][end])

    def _compute_results(self, op: str, l_res: List[int], r_res: List[int], res: List[int]) -> None:
        for lv in l_res:
            for rv in r_res:
                if op == "+":
                    res.append(lv + rv)
                elif op == "-":
                    res.append(lv - rv)
                elif op == "*":
                    res.append(lv * rv)


class Solution2:
    """42ms, 16.89mb"""

    def diffWaysToCompute(self, expression: str) -> List[int]:
        # memo = {}, # memo[(start, end)] = res
        e = expression

        @cache
        def compute(start: int, end: int) -> List[int]:
            res = []
            if start == end:  # Base case: single digit
                res.append(int(e[start]))
                return res
            if end - start == 1 and e[start].isdigit():  # Base case: two-digit number
                res.append(int(e[start: end + 1]))
                return res
            # Recursive case: split the expression at each operator
            for i in range(start, end + 1):
                if e[i].isdigit(): continue
                l_res = compute(start, i - 1)
                r_res = compute(i + 1, end)
                # Combine res from left and right subexpressions
                for lv in l_res:
                    for rv in r_res:
                        if e[i] == "+":
                            res.append(lv + rv)
                        elif e[i] == "-":
                            res.append(lv - rv)
                        elif e[i] == "*":
                            res.append(lv * rv)
            return res

        return compute(0, len(expression) - 1)
