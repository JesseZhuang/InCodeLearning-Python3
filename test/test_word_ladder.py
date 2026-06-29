import unittest

from algorithm.graph.word_ladder import Solution


class TestWordLadder(unittest.TestCase):
    def setUp(self):
        self.solutions = [Solution()]

    def test_example1(self):
        for s in self.solutions:
            self.assertEqual(
                s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5
            )
            self.assertEqual(
                s.ladderLengthBidirectional(
                    "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
                ),
                5,
            )

    def test_end_word_not_in_list(self):
        for s in self.solutions:
            self.assertEqual(
                s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0
            )
            self.assertEqual(
                s.ladderLengthBidirectional(
                    "hit", "cog", ["hot", "dot", "dog", "lot", "log"]
                ),
                0,
            )

    def test_single_char(self):
        for s in self.solutions:
            self.assertEqual(s.ladderLength("a", "c", ["a", "b", "c"]), 2)
            self.assertEqual(s.ladderLengthBidirectional("a", "c", ["a", "b", "c"]), 2)

    def test_no_path(self):
        for s in self.solutions:
            self.assertEqual(s.ladderLength("hit", "cog", ["hot", "dot", "lot", "log"]), 0)
            self.assertEqual(
                s.ladderLengthBidirectional("hit", "cog", ["hot", "dot", "lot", "log"]), 0
            )

    def test_direct_neighbor(self):
        for s in self.solutions:
            self.assertEqual(s.ladderLength("hot", "dot", ["dot", "dog"]), 2)
            self.assertEqual(s.ladderLengthBidirectional("hot", "dot", ["dot", "dog"]), 2)

    def test_longer_path(self):
        for s in self.solutions:
            word_list = ["hot", "hat", "had", "bad", "bat", "bot"]
            self.assertEqual(s.ladderLength("hot", "bad", word_list), 4)
            self.assertEqual(s.ladderLengthBidirectional("hot", "bad", word_list), 4)


if __name__ == "__main__":
    unittest.main()
