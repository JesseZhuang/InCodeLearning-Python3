"""hackerrank programmer strings, companies: salesforce"""

from collections import Counter

PG = Counter('programmer')


def programmerStrings(s: str) -> int:
    e1, s2 = 0, 0
    c2 = Counter()
    for i, c in enumerate(s):
        if c not in PG: continue
        c2[c] += 1
        if PG <= c2:
            e1 = i
            break
    c2.clear()
    for i in range(len(s) - 1, -1, -1):
        if s[i] not in PG: continue
        c2[s[i]] += 1
        if PG <= c2:
            s2 = i
            break
    return s2 - e1 - 1
