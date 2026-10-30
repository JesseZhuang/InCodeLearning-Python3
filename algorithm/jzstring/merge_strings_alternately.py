class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        shared_length = min(len(word1), len(word2))

        # The loop runs O(min(m, n)) times and appends two characters each time.
        for index in range(shared_length):
            merged.append(word1[index])
            merged.append(word2[index])

        # Appending the one remaining suffix is O(max(m, n)); total time is O(m + n).
        merged.append(word1[shared_length:])
        merged.append(word2[shared_length:])
        return "".join(merged)  # The output buffer uses O(m + n) space.
