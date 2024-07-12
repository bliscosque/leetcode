from typing import List
import copy
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s,e=newInterval
        spos,epos=-1,-1
        sposmid, eposmid=False, False
        for idx,interval in enumerate(intervals):
            si, ei=interval
            if si<=s<=ei:
                spos=idx
                sposmid=True

            if s>ei:
                spos=idx+1

            if si<=e<=ei:
                epos=idx
                eposmid=True
            
            if e < si:
                epos=idx-1

            
            
        print(spos,epos,sposmid, eposmid)


        # only 1 interval affected - no merge needed
        if spos==epos: 
            intervals[spos][0]=min(intervals[spos][0],newInterval[0])
            intervals[spos][1]=max(intervals[spos][1],newInterval[1])
            return intervals

        # merge is needed
        ans=intervals[0:spos+1]
        ans[spos][0]=min(intervals[spos][0],newInterval[0])
        ans[spos][1]=max(intervals[epos][1],newInterval[1])

        ans+=intervals[epos+1:]

        return ans
        



s=Solution()
#print(s.insert([[1,3],[6,9]],[0,1]))
print(s.insert([[1,3],[6,9]],[2,5]))
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))