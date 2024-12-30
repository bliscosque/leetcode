from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0: return 0
        sumlr=[nums[0]]
        sumrl=[nums[n-1]]
        for i in range(1,n):
            sumlr.append(nums[i]+sumlr[i-1])
        for i in range(n-2,-1,-1):
            sumrl.append(nums[i]+sumrl[-1])
        sumrl.reverse()
        #print(sumlr,sumrl)

        if  sumrl[1]==0: 
            return 0
        
        for i in range(1,n-1):
            if sumlr[i-1]==sumrl[i+1]:
                return i
        
        if sumlr[-2]==0:
            return n-1

        return -1

s=Solution()
print(s.pivotIndex([1,7,3,6,5,6])) # 3
print(s.pivotIndex([1,2,3])) # -1
print(s.pivotIndex([2,1,-1])) # 0
print(s.pivotIndex([-1,1,2])) # 2
