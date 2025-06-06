"""leet 2551, medium"""


class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        # We collect and sort the value of all n - 1 pairs.
        n = len(weights)
        pairWeights = [weights[i] + weights[i + 1] for i in range(n - 1)]

        # Since python's sort function sorts the whole list, we don't limit it to the first n-1 elements here.
        pairWeights.sort()

        # Get the difference between the largest k - 1 values and the smallest k - 1 values.
        answer = 0
        for i in range(k - 1):
            answer += pairWeights[n - 2 - i] - pairWeights[i]

        return answer
