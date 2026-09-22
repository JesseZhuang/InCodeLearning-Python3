from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """Boyer-Moore Voting extended to n/3. O(n) time, O(1) space.

        At most 2 elements can appear more than ⌊n/3⌋ times.
        Phase 1: find up to 2 candidates.
        Phase 2: verify each candidate's actual count.
        """
        c1 = c2 = 0
        n1 = n2 = None
        for num in nums:  # O(n)
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
            elif c1 == 0:
                n1, c1 = num, 1
            elif c2 == 0:
                n2, c2 = num, 1
            else:
                c1 -= 1
                c2 -= 1
        # O(n) verification pass
        threshold = len(nums) // 3
        return [n for n in (n1, n2) if n is not None and nums.count(n) > threshold]

    def majorityElementMap(self, nums: List[int]) -> List[int]:
        """HashMap counting. O(n) time, O(n) space."""
        counts = {}
        threshold = len(nums) // 3
        for num in nums:  # O(n)
            counts[num] = counts.get(num, 0) + 1  # O(1) per insert
        return [num for num, cnt in counts.items() if cnt > threshold]
