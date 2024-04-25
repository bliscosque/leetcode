from typing import Optional, List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        used=[False]*len(nums)
        def permute_int(parc=[]):
            if len(parc)==len(nums):
                ans.append(parc.copy())
            for i in range(len(nums)):
                if not used[i]:
                    used[i]=True
                    parc.append(nums[i])
                    
                    permute_int(parc)
                    
                    parc.pop()
                    used[i]=False
        permute_int()
        return ans

s=Solution()
print(s.permute([1,2,3]))