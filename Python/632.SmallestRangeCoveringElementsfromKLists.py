from typing import List
import math
import heapq
class Solution:
    def smallestRange_list(self, nums: List[List[int]]) -> List[int]:
        n=len(nums)
        cur=[]
        for l in range(n):
            cur.append((nums[l][0],l))
        mindiff=math.inf
        idxs=[0]*n
        arange=[]
        while True:
            cur.sort()
            mi,ma=cur[0][0],cur[-1][0]
            diff=ma-mi
            if mindiff>diff:
                mindiff=diff
                arange=[mi,ma]
            
            miidx=cur[0][1]
            idxs[miidx]+=1
            if idxs[miidx]==len(nums[miidx]):
                break
            cur=cur[1:]+[(nums[miidx][idxs[miidx]],miidx)]

        return arange
        
        #using PQ
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap=[(row[0],i,0) for i,row in enumerate(nums)] #(min_val, list_idx, element_index)
        heapq.heapify(heap)
        
        max_val=max(row[0] for row in nums)
        min_range=float('inf')
        smallest_range=[]

        while heap:
            mi,list_idx,el_idx=heapq.heappop(heap)
            cur_range=max_val-mi

            if cur_range < min_range:
                min_range=cur_range
                smallest_range=[mi,max_val]
            
            if el_idx+1==len(nums[list_idx]):
                break

            next_val=nums[list_idx][el_idx+1]
            max_val=max(max_val,next_val)
            heapq.heappush(heap,(next_val,list_idx,el_idx+1))

        return smallest_range

s=Solution()
print(s.smallestRange(nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]])) # [20,24]
print(s.smallestRange(nums = [[1,2,3],[1,2,3],[1,2,3]])) # [1,1]