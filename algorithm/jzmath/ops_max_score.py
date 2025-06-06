"""leet 2818, medium"""
import heapq
import math


class Solution:
    MOD = 10 ** 9 + 7

    def maximumScore(self, nums, k):
        n = len(nums)
        prime_scores = [0] * n

        # Calculate the prime score for each number in nums
        for index in range(n):
            num = nums[index]

            # Check for prime factors from 2 to sqrt(n)
            for factor in range(2, int(math.sqrt(num)) + 1):
                if num % factor == 0:
                    # Increment prime score for each prime factor
                    prime_scores[index] += 1

                    # Remove all occurrences of the prime factor from num
                    while num % factor == 0:
                        num //= factor

            # If num is still greater than or equal to 2, it's a prime factor
            if num >= 2:
                prime_scores[index] += 1

        # Initialize next and previous dominant index arrays
        next_dominant = [n] * n
        prev_dominant = [-1] * n

        # Stack to store indices for monotonic decreasing prime score
        decreasing_prime_score_stack = []

        # Calculate the next and previous dominant indices for each number
        for index in range(n):
            # While the stack is not empty and the current prime score is greater than the stack's top
            while (
                    decreasing_prime_score_stack
                    and prime_scores[decreasing_prime_score_stack[-1]]
                    < prime_scores[index]
            ):
                top_index = decreasing_prime_score_stack.pop()

                # Set the next dominant element for the popped index
                next_dominant[top_index] = index

            # If the stack is not empty, set the previous dominant element for the current index
            if decreasing_prime_score_stack:
                prev_dominant[index] = decreasing_prime_score_stack[-1]

            # Push the current index onto the stack
            decreasing_prime_score_stack.append(index)

        # Calculate the number of subarrays in which each element is dominant
        num_of_subarrays = [0] * n
        for index in range(n):
            num_of_subarrays[index] = (next_dominant[index] - index) * (
                    index - prev_dominant[index]
            )

        # Priority queue to process elements in decreasing order of their value
        processing_queue = []

        # Push each number and its index onto the priority queue
        for index in range(n):
            heapq.heappush(processing_queue, (-nums[index], index))

        score = 1

        # Helper function to compute the power of a number modulo MOD
        def _power(base, exponent):
            res = 1

            # Calculate the exponentiation using binary exponentiation
            while exponent > 0:
                # If the exponent is odd, multiply the result by the base
                if exponent % 2 == 1:
                    res = (res * base) % self.MOD

                # Square the base and halve the exponent
                base = (base * base) % self.MOD
                exponent //= 2

            return res

        # Process elements while there are operations left
        while k > 0:
            # Get the element with the maximum value from the queue
            num, index = heapq.heappop(processing_queue)
            num = -num  # Negate back to positive

            # Calculate the number of operations to apply on the current element
            operations = min(k, num_of_subarrays[index])

            # Update the score by raising the element to the power of operations
            score = (score * _power(num, operations)) % self.MOD

            # Reduce the remaining operations count
            k -= operations

        return score
