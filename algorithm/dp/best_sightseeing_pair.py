"""leet 1014, medium"""


class Solution:
    """todo editorial"""

    def maxScoreSightseeingPair(self, values):
        n = len(values)

        # The left score is initially just the value of the first element.
        max_left_score = values[0]

        max_score = 0

        for i in range(1, n):
            current_right_score = values[i] - i
            # Update the maximum score by combining the best left score so far with the current right score.
            max_score = max(max_score, max_left_score + current_right_score)

            current_left_score = values[i] + i
            # Update the maximum left score up to the current index.
            max_left_score = max(max_left_score, current_left_score)

        return max_score
