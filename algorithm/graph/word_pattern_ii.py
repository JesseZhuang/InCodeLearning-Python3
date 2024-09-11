"""leet code 291, medium, lint code 829"""


class Solution:

    def word_pattern_match(self, pattern: str, s: str) -> bool:
        """
        lint code 225ms, 5.07Mb
        @param pattern: a string,denote pattern string
        @param str: a string, denote matching string
        @return: a boolean
        """
        m, n = len(pattern), len(s)
        char_s = dict()
        marked = set()

        def dfs(i, j):
            if i == m and j == n: return True
            if i == m or j == n or m - i > n - j: return False
            c = pattern[i]
            for end in range(j + 1, n + 1):
                t = s[j:end]
                if char_s.get(c) == t:
                    if dfs(i + 1, end): return True
                if c not in char_s and t not in marked:
                    char_s[c] = t
                    marked.add(t)
                    if dfs(i + 1, end): return True
                    del char_s[c]
                    marked.remove(t)
            return False

        return dfs(0, 0)
