"""lint 637, leet 408, medium"""


class Solution:
    """81 ms, 5.14 mb"""

    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n, m = map(len, (word, abbr))
        i = j = x = 0
        while i < n and j < m:
            if abbr[j].isdigit():
                if abbr[j] == '0' and x == 0:
                    return False
                x = x * 10 + int(abbr[j])
            else:
                i += x
                x = 0
                if i >= n or word[i] != abbr[j]:
                    return False
                i += 1
            j += 1
        return i + x == n and j == m
