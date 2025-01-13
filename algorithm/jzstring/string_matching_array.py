"""leet 1408, hard"""


class Solution:
    """todo editorial"""

    class TrieNode:
        def __init__(self):
            # Tracks how many times this substring appears in the Trie.
            self.frequency = 0
            # Maps characters to their respective child nodes.
            self.child_nodes = {}

    def stringMatching(self, words: list[str]) -> list[str]:
        matching_words = []
        root = self.TrieNode()  # Initialize the root of the Trie.

        # Insert all suffixes of each word into the Trie.
        for word in words:
            for start_index in range(len(word)):
                # Insert each suffix starting from index start_index.
                self._insert_word(root, word[start_index:])

        # Check each word to see if it exists as a substring in the Trie.
        for word in words:
            if self._is_substring(root, word):
                matching_words.append(word)

        return matching_words

    def _insert_word(self, root: "TrieNode", word: str) -> None:
        current_node = root
        for char in word:
            if char not in current_node.child_nodes:
                # Create a new node if the character does not exist.
                current_node.child_nodes[char] = self.TrieNode()
            current_node = current_node.child_nodes[char]
            current_node.frequency += 1  # Increment the frequency of the node.

    def _is_substring(self, root: "TrieNode", word: str) -> bool:
        current_node = root
        for char in word:
            # Traverse the Trie following the characters of the word.
            current_node = current_node.child_nodes[char]
        # A word is a substring if its frequency in the Trie is greater than 1.
        return current_node.frequency > 1
