"""meeting rooms salesforce"""

from sortedcontainers import SortedDict


def roomsNeeded(meetings: list[list[int]], k: int) -> int:
    res, count = 0, 0
    sd = SortedDict()
    for m in meetings:
        sd.setdefault(m[0], 0)
        sd.setdefault(m[1], 0)
        sd[m[0]] += 1
        sd[m[1]] -= 1
    for c in sd.values():
        count += c
        # res = max(res, ceil(count / k))
        res = max(res, (count - 1) // k + 1)
    return res
