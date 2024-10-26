"""biweekly 142 Q1, leet code 3330"""


class SolutionQ1:
    def possibleStringCount(self, word: str) -> int:
        res, i, n = 1, 0, len(word)
        while i < n:
            j = i
            while j < n and word[i] == word[j]:
                j += 1
            res += j - i - 1
            i = j
        return res
