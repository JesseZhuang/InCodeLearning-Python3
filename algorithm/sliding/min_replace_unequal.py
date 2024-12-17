"""gfg, hackerrank, medium"""


def minReplaceUnequal(s: str) -> int:
    i, res, n = 0, 0, len(s)
    while i < n:
        streak = 1
        while i + 1 < n and s[i] == s[i + 1]:
            i += 1
            streak += 1
        res += streak // 2
        i += 1
    return res
