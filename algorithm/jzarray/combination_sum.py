"""LeetCode 39 Combination Sum"""


class Solution:
    """Backtracking with sort and pruning. O(n^(t/m)) time, O(t/m) space for recursion depth.
    n = len(candidates), t = target, m = min(candidates).
    """

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res: list[list[int]] = []

        def backtrack(start: int, remaining: int, path: list[int]) -> None:
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):  # O(n) branches per level
                if candidates[i] > remaining:  # prune: sorted, so all after are too large
                    break
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i], path)  # same index: allow reuse
                path.pop()

        backtrack(0, target, [])
        return res


class Solution2:
    """Iterative DP building combinations. O(n * t * k) time where k = avg combo length,
    O(t * C) space where C = total number of combinations stored.
    """

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        dp: list[list[list[int]]] = [[] for _ in range(target + 1)]  # dp[s] = combos summing to s
        dp[0] = [[]]
        for c in candidates:  # O(n) candidates
            for s in range(c, target + 1):  # O(t) sums
                for combo in dp[s - c]:  # extend each existing combo
                    dp[s].append(combo + [c])
        return dp[target]
