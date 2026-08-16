"""
LeetCode 355. Design Twitter
https://leetcode.com/problems/design-twitter/

Design a simplified version of Twitter where users can post tweets,
follow/unfollow another user, and get the 10 most recent tweets in the user's news feed.

Solution 1: HashMap + Heap (merge k sorted lists approach)
- postTweet: O(1)
- getNewsFeed: O(k log k) where k = number of followees, at most 10 iterations
- follow/unfollow: O(1)
- Space: O(total tweets + total follow relationships)
"""

import heapq
from collections import defaultdict


class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)  # userId -> [(time, tweetId)]
        self.followees = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1  # negative for max-heap via min-heap
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        # O(k) to build heap where k = number of followees + 1(self)
        heap = []
        self.followees[userId].add(userId)
        for followeeId in self.followees[userId]:
            if self.tweets[followeeId]:
                idx = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][idx]
                heap.append((time, tweetId, followeeId, idx))
        heapq.heapify(heap)  # O(k)

        res = []
        while heap and len(res) < 10:  # O(10 * log k)
            time, tweetId, followeeId, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx > 0:
                idx -= 1
                time, tweetId = self.tweets[followeeId][idx]
                heapq.heappush(heap, (time, tweetId, followeeId, idx))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)
