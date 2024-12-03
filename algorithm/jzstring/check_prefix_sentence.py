"""leet 1455, easy """


class Solution:
    """todo 0 ms, 17.4 mb"""

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # Split the sentence into words
        words = sentence.split()
        # Iterate over the words with their positions (starting from 1)
        for i, word in enumerate(words, 1):
            # Check if the current word starts with the searchWord
            if word[: len(searchWord)] == searchWord:
                # If a match is found, return the current word position
                return i
        # If no match is found, return -1
        return -1
