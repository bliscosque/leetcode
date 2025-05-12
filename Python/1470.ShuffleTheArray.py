from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[n+i])
        return ans

s=Solution()
print(s.shuffle(nums = [2,5,1,3,4,7], n = 3))