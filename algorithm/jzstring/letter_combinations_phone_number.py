"""leet 17, medium, tags: hash table, string, backtracking."""


class Solution:
    """Iterative BFS-like approach. Time O(n * 4^n), Space O(4^n) where n is len(digits)."""

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        mapping = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = [""]
        for d in digits:  # O(n)
            letters = mapping[int(d) - 2]
            res = [prefix + c for prefix in res for c in letters]  # O(4^n) combinations
        return res


class Solution2:
    """Backtracking approach. Time O(n * 4^n), Space O(n) recursion + O(4^n) result."""

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        mapping = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []

        def backtrack(i: int, path: list[str]) -> None:
            if i == len(digits):
                res.append("".join(path))
                return
            for c in mapping[int(digits[i]) - 2]:  # O(3 or 4) letters per digit
                path.append(c)
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
