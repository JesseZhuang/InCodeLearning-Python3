from functools import cmp_to_key
from sortedcontainers import SortedDict  # important


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        res = list()
        v_lines = list()
        for b in buildings:
            v_lines.append((b[0], b[2]))
            v_lines.append((b[1], -b[2]))

        def cmp(l1, l2):
            if l1[0] == l2[0]:
                return l2[1] - l1[1]
            else:
                return l1[0] - l2[0]
        v_lines.sort(key=cmp_to_key(cmp))
        b_edges = SortedDict()
        b_edges[0] = 1
        prev = 0
        for l in v_lines:
            if l[1] > 0:
                b_edges[l[1]] = b_edges.get(l[1], 0) + 1
            else:
                c = b_edges[-l[1]]
                if c == 1:
                    del b_edges[-l[1]]
                else:
                    b_edges[-l[1]] -= 1
            cur_h = b_edges.peekitem()[0]  # remember item (k,v)
            if cur_h != prev:
                res.append([l[0], cur_h])
                prev = cur_h
        return res
