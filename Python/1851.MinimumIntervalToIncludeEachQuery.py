from typing import List
import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        h=[] # valid intervals in format (size,right)
        heapq.heapify(h)

        queries_with_index=[(q,i) for i,q in enumerate(queries)]
        queries_with_index.sort()

        intervals.sort()
        
        lastInterval=0
        ans=[-1]*len(queries)

        for q,orig_index in queries_with_index:
            # while I have intervals that can be used for that query, add it to possible answers
            while lastInterval<len(intervals) and intervals[lastInterval][0]<=q:
                size=intervals[lastInterval][1]-intervals[lastInterval][0]+1
                heapq.heappush(h,(size,intervals[lastInterval][1])) 
                lastInterval+=1

            # get min interval that is valid
            
            if len(h)==0:
                ans[orig_index]=-1
                continue
            
            minInterval=heapq.heappop(h)
            while len(h)>=1 and minInterval[1]<q:
                minInterval=heapq.heappop(h)
            if minInterval[1]<q:
                ans[orig_index]=-1
                continue

            ans[orig_index]=minInterval[0]
            heapq.heappush(h,minInterval)
        
        return ans                    

s=Solution()
print(s.minInterval(intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5])) #[3,3,1,4]
print(s.minInterval([[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22])) #[2,-1,4,6]