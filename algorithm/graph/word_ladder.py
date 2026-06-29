from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        """BFS with wildcard pattern map. O(M*N) time and space, M=word length, N=word count."""
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        L = len(beginWord)
        wild_to_words: dict[str, list[str]] = defaultdict(list)
        for word in wordList:
            for i in range(L):  # O(M) patterns per word, O(N) words -> O(M*N) total
                wild_to_words[word[:i] + '*' + word[i + 1:]].append(word)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:  # O(N) words visited at most
            cur, level = queue.popleft()
            for i in range(L):  # O(M) patterns per word
                pattern = cur[:i] + '*' + cur[i + 1:]
                for neighbor in wild_to_words[pattern]:
                    if neighbor == endWord:
                        return level + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
        return 0

    def ladderLengthBidirectional(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        """Bidirectional BFS. O(M*N) time and space, but faster in practice."""
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        L = len(beginWord)
        front = {beginWord}
        back = {endWord}
        visited = {beginWord, endWord}
        level = 1
        while front and back:  # O(N) total expansion
            if len(front) > len(back):
                front, back = back, front
            next_front = set()
            for word in front:
                for i in range(L):  # O(M)
                    for c in 'abcdefghijklmnopqrstuvwxyz':  # O(26)
                        candidate = word[:i] + c + word[i + 1:]
                        if candidate in back:
                            return level + 1
                        if candidate in word_set and candidate not in visited:
                            visited.add(candidate)
                            next_front.add(candidate)
            front = next_front
            level += 1
        return 0
