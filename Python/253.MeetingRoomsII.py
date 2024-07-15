from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        #print(intervals)
        ans=0

        while (len(intervals)>0):
            ans+=1
            n=len(intervals)
            lastUsed=0
            nonUsed=[]
            for i in range(1,n):
                if intervals[i][0]>=intervals[lastUsed][1]:
                    lastUsed=i
                else:
                    nonUsed.append(intervals[i])
            intervals=nonUsed
            #print(nonUsed)
        return ans

s=Solution()
print(s.minMeetingRooms([(0,40),(5,10),(15,20)]))
print(s.minMeetingRooms([(4,9)]))
print(s.minMeetingRooms([(1,10),(2,3),(4,5),(6,7),(8,9)]))