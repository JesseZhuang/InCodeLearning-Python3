class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """Binary search on shorter array. O(log(min(m,n))) time, O(1) space."""
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2  # O(log(min(m,n))) binary search iterations
            j = (m + n + 1) // 2 - i
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            right2 = nums2[j] if j < n else float('inf')
            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return max(left1, left2)
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                hi = i - 1
            else:
                lo = i + 1
        return -1.0


class Solution2:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """Merge and find median. O(m+n) time, O(m+n) space."""
        merged = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):  # O(m+n)
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        n = len(merged)
        if n % 2 == 1:
            return merged[n // 2]
        return (merged[n // 2 - 1] + merged[n // 2]) / 2
