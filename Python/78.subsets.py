from typing import Optional, List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def subsets_int(ss=[], pos=0):
            if pos==len(nums): 
                ans.append(ss.copy())
                return
            ss.append(nums[pos])
            subsets_int(ss,pos+1)
            ss.pop()
            subsets_int(ss,pos+1)       
        subsets_int()     
        return ans

s=Solution()
print(s.subsets([1,2,3]))