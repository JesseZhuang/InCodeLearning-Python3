"""LeetCode 40 Combination Sum II"""


class Solution:
    """Backtracking with sort and skip duplicates. O(2^n) time, O(n) space for recursion depth.
    n = len(candidates).
    """

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()  # O(n log n)
        res: list[list[int]] = []

        def backtrack(start: int, remaining: int, path: list[int]) -> None:
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):  # O(n) branches per level
                if candidates[i] > remaining:  # prune: sorted, rest too large
                    break
                if i > start and candidates[i] == candidates[i - 1]:  # skip duplicates at same level
                    continue
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], path)  # i+1: each element used once
                path.pop()

        backtrack(0, target, [])
        return res


class Solution2:
    """Counter-based backtracking. O(2^n) time, O(n) space.
    Uses frequency map instead of sorting to handle duplicates.
    """

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        from collections import Counter
        counter = Counter(candidates)
        unique = sorted(counter.keys())  # O(u log u) where u = unique count
        res: list[list[int]] = []

        def backtrack(idx: int, remaining: int, path: list[int]) -> None:
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(idx, len(unique)):  # O(u) branches
                c = unique[i]
                if c > remaining:  # prune
                    break
                orig_len = len(path)
                for count in range(1, counter[c] + 1):  # try 1..freq copies of c
                    if c * count > remaining:  # prune
                        break
                    path.append(c)
                    backtrack(i + 1, remaining - c * count, path)
                del path[orig_len:]  # remove all appended copies of c

        backtrack(0, target, [])
        return res
