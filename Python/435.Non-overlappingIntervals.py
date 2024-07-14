from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        if len(intervals)<=1: 
            return 0
        nonOverlap=1
        lastUsed=0
        for i in range(1,len(intervals)):
            if intervals[i][0]>=intervals[lastUsed][1]: #can use this one
                nonOverlap+=1
                lastUsed=i
        return len(intervals)-nonOverlap

s=Solution()
print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(s.eraseOverlapIntervals([[1,2],[2,3]]))