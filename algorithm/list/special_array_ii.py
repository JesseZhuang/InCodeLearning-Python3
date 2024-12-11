"""leet 3152, medium"""


class Solution:
    """editorial todo, 51 ms, 46.6 mb"""

    def isArraySpecial(
            self, nums: list[int], queries: list[list[int]]
    ) -> list[bool]:
        n = len(nums)
        max_reach = [0] * n
        end = 0

        # Step 1: Compute the maximum reachable index for each starting index
        for start in range(n):
            # Ensure 'end' always starts from the current index or beyond
            end = max(end, start)
            # Expand 'end' as long as adjacent elements have different parity
            while end < n - 1 and nums[end] % 2 != nums[end + 1] % 2:
                end += 1
            # Store the farthest index reachable from 'start'
            max_reach[start] = end

        ans = []

        # Step 2: Answer each query based on precomputed 'max_reach'
        for start, end_query in queries:
            # Check if the query range [start, end] lies within the max reachable range
            ans.append(end_query <= max_reach[start])
        return ans
