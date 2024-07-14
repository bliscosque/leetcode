from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        intervals.sort()
        ans.append(intervals[0])

        for cur_start,cur_end in intervals[1:]:
            last_start,last_end=ans[-1][0],ans[-1][1]
            if last_start<=cur_start<=last_end:
                ans[-1][1]=max(last_end,cur_end)
            else:
                ans.append([cur_start,cur_end])

        return ans

s=Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
print(s.merge([[1,4],[4,5]]))