"""leet code 212, hard"""
from typing import List

from algorithm.string.impl_trie import Trie


# class Solution:
#     """time limit exceeded"""
#
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         trie = Trie()
#         for w in words: trie.insert(w)
#         res = set()
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if trie.startsWith(board[i][j]):
#                     self.dfs(board, trie, i, j, res, board[i][j])
#         return list(res)
#
#     def dfs(self, board, trie, i, j, res, candidate):
#         tmp = board[i][j]
#         board[i][j] = "#"
#         if trie.search(candidate): res.add(candidate)
#         dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
#         for d in dirs:
#             ni, nj = i + d[0], j + d[1]
#             if ni < 0 or ni > len(board) - 1 or nj < 0 or nj > len(board[0]) - 1 or board[ni][nj] == "#": continue
#             if trie.startsWith(candidate + board[ni][nj]):
#                 self.dfs(board, trie, ni, nj, res, candidate + board[ni][nj])
#         board[i][j] = tmp


class Solution(object):
    def findWords(self, board, words):
        res = set()
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                if c in node.next:
                    self.dfs(board, node, i, j, c, res)
        return list(res)

    def dfs(self, board, node, i, j, candidate, res):
        tmp = board[i][j]
        board[i][j] = "#"
        node = node.next[tmp]
        if node.is_word:
            res.add(candidate)
            # node.isWord = False
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        for d in dirs:
            ni, nj = i + d[0], j + d[1]
            if ni < 0 or ni > len(board) - 1 or nj < 0 or nj > len(board[0]) - 1 or board[ni][nj] == "#":
                continue
            if board[ni][nj] in node.next:
                self.dfs(board, node, ni, nj, candidate + board[ni][nj], res)
        board[i][j] = tmp


class Solution2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        m, n = len(board), len(board[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        root = Node()
        for w in words: root.insert(w)

        def dfs(r, c, node):
            if r < 0 or r > m - 1 or c < 0 or c > n - 1: return
            tmp = board[r][c]
            if tmp not in node.next or tmp == "#": return
            node = node.next[tmp]
            if node.word:
                res.append(node.word)
                node.word = None
            board[r][c] = "#"
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                dfs(nr, nc, node)
            board[r][c] = tmp

        for r in range(m):
            for c in range(n):
                dfs(r, c, root)
        return res


class Node:
    def __init__(self):
        self.word = None
        self.next = dict()

    def insert(self, word):
        n = self
        for c in word:
            if c not in n.next: n.next[c] = Node()
            n = n.next[c]
        n.word = word
