'''leet code 217 easy'''


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''403ms, 31.97Mb'''
        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False
