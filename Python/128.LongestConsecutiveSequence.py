from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        ans=0
        for el in s:
            if (el-1) not in s:
                ans1=1
                cur=el+1
                while cur in s:
                    cur+=1
                    ans1+=1
                ans=max(ans,ans1)
        return ans

        
s=Solution()
print(s.longestConsecutive([100,4,200,1,3,2])) #4
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])) #9
print(s.longestConsecutive([1,0,1,2])) #3