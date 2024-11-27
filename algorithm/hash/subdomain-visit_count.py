"""leet code 811, medium"""
import collections


class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        cnt = collections.Counter()
        for cpd in cpdomains:
            n, d = cpd.split()
            n = int(n)
            cnt[d] += n
            for i, c in enumerate(d):
                if c != '.': continue
                cnt[d[i + 1:]] += n
        return [f'{cnt[k]} {k}' for k in cnt]
