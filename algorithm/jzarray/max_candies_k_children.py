"""leet 2226, medium"""


class Solution:
    """todo editorial"""

    def maximumCandies(self, candies, k):
        # Find the maximum number of candies in any pile
        max_candies_in_pile = 0
        for candy in candies:
            max_candies_in_pile = max(max_candies_in_pile, candy)

        # Set the initial search range for binary search
        left = 0
        right = max_candies_in_pile

        # Binary search to find the maximum number of candies each child can get
        while left < right:
            # Calculate the middle value of the current range
            middle = (left + right + 1) // 2

            # Check if it's possible to allocate candies so that each child gets 'middle' candies
            if self._can_allocate_candies(candies, k, middle):
                # If possible, move to the upper half to search for a larger number
                left = middle
            else:
                # Otherwise, move to the lower half
                right = middle - 1

        return left

    def _can_allocate_candies(self, candies, k, num_of_candies):
        # Initialize the total number of children that can be served
        max_num_of_children = 0

        # Iterate over all piles to calculate how many children each pile can serve
        for pile in candies:
            max_num_of_children += pile // num_of_candies

        return max_num_of_children >= k
