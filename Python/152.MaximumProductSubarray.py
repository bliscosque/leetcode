from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def maxProdutWOZeros(nums: List[int]):
            if len(nums)==1: return nums[0]
            if len(nums)==0: return 0
            cnt=0
            first=-1
            last=-1
            for idx,n in enumerate(nums):
                if n<0: 
                    cnt+=1
                    if first==-1:
                        first=idx
                    last=idx
            #print(cnt,first,last)
            if cnt%2==0: 
                ans=1
                for n in nums:
                    ans*=n
                return ans
            else:
                # from beginning to before last negative
                prod1, prod2=1,1
                for n in nums[0:last]:
                    prod1*=n
                # after first negative to the end
                for n in nums[first+1:]:
                    prod2*=n
                return max(prod1,prod2)

        if 0 not in nums:
            return maxProdutWOZeros(nums)

        ans=0
        while 0 in nums:
            idx0=nums.index(0)
            ans=max(ans,maxProdutWOZeros(nums[:idx0]))
            nums=nums[idx0+1:]

        return ans

s=Solution()
print(s.maxProduct([0,2,3,-2,4,0]))
print(s.maxProduct([-1,-2,0,-1]))
print(s.maxProduct([0,2])) #2