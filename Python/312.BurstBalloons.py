from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]
        n=len(nums)
        dp={}
        
        def maxCoinsInt(l,r):            
            if (l,r) in dp: 
                return dp[(l,r)]
            if l+1==r: 
                return 0
            
            ans=0
            for i in range(l+1,r):
                coins=nums[l]*nums[i]*nums[r]
                coins+=maxCoinsInt(l,i)+maxCoinsInt(i,r)
                ans=max(ans,coins)
            
            dp[(l,r)]=ans
            return ans

        return maxCoinsInt(0,n-1)

s=Solution()
print(s.maxCoins([3,1,5,8])) #167
print(s.maxCoins([1,5])) #10
print(s.maxCoins([7,9,8,0,7,1,3,5,5,2])) # 1582
print(s.maxCoins([8,2,6,8,9,8,1,4,1,5,3,0,7,7,0,4,2,2])) #3446