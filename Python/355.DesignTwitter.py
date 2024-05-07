from typing import Optional, List

import heapq
class Twitter:

    def __init__(self):
        self.userFollow={} # HM de UID -> Set de FoloweeId
        self.userTweet={} # HM de UID -> [(count,TweetID)]
        self.cnt=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not userId in self.userTweet:
            self.userTweet[userId]=[(self.cnt,tweetId)]
        else:
            self.userTweet[userId].append((self.cnt,tweetId))
        self.cnt-=1
        #print(self.userTweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        ans=[]
        minHeap=[]

        self.follow(userId,userId)

        for followeeId in self.userFollow[userId]:
            if followeeId in self.userTweet:
                lastIdx=len(self.userTweet[followeeId]) - 1
                cnt,tId=self.userTweet[followeeId][lastIdx]
                minHeap.append((cnt,tId,followeeId,lastIdx-1))
        heapq.heapify(minHeap)
        while minHeap and len(ans)<10:
            cnt,tId,followeeId,lastIdx = heapq.heappop(minHeap)
            ans.append(tId)
            #add again last val
            if lastIdx>=0:
                cnt,tId = self.userTweet[followeeId][lastIdx]
                heapq.heappush(minHeap,(cnt,tId,followeeId,lastIdx-1))
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userFollow:
            self.userFollow[followerId].add(followeeId)
        else:
            self.userFollow[followerId]={followeeId}
        #print(self.userFollow)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userFollow:
            self.userFollow[followerId].remove(followeeId)
        #print(self.userFollow)

# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1,5)
print(obj.getNewsFeed(1))
obj.follow(1,2)
obj.postTweet(2,6)
print(obj.getNewsFeed(1))
obj.unfollow(1,2)
print(obj.getNewsFeed(1))

print()

obj2=Twitter()
obj2.postTweet(1,4)
obj2.postTweet(2,5)
obj2.unfollow(1,2)
print(obj.getNewsFeed(1))