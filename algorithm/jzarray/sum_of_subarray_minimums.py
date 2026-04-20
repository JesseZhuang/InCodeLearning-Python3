"""LeetCode 907, medium, tags: array, dynamic programming, stack, monotonic stack."""

MOD = 10**9 + 7


class Solution:
    """Monotonic stack. O(n) time, O(n) space."""

    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)
        # left[i]: number of subarrays ending at i where arr[i] is the minimum
        # right[i]: number of subarrays starting at i where arr[i] is the minimum
        left = [0] * n  # distance to previous less-or-equal element
        right = [0] * n  # distance to next strictly less element
        stack: list[int] = []

        # For each element, find how far left it can extend as the minimum
        for i in range(n):  # O(n), each element pushed/popped at most once
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)

        stack.clear()

        # For each element, find how far right it can extend as the minimum
        for i in range(n - 1, -1, -1):  # O(n)
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)

        # Contribution of arr[i] = arr[i] * left[i] * right[i]
        result = 0
        for i in range(n):  # O(n)
            result = (result + arr[i] * left[i] * right[i]) % MOD
        return result


class Solution2:
    """Monotonic stack single pass with sentinel. O(n) time, O(n) space."""

    def sumSubarrayMins(self, arr: list[int]) -> int:
        result = 0
        stack: list[int] = []  # indices, monotonically increasing values
        arr = [0] + arr + [0]  # sentinels to flush the stack

        for i, val in enumerate(arr):  # O(n), each index pushed/popped once
            while stack and arr[stack[-1]] > val:
                mid = stack.pop()
                left = mid - stack[-1]  # distance to previous <= element
                right = i - mid  # distance to next < element
                result = (result + arr[mid] * left * right) % MOD
            stack.append(i)

        return result
