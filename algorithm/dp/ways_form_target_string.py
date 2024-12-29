"""leet 1639, hard"""


class Solution:
    """todo editorial """

    def numWays(self, words: list[str], target: str) -> int:
        MOD = 1000000007
        word_length = len(words[0])
        target_length = len(target)
        char_frequency = [[0] * 26 for _ in range(word_length)]

        # Step 1: Calculate frequency of each character at every index in "words".
        for word in words:
            for j in range(word_length):
                char_frequency[j][ord(word[j]) - ord("a")] += 1

        # Step 2: Initialize two DP arrays: prev_count and curr_count.
        prev_count = [0] * (target_length + 1)
        curr_count = [0] * (target_length + 1)

        # Base case: There is one way to form an empty target string.
        prev_count[0] = 1

        # Step 3: Fill the DP arrays.
        for curr_word in range(1, word_length + 1):
            curr_count = prev_count.copy()
            for curr_target in range(1, target_length + 1):
                cur_pos = ord(target[curr_target - 1]) - ord("a")

                # If characters match, add the number of ways.
                curr_count[curr_target] += (
                                                   char_frequency[curr_word - 1][cur_pos]
                                                   * prev_count[curr_target - 1]
                                           ) % MOD
                curr_count[curr_target] %= MOD

            # Move current row to previous row for the next iteration.
            prev_count = curr_count.copy()

        # Step 4: The result is in prev[target_length].
        return curr_count[target_length]
