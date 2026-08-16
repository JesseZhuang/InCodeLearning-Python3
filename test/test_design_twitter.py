import unittest

from algorithm.heap.design_twitter import Twitter


class TestDesignTwitter(unittest.TestCase):
    def setUp(self):
        self.solutions = [Twitter]

    def test_example(self):
        """LeetCode example case."""
        for Cls in self.solutions:
            tw = Cls()
            tw.postTweet(1, 5)
            self.assertEqual(tw.getNewsFeed(1), [5])
            tw.follow(1, 2)
            tw.postTweet(2, 6)
            self.assertEqual(tw.getNewsFeed(1), [6, 5])
            tw.unfollow(1, 2)
            self.assertEqual(tw.getNewsFeed(1), [5])

    def test_empty_feed(self):
        """User with no tweets and no followees."""
        for Cls in self.solutions:
            tw = Cls()
            self.assertEqual(tw.getNewsFeed(1), [])

    def test_max_ten_tweets(self):
        """Feed should return at most 10 tweets."""
        for Cls in self.solutions:
            tw = Cls()
            for i in range(1, 15):
                tw.postTweet(1, i)
            feed = tw.getNewsFeed(1)
            self.assertEqual(len(feed), 10)
            self.assertEqual(feed, [14, 13, 12, 11, 10, 9, 8, 7, 6, 5])

    def test_follow_self(self):
        """Following self should not duplicate tweets in feed."""
        for Cls in self.solutions:
            tw = Cls()
            tw.postTweet(1, 100)
            tw.follow(1, 1)
            self.assertEqual(tw.getNewsFeed(1), [100])

    def test_unfollow_non_followee(self):
        """Unfollowing someone not followed should not error."""
        for Cls in self.solutions:
            tw = Cls()
            tw.unfollow(1, 2)  # should not raise

    def test_multiple_users_interleaved(self):
        """Tweets from multiple followees merged in time order."""
        for Cls in self.solutions:
            tw = Cls()
            tw.postTweet(1, 10)
            tw.postTweet(2, 20)
            tw.postTweet(1, 11)
            tw.postTweet(2, 21)
            tw.follow(1, 2)
            feed = tw.getNewsFeed(1)
            self.assertEqual(feed, [21, 11, 20, 10])

    def test_unfollow_then_follow_again(self):
        """Re-following should restore tweets in feed."""
        for Cls in self.solutions:
            tw = Cls()
            tw.postTweet(2, 50)
            tw.follow(1, 2)
            self.assertEqual(tw.getNewsFeed(1), [50])
            tw.unfollow(1, 2)
            self.assertEqual(tw.getNewsFeed(1), [])
            tw.follow(1, 2)
            self.assertEqual(tw.getNewsFeed(1), [50])


if __name__ == "__main__":
    unittest.main()
