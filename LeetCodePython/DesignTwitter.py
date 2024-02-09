from collections import defaultdict
class Twitter:

    def __init__(self):
        self.twit = defaultdict(list)
        self.follow = defaultdict(set())
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.twit[userId].append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        if len(self.twit[userId]) >= 10:
            return self.twit[userId][-10:]
        else:
            return self.twit[userId]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)