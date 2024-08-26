from typing import List
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n=len(nums)
        dp={}
        def hammingDistance(n1,n2):
            if (n1,n2) in dp: return dp[(n1,n2)]
            if (n2,n1) in dp: return dp[(n2,n1)]
            ans=0
            while n1 or n2:
                if n1&1 != n2&1: 
                    ans+=1
                n1=n1>>1
                n2=n2>>1

            dp[(n1,n2)]=ans
            return dp[(n1,n2)]
        
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                ans+=hammingDistance(nums[i],nums[j])
        return ans



s=Solution()
print(s.totalHammingDistance([4,14,2])) # 6
print(s.totalHammingDistance([4,14,4])) # 4